def stats_df(df):
    print("\n" + "="*40)
    print("STATS")
    print("="*40)
    
    nums = df.select_dtypes(include=['number']).columns
    if len(nums) > 0:
        print("\nNumeric Stats:")
        print(df[nums].describe())
    
    cats = df.select_dtypes(include=['object']).columns
    if len(cats) > 0:
        print("\nCategorical:")
        for col in cats:
            print(f"\n{col}:")
            print(f"Unique: {df[col].nunique()}")
            print("Top 5:")
            print(df[col].value_counts().head())
    
    if len(nums) > 1:
        print("\nCorrelation:")
        print(df[nums].corr())
