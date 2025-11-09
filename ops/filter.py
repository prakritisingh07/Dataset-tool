import pandas as pd

def filter_df(df):
    print("\n--- FILTER ---")
    print("Columns:")
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")
    
    choice = input("Column: ")
    
    if choice.isdigit():
        idx = int(choice) - 1
        if idx < 0 or idx >= len(df.columns):
            print("Invalid")
            return df
        col = df.columns[idx]
    else:
        if choice not in df.columns:
            print("Not found")
            return df
        col = choice
    
    if pd.api.types.is_numeric_dtype(df[col]):
        print("\n1. Greater than")
        print("2. Less than")
        print("3. Equal to")
        print("4. Between")
        
        c = input("Choose: ")
        
        if c == '1':
            v = float(input("Value: "))
            result = df[df[col] > v]
        elif c == '2':
            v = float(input("Value: "))
            result = df[df[col] < v]
        elif c == '3':
            v = float(input("Value: "))
            result = df[df[col] == v]
        elif c == '4':
            min_v = float(input("Min: "))
            max_v = float(input("Max: "))
            result = df[(df[col] >= min_v) & (df[col] <= max_v)]
        else:
            print("Invalid")
            return df
    else:
        print("\n1. Contains")
        print("2. Equals")
        print("3. Starts with")
        print("4. Ends with")
        
        c = input("Choose: ")
        v = input("Value: ")
        
        if c == '1':
            result = df[df[col].astype(str).str.contains(v, na=False)]
        elif c == '2':
            result = df[df[col] == v]
        elif c == '3':
            result = df[df[col].astype(str).str.startswith(v, na=False)]
        elif c == '4':
            result = df[df[col].astype(str).str.endswith(v, na=False)]
        else:
            print("Invalid")
            return df
    
    print(f"Filtered! Shape: {result.shape}")
    print(result.head())
    return result
