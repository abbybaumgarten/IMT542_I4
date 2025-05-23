import pandas as pd

# Pros:
# - Fast and easy to analyze
# - No internet required
# - CSV is a widely supported format

# Cons:
# - Requires manual download/setup
# - Not suited for dynamic or frequently updated data

try:
    df = pd.read_csv("U.S._Chronic_Disease_Indicators.csv")
    print("Sample CSV Data (from U.S. Chronic Disease Indicators):")
    print(df[['YearStart', 'LocationDesc', 'Topic', 'DataValue']].head())
except FileNotFoundError:
    print("CSV file not found. Make sure 'U.S._Chronic_Disease_Indicators.csv' is in the directory.")
    
Sample Data from CSV:
   YearStart LocationDesc     Topic  DataValue
0       2019     Arkansas  Diabetes       13.6
1       2019        Idaho  Diabetes       10.6
2       2019      Indiana     Sleep        NaN
3       2019         Iowa    Asthma       54.0
4       2019         Iowa    Asthma       10.3
