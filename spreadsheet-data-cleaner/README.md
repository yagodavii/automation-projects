# Spreadsheet Data Cleaner

Clean, standardize, and organize CSV data.

## Features
- Trims extra whitespace
- Standardizes column names
- Removes duplicate rows
- Sorts data by a selected column

## Setup

```bash
pip install -r requirements.txt
```

## Usage

### Clean a CSV file

```bash
python main.py --input raw_data.csv --output cleaned_data.csv
```

### Clean and sort by a column

```bash
python main.py --input raw_data.csv --output cleaned_data.csv --sort-by customer_name
```
