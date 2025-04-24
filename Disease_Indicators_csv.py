import pandas as pd

# Load the CSV (make sure it's uploaded in the left sidebar)
df = pd.read_csv("U.S._Chronic_Disease_Indicators.csv")

# Display a few sample rows
print("Sample Data from CSV:")
print(df[['YearStart', 'LocationDesc', 'Topic', 'DataValue']].head())

Sample Data from CSV:
   YearStart LocationDesc     Topic  DataValue
0       2019     Arkansas  Diabetes       13.6
1       2019        Idaho  Diabetes       10.6
2       2019      Indiana     Sleep        NaN
3       2019         Iowa    Asthma       54.0
4       2019         Iowa    Asthma       10.3 
