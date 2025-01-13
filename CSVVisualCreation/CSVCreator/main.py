import csv
import process
import visualize
import export

# Global variable to store the data
data = None

def load_data():
    """
    Load sales data from a CSV file in the same directory as the script.

    Returns:
        list[dict]: The loaded data as a list of dictionaries.
    """
    try:
        file_name = 'retail_sales_data.csv'
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        print("Data successfully loaded into memory.")
        print(f"Total records loaded: {len(data)}")
        return data

    except FileNotFoundError:
        print("Error: The file 'retail_sales_data.csv' was not found in the current directory.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def load_data_option():
    """
    Option 1: Load data from 'retail_sales_data.csv' in the same directory.
    """
    global data
    data = load_data()
    if data is not None:
        print("Data is now loaded into memory.")

def process_data():
    if data is None:
        print("No data loaded. Please load the data first.")
        return

    while True:
        print("\nProcess Data")
        print("====================")
        print("1. Retrieve Total Transactions")
        print("2. Retrieve Unique Store Locations")
        print("3. Retrieve Transaction by TransactionID")
        print("4. Retrieve Transactions by Store Location")
        print("5. Group by Store and Calculate Revenue")
        print("6. Summary by Store Location")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            process.retrieve_total_transactions(data)
        elif choice == "2":
            process.retrieve_unique_stores(data, "StoreLocation")
        elif choice == "3":
            transaction_id = input("Enter TransactionID: ")
            process.retrieve_transaction_by_id(data, transaction_id)
        elif choice == "4":
            store_location = input("Enter Store Location: ")
            process.retrieve_transactions_by_filter(data, "StoreLocation", store_location)
        elif choice == "5":
            process.group_by_store_and_calculate_revenue(data)
        elif choice == "6":
            store_location = input("Enter Store Location: ")
            process.summary_by_store(data, store_location)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

def visualize_data():
    if data is None:
        print("No data loaded. Please load the data first.")
        return

    while True:
        print("\nVisualize Data")
        print("====================")
        print("1. Pie Chart: Revenue by Store Location")
        print("2. Histogram: Transactional Values")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            visualize.plot_revenue_by_store(data)
        elif choice == "2":
            visualize.plot_transaction_histogram(data)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def export_data():
    """
    Sub-menu for exporting data.
    """
    while True:
        print("\nExport Data")
        print("====================")
        print("1. Export Revenue by Store to JSON")
        print("2. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            if not data:
                print("No data loaded. Please load the data first.")
                continue
            export.export_revenue_as_json(data)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    print("\nE-Commerce Dashboard")
    print("====================")
    print("1. Load Data")
    print("2. Process Data")
    print("3. Visualize Data")
    print("4. Export Data")
    print("5. Exit")
    return input("Enter your choice: ")

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            load_data_option()
        elif choice == "2":
            process_data()
        elif choice == "3":
            visualize_data()
        elif choice == "4":
            export_data()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
