import pandas as pd

# --- Load the CSV file into a Pandas DataFrame ---
data = pd.read_csv('customer_data.csv')

# --- Handle missing values ---
data.fillna('', inplace=True)  # Replace missing values with empty strings

# --- Eradicate unique characters ($) ---
data['Purchase 1'] = data['Purchase 1'].astype(str).str.replace('$', '')
data['Purchase 2'] = data['Purchase 2'].astype(str).str.replace('$', '')
data['Purchase 3'] = data['Purchase 3'].astype(str).str.replace('$', '')

# --- Set the type of data ---
for x in range(len(data)):
    try:
        data['Purchase 1'][x] = int(data['Purchase 1'][x])
        data['Purchase 2'][x] = int(data['Purchase 2'][x])
        data['Purchase 3'][x] = int(data['Purchase 3'][x])
    except ValueError:
        data['Purchase 1'][x] = 0
        data['Purchase 2'][x] = 0
        data['Purchase 3'][x] = 0

# --- Standardize formatting for Customer Name ---
data['Customer Name'] = data['Customer Name'].str.title()

# --- Save the cleaned dataset ---
data.to_csv('cleaned_customer_data.csv', index=False)

# ==========================
# Example 2: Analysis Section
# ==========================

# Calculate the total spent by each customer
data['Total Spent'] = data[
    'Purchase 1'] + data['Purchase 2'] + data['Purchase 3']

# Group data by customer and calculate aggregate statistics
summary = (
    data.groupby('Customer Name')
    .agg({
        'Total Spent': 'sum',
        'Purchase 1': 'count'
    })
    .rename(columns={'Purchase 1': 'Number of Purchases'})
)

# Sort the summary by total spent in descending order
summary = summary.sort_values('Total Spent', ascending=False)

# Print the summary
print(summary)

# Save summary to file
summary.to_csv('customer_summary.csv')
