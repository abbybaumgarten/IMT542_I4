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
