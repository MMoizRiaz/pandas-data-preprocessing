# Pandas Data Preprocessing – Commit-by-Commit Learning

This repository demonstrates **practical data preprocessing using Pandas**, implemented in a **single Python file** and developed **step by step through Git commits**.

The goal of this project is:
1. Practice real-world Pandas data cleaning techniques
2. Demonstrate clean, incremental Git usage and commit history

---

## How to Explore This Repository (Important)

This project is intentionally built using **one Python file**:  
`pandas_preprocessing.py`

Each preprocessing technique is introduced in a **separate Git commit**.

**To follow the learning progression:**
1. Open `pandas_preprocessing.py`
2. Click **History**
3. Start from **Commit 1 (or Commit 2)** and move forward commit by commit

Each commit adds exactly **one new preprocessing concept**, such as:
- loading & inspecting data
- cleaning strings and whitespace
- handling missing values
- numeric and datetime conversion
- sanity checks and deduplication
- building a reusable preprocessing pipeline

The Git history itself is part of the learning material.

---

## Preprocessing Techniques Covered

- Column name standardization
- Whitespace and string normalization
- Handling empty values and missing data
- Categorical normalization
- Numeric cleaning and safe coercion
- Datetime parsing with mixed formats
- Missing value strategies (mean / median / labels)
- Duplicate removal
- Basic sanity checks
- Building a reusable preprocessing pipeline

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/MMoizRiaz/pandas-data-preprocessing.git
cd pandas-data-preprocessing
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the preprocessing script:
```bash
python pandas_preprocessing.py
```
## Project Structure
```
.
├── pandas_preprocessing.py
├── requirements.txt
├── data/
│   ├── sample.csv
│   ├── cleaned_sample.csv
│   └── README.md
└── README.md
