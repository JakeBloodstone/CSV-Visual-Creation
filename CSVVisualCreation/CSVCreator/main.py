import pandas as pd

# Global variable to store the data
data = None


def load_data():
    """
    Load sales data from a CSV file in the same directory as the script.

    Returns:
        pd.DataFrame: The loaded data as a Pandas DataFrame.
    """
    try:
        # File name only, since it's in the same directory
        file_name = 'retail_sales.csv'
        data = pd.read_csv(file_name)

        # Validate columns
        required_columns = [
            "TransactionID", "CustomerID", "StoreLocation", "ProductCategory",
            "ProductID", "Quantity", "UnitPrice", "TotalPrice",
            "TransactionDate", "PaymentMethod", "DiscountApplied", "CustomerSatisfaction"
        ]
        if not all(column in data.columns for column in required_columns):
            raise ValueError("The CSV file does not contain all required columns.")

        print("Data successfully loaded into memory.")
        print(f"Total records loaded: {len(data)}")
        return data

    except FileNotFoundError:
        print("Error: The file 'retail_sales.csv' was not found in the current directory.")
        return None
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def load_data_option():
    """
    Option 1: Load data from 'retail_sales.csv' in the same directory.
    """
    global data
    data = load_data()
    if data is not None:
        print("Data is now loaded into memory.")

def main_menu():
    print("\nE-Commerce Dashboard")
    print("====================")
    print("1. Load Data")
    print("2. Process Data")
    print("3. Visualize Data")
    print("4. Export Data")
    print("5. Exit")
    return input("Enter your choice: ")


def process_data():
    print("Option 2: Process Data (Placeholder)")


def visualize_data():
    print("Option 3: Visualize Data (Placeholder)")


def export_data():
    print("Option 4: Export Data (Placeholder)")


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