from datetime import datetime
import csv

def add_transaction(type, amount, description):
    date = datetime.now().strftime("%Y-%m-%d")
    with open('transactions.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, type, amount, description])

def view_transactions():
    try:
        with open('transactions.csv', 'r') as file:
            reader = csv.reader(file)
            print("\nDate       | Type    | Amount  | Description")
            print("-" * 50)
            for row in reader:
                print(f"{row[0]} | {row[1]:<7} | ${row[2]:<6} | {row[3]}")
    except FileNotFoundError:
        print("\nNo transactions found.")

def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == "1":
            amount = input("Enter income amount: $")
            description = input("Enter description: ")
            add_transaction("Income", amount, description)
            print("Income added successfully!")
            
        elif choice == "2":
            amount = input("Enter expense amount: $")
            description = input("Enter description: ")
            add_transaction("Expense", amount, description)
            print("Expense added successfully!")
            
        elif choice == "3":
            view_transactions()
            
        elif choice == "4":
            print("Thank you for using Finance Tracker!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()