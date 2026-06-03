# CSV To Database Importer

Import CSV files into a SQLite database with basic data validation.

## Features
- CSV import into SQLite
- Automatic table creation
- Required-column validation
- Empty-value validation

## Setup

```bash
pip install -r requirements.txt
```

## Usage

### Import a CSV file

```bash
python main.py --csv customers.csv --db app.db --table customers
```

### Require specific columns

```bash
python main.py --csv customers.csv --db app.db --table customers --required email name
```
