# Sports Betting Impact Study

## Project Overview

This project aims to analyze the impact of sports betting on various metrics such as gaming revenue, crime data, and problem gambling spending across different states in the United States. The data spans multiple years and includes detailed information on monthly and quarterly revenues, crime rates, and other relevant statistics.


## Data Sources

### Processed Data

- **AllGamingRevenuebyStatebyQuarter**
  - [AllGamingRevenuebyStatebyQuarter-tidy-all.csv](dataProcessing/processed/AllGamingRevenuebyStatebyQuarter/AllGamingRevenuebyStatebyQuarter-tidy-all.csv)
  - [AllGamingRevenuebyStatebyQuarter-tidy-quarterly.csv](dataProcessing/processed/AllGamingRevenuebyStatebyQuarter/AllGamingRevenuebyStatebyQuarter-tidy-quarterly.csv)
  - [AllGamingRevenuebyStatebyQuarter-tidy-yearly.csv](dataProcessing/processed/AllGamingRevenuebyStatebyQuarter/AllGamingRevenuebyStatebyQuarter-tidy-yearly.csv)
  - [CodeBook.md](dataProcessing/processed/AllGamingRevenuebyStatebyQuarter/CodeBook.md)

- **MonthlyRevenueForEachState2012to2024**
  - [MonthlyRevenueForEachState2012to2024-tidy-all.csv](dataProcessing/processed/MonthlyRevenueForEachState2012to2024/MonthlyRevenueForEachState2012to2024-tidy-all.csv)
  - [MonthlyRevenueForEachState2012to2024-tidy-monthly.csv](dataProcessing/processed/MonthlyRevenueForEachState2012to2024/MonthlyRevenueForEachState2012to2024-tidy-monthly.csv)
  - [MonthlyRevenueForEachState2012to2024-tidy-yearly.csv](dataProcessing/processed/MonthlyRevenueForEachState2012to2024/MonthlyRevenueForEachState2012to2024-tidy-yearly.csv)
  - [CodeBook.md](dataProcessing/processed/MonthlyRevenueForEachState2012to2024/CodeBook.md)

- **OnlineSportsBettingRevenueByState**
  - [OnlineSportsBettingRevenueByState-tidy-historicalTotal.csv](dataProcessing/processed/OnlineSportsBettingRevenueByState/OnlineSportsBettingRevenueByState-tidy-historicalTotal.csv)
  - [OnlineSportsBettingRevenueByState-tidy-monthly.csv](dataProcessing/processed/OnlineSportsBettingRevenueByState/OnlineSportsBettingRevenueByState-tidy-monthly.csv)
  - [CodeBook.md](dataProcessing/processed/OnlineSportsBettingRevenueByState/CodeBook.md)

- **CrimeData**
  - [StatePopulation-tidy-yearly.csv](dataProcessing/processed/PopulationbyStatebyYear/StatePopulation-tidy-yearly.csv)
  - [2012to2022_CrimeData-tidy-yearly.csv](dataProcessing/processed/CrimeDataYearly/2012to2022_CrimeData-tidy-yearly.csv)

## Scripts

### Data Processing

- **AllGamingRevenuebyStatebyQuartersince2020Q3-Untidy.py**
  - Processes untidy gaming revenue data and saves it into tidy formats.
  - [Script](dataProcessing/processing-AllGamingRevenuebyStatebyQuartersince2020Q3-Untidy.py)

- **MonthlyRevenueForEachState2012to2024.py**
  - Processes monthly revenue data for each state from 2012 to 2024.
  - [Script](dataProcessing/processing-MonthlyRevenueForEachState2012to2024.py)

- **OnlineSportsBettingRevenueByState.py**
  - Processes online sports betting revenue data by state.
  - [Script](dataProcessing/processing-OnlineSportsBettingRevenueByState.py)

- **CrimeData.py**
  - Processes crime data and merges it with population data.
  - [Script](dataProcessing/processing2-CrimeData.py)

### Preview

- **preview1-CrimeData.py**
  - Loads and previews crime data.
  - [Script](dataProcessing/preview1-CrimeData.py)

## Final Report

- **FinalReport-final.ipynb**
  - Jupyter notebook containing the final analysis and visualizations.
  - [Notebook](FinalReport-final.ipynb)

## How to Run

1. **Install Dependencies**
   - Ensure you have Python and the necessary libraries installed. You can install the required libraries using:
     ```sh
     pip install pandas
     ```

2. **Run Data Processing Scripts**
   - Execute the data processing scripts to generate the processed data files.
     ```sh
     python dataProcessing/processing-AllGamingRevenuebyStatebyQuartersince2020Q3-Untidy.py
     python dataProcessing/processing-MonthlyRevenueForEachState2012to2024.py
     python dataProcessing/processing-OnlineSportsBettingRevenueByState.py
     python dataProcessing/processing2-CrimeData.py
     ```

3. **Generate Final Report**
   - Open and run the Jupyter notebook to generate the final report.
     ```sh
     jupyter notebook FinalReport-final.ipynb
     ```
