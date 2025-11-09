def clean_df(df):
    print("\n--- CLEAN ---")
    miss = df.isnull().sum()
    print("Missing values:")
    print(miss[miss > 0])
    
    if miss.sum() == 0:
        print("No missing values")
        return df
    
    print("\n1. Drop all NA rows")
    print("2. Drop NA in column")
    print("3. Fill NA with value")
    print("4. Fill NA with mean")
    print("5. Forward fill")
    
    choice = input("Choose: ")
    
    if choice == '1':
        result = df.dropna()
        print(f"Dropped {df.shape[0] - result.shape[0]} rows")
        return result
    elif choice == '2':
        col = input("Column: ")
        if col not in df.columns:
            print("Column not found")
            return df
        result = df.dropna(subset=[col])
        print(f"Dropped {df.shape[0] - result.shape[0]} rows")
        return result
    elif choice == '3':
        col = input("Column: ")
        if col not in df.columns:
            print("Column not found")
            return df
        val = input("Value: ")
        result = df.copy()
        result[col].fillna(val, inplace=True)
        print("Filled NA values")
        return result
    elif choice == '4':
        nums = df.select_dtypes(include=['number']).columns
        result = df.copy()
        for col in nums:
            if result[col].isnull().sum() > 0:
                m = result[col].mean()
                result[col].fillna(m, inplace=True)
                print(f"Filled {col} with {m:.2f}")
        return result
    elif choice == '5':
        result = df.fillna(method='ffill')
        print("Forward filled")
        return result
    else:
        print("Invalid")
        return df
