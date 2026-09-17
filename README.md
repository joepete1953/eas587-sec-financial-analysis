# Scalable Analysis and Anomaly Detection in SEC Corporate Filings

This repository contains the semester project for EAS 587 – Data-Intensive Computing.

The project uses the U.S. Securities and Exchange Commission Financial Statement and Notes Data Sets to study changes in corporate financial health and unusual reporting patterns across companies and industries.

The SEC dataset contains both numerical financial information and textual disclosures from public company filings. The project will begin with data access, cleaning and exploratory analysis, and later move toward distributed processing using Apache Spark and machine learning or anomaly detection methods where appropriate.

## Team Members

- Joebin Peter Soosairaj
- Shreyas Aravind

## Dataset

Primary dataset:

SEC Financial Statement and Notes Data Sets

Source:

https://www.sec.gov/data-research/sec-markets-data/financial-statement-notes-data-sets

The dataset contains eight related tables:

- SUB – filing and company information
- TAG – definitions of financial reporting tags
- DIM – reporting dimensions
- NUM – numerical financial facts
- TXT – textual disclosures
- REN – report rendering information
- PRE – presentation relationships
- CAL – calculation relationships

For Phase 1, a small sample from the January 2026 package is included in this repository. The full historical SEC dataset is not stored in GitHub because of its size.

## Project Structure

```text
eas587-sec-financial-analysis/
│
├── README.md
├── requirements.txt
├── research_plan.md
├── .gitignore
│
├── data/
│   ├── samples/
│   │   ├── sub_sample.csv
│   │   ├── num_sample.csv
│   │   ├── txt_sample.csv
│   │   └── tag_sample.csv
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── data_access.py
│   └── data_sampling.py
│
├── notebooks/
└── presentation/