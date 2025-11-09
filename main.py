import sys
import pandas as pd
from load import get_data, show_info
from ops.sort import sort_df
from ops.clean import clean_df
from ops.filter import filter_df
from ops.stats import stats_df
from ops.save import save_df

def menu():
    print("\n" + "="*40)
    print("DATA TOOL")
    print("="*40)
    print("1. Sort")
    print("2. Clean")
    print("3. Filter")
    print("4. Stats")
    print("5. Remove Duplicates")
    print("6. Save")
    print("7. View Info")
    print("8. Exit")
    print("="*40)

path = input("Enter CSV file path: ")
data = get_data(path)

if data is None:
    print("Error loading file")
    sys.exit()

print(f"Loaded! Rows: {data.shape[0]}, Cols: {data.shape[1]}")
show_info(data)

while True:
    menu()
    choice = input("Choose (1-8): ")
    
    if choice == '1':
        data = sort_df(data)
    elif choice == '2':
        data = clean_df(data)
    elif choice == '3':
        data = filter_df(data)
    elif choice == '4':
        stats_df(data)
    elif choice == '5':
        old = data.shape[0]
        data = data.drop_duplicates()
        print(f"Removed {old - data.shape[0]} duplicates")
    elif choice == '6':
        save_df(data)
    elif choice == '7':
        show_info(data)
    elif choice == '8':
        print("Bye!")
        break
    else:
        print("Invalid choice")
