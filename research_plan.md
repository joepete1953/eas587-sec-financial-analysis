# Scalable Detection of Financial Health Changes and Reporting Anomalies in SEC Corporate Filings

**Created By:**  
Joebin Peter Soosairaj  
Shreyas Aravind

**Version:**  
1.0

**Target Community of Interest:**  
Financial analysts, researchers, regulators and organizations interested in understanding corporate financial reporting and changes in company financial health.

**Date Created:**  
September 17, 2026

**Last Updated:**  
September 17, 2026

**GitHub Repository:**  
https://github.com/joepete1953/eas587-sec-financial-analysis


## 1. Research Goal

Public companies submit large amounts of financial information to the U.S. Securities and Exchange Commission every year. Looking at one company or one filing is manageable, but looking across thousands of companies, several industries and many years quickly becomes a much larger data problem.

The goal of this project is to explore whether this large collection of SEC filings can be processed at scale to identify meaningful changes in company financial health and unusual reporting patterns. We will use the SEC Financial Statement and Notes Data Sets, which contain both numerical financial information and textual disclosures reported by public companies.

The project will begin with understanding and cleaning the different SEC tables and then move toward large-scale exploratory analysis. In the later stages, distributed processing and machine learning techniques will be explored to identify patterns that may be difficult to notice by manually looking at individual filings.

The expected outcome is a scalable analytical pipeline that can process SEC filing data across companies and time, summarize important changes in financial information and highlight filings or companies that show unusual patterns for further investigation.

### Primary Research Question

How can large-scale numerical and textual information from SEC corporate filings be processed and analyzed to identify significant changes in corporate financial health and unusual reporting patterns?

### Supporting Questions

1. Which financial measures and ratios show the largest changes over time within companies and industries?

2. Can unusual changes in financial values or disclosure patterns be identified automatically across a large number of filings?

3. Are some types of financial or reporting changes more common in particular industries?

4. How can distributed processing tools such as Apache Spark make the analysis of many years of SEC filing data more practical?


## 2. Background and Motivation

Companies listed in the United States regularly file reports such as 10-K and 10-Q forms with the SEC. These reports contain information about revenue, assets, liabilities, income, cash flow and many other parts of a company's financial position. They also contain detailed notes explaining accounting policies, commitments, risks and other information that may not be obvious from the financial statements alone.

For an individual company, this information can be reviewed manually. The difficulty appears when the goal is to compare thousands of filings across many companies and many years. Financial concepts can appear repeatedly under different reporting contexts, companies may use different XBRL tags, and the information is spread across several connected tables rather than being available as one clean dataset.

This makes the problem interesting from a data-intensive computing point of view. The challenge is not simply calculating financial ratios. The data first has to be downloaded or accessed in manageable pieces, understood, joined correctly, cleaned and transformed before useful analysis can be carried out.

There is also a practical reason for studying the data. Large changes in financial values or the way information is disclosed may provide useful signals about changes taking place within a company. The goal of this project is not to label a company as good or bad, or to make investment recommendations. Instead, the project aims to identify unusual changes and patterns that may deserve closer investigation.

The SEC Financial Statement and Notes Data Sets are useful for this because they provide both detailed numerical information and narrative disclosures directly from corporate filings. The dataset currently covers filings from 2009 through 2026 and is updated regularly by the SEC.


## 3. Research Objectives and Scope

### Objectives

The first objective is to build a reliable process for accessing and combining the different tables contained in the SEC Financial Statement and Notes Data Sets.

The second objective is to understand the structure and quality of the data, including missing values, repeated financial concepts, reporting dimensions and differences between companies and industries.

The third objective is to perform large-scale exploratory analysis of important financial measures such as revenue, assets, liabilities, income and cash flow across companies and over time.

The fourth objective is to create useful financial features and measures that describe changes in company financial health.

The fifth objective is to investigate methods for identifying unusual financial or reporting behavior. These may include statistical methods, anomaly detection techniques or machine learning approaches depending on what is learned during the exploratory analysis.

The final objective is to move the processing workflow toward Apache Spark or another distributed approach so that a larger part of the historical SEC dataset can be analyzed efficiently.

### In Scope

The project will focus on:

- SEC Financial Statement and Notes data
- Corporate financial filings such as 10-K and 10-Q reports
- Numerical financial facts
- Selected textual disclosures
- Changes in financial measures over time
- Comparisons between companies and industries
- Detection of unusual financial and reporting patterns
- Large-scale processing using Apache Spark
- Exploratory machine learning where appropriate

### Out of Scope

The project will not attempt to:

- Recommend stocks or investment decisions
- Predict exact future stock prices
- Determine whether a company has committed fraud
- Replace professional financial analysis
- Process every piece of information available in the complete SEC EDGAR system
- Build a production financial trading system

Keeping these areas outside the project helps keep the work focused on scalable financial-data analysis rather than trying to solve every possible financial problem.


## 4. Prior Research and References

Previous research has shown that corporate financial information can be useful for identifying financial distress and other changes in company health. Traditional approaches commonly use accounting ratios, while more recent studies have explored machine learning and textual information from corporate reports.

