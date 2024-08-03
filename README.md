## README for Tech Adoption Trends Analysis

This Python script analyzes tech adoption trends using CSV files for various technologies. It reads the data, plots the trends, and forecasts future adoption rates.

### Prerequisites
Install the necessary packages:
sh
pip install statsmodels plotly


### Usage
1. *Run the Script*:
   sh
   python script_name.py
   

2. *Select a Technology*:
   - 1: Big Data
   - 2: Deep Learning
   - 3: Machine Learning
   - 4: Python
   - 5: SQL
   - 6: Quit

3. *Files*:
   - big_data_canada.csv
   - dl_canada.csv
   - ml_canada.csv
   - py_canada.csv
   - sql_canada.csv

### Functions
- option(choice): Returns the file name based on user choice.
- convert(file_path): Reads and validates the CSV file.
- trend(tech_data): Plots the adoption trend using Plotly.
- forecast(tech_data): Forecasts future adoption rates with ARIMA.
- main(): Orchestrates user interaction and calls other functions.

### For Tableau
1. Connect to CSV in Tableau.
2. Create a line chart with Year and Adoption Rate.
3. Add a forecast via the Analytics pane.
4. Customize and save the visualization.
