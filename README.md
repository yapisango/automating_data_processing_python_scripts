# Automating Data Processing with Python

This project demonstrates how to automate **customer data cleaning and analysis** using Python.  
It includes both a **Python script** and a **Jupyter Notebook** for flexible use.

---

## 📂 Project Structure
- `data_automation.py` → Python script that cleans and processes data in one go.  
- `data_automation.ipynb` → Jupyter Notebook version for interactive exploration.  
- `customer_data.csv` → Example raw dataset.  
- `cleaned_customer_data.csv` → Output file with cleaned data (generated after running the script).  
- `.gitignore` → Ensures unnecessary files (e.g., virtual environments, cache) are not pushed to GitHub.  

---

## ✨ Features
- Cleans inconsistent purchase data  
- Handles missing or invalid values by defaulting them to `0`  
- Converts purchase values to integers  
- Generates a cleaned dataset for further analysis  

---

## 🛠️ Requirements
- Python 3.8+  
- [pandas](https://pandas.pydata.org/)  

Install dependencies with:
```bash
pip install pandas