Zhao, Xu and Ji studied financial distress prediction using both detailed financial data and Management Discussion and Analysis text. Their results showed that detailed financial data provides useful predictive information and that textual disclosures can provide additional information in some settings.

Hajek and Munk investigated the use of risk-related text from annual reports for financial distress prediction. Their work used natural language processing and machine learning techniques to extract information from corporate disclosures.

Other recent research has also explored machine learning approaches for financial distress prediction and has shown that models can identify relationships between financial indicators that may be difficult to capture using traditional methods alone.

Our project differs slightly from these studies because the main focus is not only prediction. We first want to build a scalable data pipeline capable of processing many years of SEC filings and then investigate changes and anomalies across companies and industries. Predictive modeling may be introduced later after the large-scale data processing and exploratory work is complete.

### Initial References

1. U.S. Securities and Exchange Commission. "Financial Statement and Notes Data Sets."  
   https://www.sec.gov/data-research/sec-markets-data/financial-statement-notes-data-sets

2. U.S. Securities and Exchange Commission. "Financial Statement and Notes Data Sets – Technical Documentation."  
   https://www.sec.gov/files/fsnds_2.pdf

3. Zhao, Q., Xu, W., and Ji, Y. (2023). "Predicting financial distress of Chinese listed companies using machine learning: To what extent does textual disclosure matter?" International Review of Financial Analysis, 89, 102770.  
   https://doi.org/10.1016/j.irfa.2023.102770

4. Hajek, P., and Munk, M. (2024). "Corporate financial distress prediction using the risk-related information content of annual reports." Information Processing & Management, 61, 103820.  
   https://doi.org/10.1016/j.ipm.2024.103820

5. Nour, A. N. I., Lokanan, M. E., and Ramzan, S. (2024). "Predicting financial distress in TSX-listed firms using machine learning algorithms."  
   https://pmc.ncbi.nlm.nih.gov/articles/PMC11631907/

The reference list will be expanded as the project develops, especially once the final anomaly detection and machine learning methods have been selected.


## 5. Supporting Data and Resources

### Primary Dataset

The primary dataset for this project is the **SEC Financial Statement and Notes Data Sets** published by the U.S. Securities and Exchange Commission.

Dataset source:

https://www.sec.gov/data-research/sec-markets-data/financial-statement-notes-data-sets

The collection contains financial information extracted from XBRL corporate filings. It currently covers filings from 2009 to August 2026.

The SEC provides the data as monthly and quarterly ZIP archives. Across the available historical files, the compressed collection is roughly 25 GB. Once extracted, the amount of data is considerably larger.

The dataset contains eight connected tables:

- SUB - information about the company and filing
- TAG - information describing XBRL financial tags
- DIM - reporting dimensions and additional context
- NUM - numerical financial facts
- TXT - textual disclosures
- REN - information about how filings are rendered
- PRE - presentation relationships
- CAL - calculation relationships

The common filing identifier `adsh` allows several of these tables to be connected back to a particular SEC submission.

### Initial Data Inspection

Before committing to the dataset, we downloaded and inspected the January 2026 monthly package.

The package itself was approximately 41 MB compressed.

Our initial inspection found:

- 5,428 submission records in the SUB table
- 505,197 numerical financial facts in the NUM table
- 190,846 textual facts in the TXT table

We also filtered the text data for disclosures longer than 500 characters and found 8,404 longer narrative disclosures in this single monthly package.

Examples included disclosures related to:

- accounting policies
- commitments and contingencies
- financial instruments
- revenue
- compensation
- earnings per share

This initial test confirmed that the dataset contains both structured numerical information and useful narrative financial disclosures.

### Why This Is a Data-Intensive Computing Problem

The complete dataset cannot be treated as one simple CSV file.

The data is divided across many historical archives and eight connected tables. A meaningful analysis requires joining large numbers of financial facts with submission information, XBRL tags, dimensions and other supporting tables.

The project also covers many years of filings and thousands of companies. Processing the complete history using a normal in-memory pandas workflow would become increasingly slow and inefficient.

For this reason, the project will use smaller samples during development and progressively move toward distributed processing for the larger historical dataset.

### Data Access Strategy

The entire SEC collection will not be permanently downloaded to a local laptop.

Instead, monthly or quarterly archives will be downloaded or accessed when required. The relevant tables will be processed and converted into more efficient formats such as Parquet where appropriate.

This allows the project to work with the full historical source while keeping local storage requirements manageable.

### Software and Computing Resources

The expected tools for the project include:

- Python
- Pandas
- Apache Spark / PySpark
- Jupyter or Google Colab for initial exploration
- Visual Studio Code
- Git and GitHub
- Parquet for processed data storage
- Scikit-learn for later machine learning experiments
- NLP libraries if textual disclosures are used in later phases

Cloud or university computing resources may be used for larger Spark jobs if processing the complete dataset locally becomes impractical.


## 6. Risks, Constraints, Assumptions and Open Questions

### Data Complexity

SEC filings use XBRL, which means the same financial concept can appear under different contexts, dimensions or company-specific tags. A value that appears duplicated may therefore represent a different reporting context rather than an actual duplicate.

