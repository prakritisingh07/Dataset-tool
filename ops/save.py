import os

def save_df(df):
    print("\n--- SAVE ---")
    name = input("Filename: ")
    
    if not name:
        print("Invalid name")
        return
    
    out = f"{name}.csv"
    df.to_csv(out, index=False)
    print(f"Saved to {out}")
    print(f"Location: {os.path.abspath(out)}")
