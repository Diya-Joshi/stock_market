import pandas as pd

data1 = pd.read_csv("D:\\stock_market analysis\\EQUITY_L.csv")
data2 = pd.read_csv("D:\\stock_market analysis\\ind_nifty100list.csv")
merge_data = pd.merge(data1, data2, on=["Symbol", "ISIN Code", "Series"])
final_data = merge_data[['Symbol', 'Company Name', 'Series', 'Date of listing', 'ISIN Code', 'Industry', 'Face value']]
sorted_data = final_data.sort_values('Face value')
sorted_top_75 = sorted_data.head(75)

def all_data():
    print(sorted_data)

def top_75():
    print(sorted_top_75)

def search():
    symbol_name = input("Enter the symbol of the company: ")
    searched_data = final_data[final_data['Symbol'] == symbol_name]
    print(searched_data)

flag = True
while flag == True:
    print('''
       ****** MENU *******
    Select from the following:- 
    
    1) Display all data, Press 1 
    2) Display Top 75, Press 2
    3) Search, Press 3
    4) Exit, Press 4''')

    choice = int(input("\nEnter your choice:- "))

    if choice == 1:
        all_data()

    elif choice == 2:
        top_75()

    elif choice == 3:
        search()

    elif choice == 4:
        print("Exiting, Thank you!")
        flag = False
    else:
        print("\nInvalid input")
