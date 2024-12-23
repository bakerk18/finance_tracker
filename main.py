from datetime import datetime
import csv

def add_transaction(type, amount, description):
    date = datetime.now().strftime("%Y-%m-%d")
    with open('transactions.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, type, amount, description])

def main():
    print("Personal Finance Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Exit")

if __name__ == "__main__":
    main()