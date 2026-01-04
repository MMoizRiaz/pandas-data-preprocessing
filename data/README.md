# Dataset Information

This folder contains the datasets used in the **Pandas Data Preprocessing** project.

The data is intentionally **small and messy** to demonstrate common real-world data quality issues and how to handle them using Pandas.

---

## Files

### `sample.csv`
Raw input dataset used for practice.

It intentionally includes:
- missing values
- empty strings and extra whitespace
- inconsistent categorical values
- mixed date formats
- numeric values stored as strings
- duplicate records
- invalid or placeholder values

This file is the **starting point** for all preprocessing steps shown in the project.

---

### `cleaned_sample.csv`
Cleaned dataset generated after running `pandas_preprocessing.py`.

It represents the output after:
- cleaning and normalizing strings
- handling missing values
- converting numeric and datetime columns
- applying sanity checks
- removing duplicates

This file is **generated automatically** and can be safely deleted and recreated by rerunning the script.

---

## Purpose

The datasets in this folder are designed for:
- learning Pandas data preprocessing
- demonstrating step-by-step cleaning via Git commits
- keeping the project lightweight and easy to understand

You can replace `sample.csv` with your own dataset as long as the column names remain compatible with the preprocessing script.

---

## Notes

- These datasets are for **educational and demonstration purposes only**.

