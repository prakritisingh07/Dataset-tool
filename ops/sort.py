def sort_df(df):
    print("\n--- SORT ---")
    print("Columns:")
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")
    
    choice = input("Column name or number: ")
    
    if choice.isdigit():
        idx = int(choice) - 1
        if idx < 0 or idx >= len(df.columns):
            print("Invalid number")
            return df
        col = df.columns[idx]
    else:
        if choice not in df.columns:
            print("Column not found")
            return df
        col = choice
    
    order = input("Order (a/d): ")
    asc = True if order != 'd' else False
    
    result = df.sort_values(by=col, ascending=asc)
    print(f"Sorted by {col}")
    print(result.head())
    return result
