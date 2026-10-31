# Automated Audit Data Analytics

A Python-based continuous auditing tool designed to process transaction data and identify compliance risks.

# Audit Procedures

* Duplicate Detection: Scans the ledger for exact duplicate entries to prevent double-posting.
* Threshold Filtering: Filters transactions exceeding material thresholds (amounts > 10,000) for review.
* User Aggregation: Summarizes total transaction volumes by `user_id`.
* Time-Based Risk Analysis: Identifies weekend transactions (Saturdays and Sundays) as potential indicators of irregular postings.
* Benford's Law Analysis: Performs a first-digit statistical analysis to detect anomalies and potential data manipulation.

# Tech Stack

Language: Python
Library: Pandas

# Repository Structure

* `automated-audit-analytics` - Main execution script
* `general_ledger_sample.csv` - Sample dataset
* `README.md` - Documentation

# Usage

1. Install dependencies:
   ```bash
   pip install pandas
