import pandas as pd
import os

def get_data(path):
    path = path.strip().strip('"').strip("'")
    path = os.path.normpath(path)
    
    if not os.path.exists(path):
        print(f"File not found")
        return None
    
    if not path.endswith('.csv'):
        print("Only CSV files supported")
        return None
    
    try:
        df = pd.read_csv(path)
        print("CSV loaded successfully")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

def show_info(df):
    print("\n" + "-"*40)
    print("INFO")
    print("-"*40)
    print(f"Rows: {df.shape[0]}, Cols: {df.shape[1]}")
    print("\nColumns:")
    print(df.dtypes)
    print("\nMissing:")
    print(df.isnull().sum())
    print("\nFirst 5:")
    print(df.head())
