# Automation Projects

A curated collection of practical automation projects built with Python, focused on solving real workflow, data processing, reporting, and system integration problems.

This repository was created to demonstrate hands-on automation engineering skills for software engineering, data operations, back-office automation, and workflow optimization opportunities.

## Problem Solved

Many companies still rely on repetitive manual tasks such as cleaning spreadsheets, sending reports, importing CSV files, extracting information from messages, and synchronizing data between systems.

These projects show how Python can be used to reduce manual work, improve data quality, automate recurring processes, and connect different tools through scripts, APIs, and databases.

## Business Value

This repository demonstrates automation patterns that can be applied to:

* Back-office process automation
* Data cleaning and standardization
* Report generation
* API integrations
* Database imports
* Operational workflow automation
* Message parsing and structured data extraction
* Repetitive task reduction

The main goal is to show how small automation tools can evolve into production-ready internal systems.

## Projects Overview

### 1. Email Report Automation

Generates summary reports and sends them automatically by email.

**Use case:** daily, weekly, or monthly operational reports.

**Business value:** reduces manual reporting work and improves communication consistency.

### 2. Spreadsheet Data Cleaner

Cleans, standardizes, and organizes spreadsheet or CSV data.

**Use case:** preparing messy operational data for analysis, import, or reporting.

**Business value:** improves data quality and reduces manual spreadsheet corrections.

### 3. WhatsApp Message Parser

Extracts useful structured data from exported WhatsApp messages.

**Use case:** converting unstructured conversations into organized records.

**Business value:** helps transform informal communication into searchable and processable data.

### 4. CSV to Database Importer

Imports CSV files into a database with basic validation.

**Use case:** moving spreadsheet-based data into a structured database.

**Business value:** reduces manual data entry and creates a more reliable data workflow.

### 5. API Data Sync

Synchronizes data between two APIs or between an API and a local database.

**Use case:** keeping information updated across different systems.

**Business value:** reduces duplicate work, improves consistency, and supports system integration.

## Repository Structure

```txt
automation-projects/
├── email-report-automation/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
├── spreadsheet-data-cleaner/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
├── whatsapp-message-parser/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
├── csv-to-database-importer/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
├── api-data-sync/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
└── README.md
```

## Tech Stack

* Python
* CSV processing
* SQLite
* Email automation
* API synchronization
* Data validation
* File processing
* Workflow automation

## Quick Start

Enter one of the project folders:

```bash
cd spreadsheet-data-cleaner
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the script:

```bash
python main.py --input sample.csv --output cleaned.csv
```

Each project folder contains its own README with specific usage instructions.

## What This Repository Demonstrates

This repository demonstrates:

* Practical automation thinking
* Python scripting
* Data cleaning
* API integration
* Basic database workflows
* File processing
* Reusable internal tools
* Problem-solving through automation

## Portfolio Goal

The goal of this repository is to show practical automation engineering skills through clean, runnable examples that solve real workflow problems and can evolve into production-grade internal tools.