**Mitigation:**  
The project will use the SEC documentation and the TAG and DIM tables to understand these differences before removing or aggregating records.

### Dataset Size

Processing the complete historical collection locally may exceed the available storage or memory on a normal laptop.

**Mitigation:**  
The data will be processed in monthly or quarterly batches. Larger experiments will use Spark and, if required, cloud or university computing resources.

### Data Quality

The SEC states that the dataset is created from information filed by individual registrants and does not guarantee that every value is free from errors.

**Mitigation:**  
Basic validation, missing-value checks and consistency checks will be included during preprocessing. Where necessary, suspicious records will be checked against the original filing.

### Company-to-Company Differences

Companies may report similar information using different XBRL tags or structures.

**Mitigation:**  
The project will initially focus on widely used financial concepts and gradually expand the feature set after understanding the taxonomy.

### Defining an Anomaly

An unusual financial change does not automatically mean something is wrong. A large change could be caused by an acquisition, restructuring, unusual economic conditions or another legitimate event.

**Mitigation:**  
The project will describe detected cases as unusual patterns or anomalies rather than automatically treating them as fraud or financial failure.

### Open Questions

Some questions will only be answered after exploratory analysis, including:

- Which financial variables are reported consistently enough across companies for comparison?
- How much textual information should be included in the first version of the analysis?
- Which industries should be compared separately?
- Which anomaly detection method is most suitable for this type of data?
- How much of the historical dataset can be processed efficiently with the computing resources available to the team?


## 7. Research Approach, Tasks and Timeline

The project will be completed over roughly twelve weeks. The first few weeks focus on understanding the data and building the processing pipeline. Later weeks move toward scalable analytics and machine learning.

### Week 1

- Select the research problem
- Identify the SEC dataset
- Verify that the dataset can be accessed
- Inspect the January 2026 sample
- Understand the eight tables
- Define the initial research questions
- Create the GitHub repository
- Complete the Phase 1 research plan

### Week 2

- Study the SEC technical documentation in more detail
- Build scripts for downloading selected SEC archives
- Load SUB, NUM, TXT and TAG data
- Test joins between the main tables
- Create representative data samples
- Begin basic data-quality checks

### Week 3

- Process a larger period of SEC filings
- Identify commonly reported financial concepts
- Handle missing values and repeated reporting contexts
- Begin exploratory analysis of important financial measures
- Compare reporting patterns across companies

### Week 4

- Expand analysis across multiple industries and time periods
- Create financial ratios and change-based features
- Analyze distributions and outliers
- Prepare the first scalable analytics results
- Prepare material for the Phase 2 presentation

### Phase 2 Presentation - October 14-16

Present the cleaned data, exploratory analysis and first scalable analytics results.

### Weeks 5-6

- Move the larger processing workflow to PySpark
- Convert useful intermediate data to Parquet
- Test distributed joins and aggregations
- Compare processing performance with the earlier local workflow

### Weeks 7-8

- Develop financial change and anomaly features
- Test statistical and machine learning anomaly detection approaches
- Investigate unusual company or filing patterns

### Weeks 9-10

- Introduce selected textual disclosure features if practical
- Compare numerical and textual reporting changes
- Refine the anomaly detection approach
- Evaluate results across industries and time periods

### Week 11

- Finalize analysis
- Validate selected results
- Produce final visualizations
- Document limitations and findings

### Week 12

- Clean and package the code
- Finalize the GitHub repository
- Complete the final report and presentation
- Prepare the final project demonstration

### Final Presentation

The final project presentation is planned for the week of December 7.


## 8. Design Decisions

### Choosing the Financial Statement and Notes Dataset

We originally considered the smaller SEC Financial Statement Data Sets, which mainly contain numerical information from the primary financial statements.

We decided to use the Financial Statement and Notes Data Sets instead because they contain both detailed numerical information and textual disclosures. This gives the project more flexibility for later analysis while still keeping the same reliable SEC source.

### Working With the Data in Batches

The complete historical dataset will not be permanently stored on a local machine. Monthly and quarterly archives will be processed as needed.

This approach reduces local storage requirements and also reflects how a larger real-world dataset would normally be processed.

### Starting With the Core Tables

Although the dataset contains eight tables, the first stage will mainly focus on SUB, NUM, TXT and TAG.

These tables provide the company and filing information, numerical values, textual disclosures and definitions required for most of the initial analysis.

The other tables will be introduced when they are needed.

### Keeping the Research Question Broad During Phase 1

At this stage, we have intentionally not committed to one specific machine learning algorithm.

The first priority is to understand the data and determine what types of anomalies and financial changes can be measured reliably.

The final modeling approach will be selected after the exploratory analysis rather than choosing a model before understanding the data.


## 9. Phase 1 Data Samples

Representative samples from the January 2026 SEC Financial Statement and Notes package will be stored in:

`data/samples/`

The samples will contain a small number of records from the main tables so that the structure of the original data can be inspected without storing large SEC archives in the GitHub repository.

The full raw data will not be committed to GitHub. Instructions and scripts for accessing the original SEC data will instead be provided in the repository.