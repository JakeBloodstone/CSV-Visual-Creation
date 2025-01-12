import pandas as pd
import matplotlib.pyplot as plt

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


def retrieve_total_transactions(data):
    """
    Retrieve the total number of transactions.
    """
    total = len(data)
    print(f"Total Transactions: {total}")

def retrieve_unique_values(data, column_name):
    """
    Retrieve unique values from a specified column.
    Args:
        data (pd.DataFrame): The DataFrame containing the data.
        column_name (str): The column to retrieve unique values from.
    """
    if column_name in data.columns:
        unique_values = data[column_name].unique()
        print(f"Unique {column_name}: {unique_values}")
    else:
        print(f"Error: Column '{column_name}' does not exist.")

def retrieve_transaction_by_id(data, transaction_id):
    """
    Retrieve details of a specific transaction using TransactionID.
    """
    transaction = data[data["TransactionID"] == transaction_id]
    if not transaction.empty:
        print(transaction)
    else:
        print(f"No transaction found with TransactionID: {transaction_id}")

def retrieve_transactions_by_filter(data, column_name, value):
    """
    Retrieve all transactions filtered by a specific column and value.
    Args:
        data (pd.DataFrame): The DataFrame containing the data.
        column_name (str): The column to filter by.
        value: The value to match.
    """
    if column_name in data.columns:
        filtered_data = data[data[column_name] == value]
        print(filtered_data)
    else:
        print(f"Error: Column '{column_name}' does not exist.")

def group_by_store_and_calculate_revenue(data):
    """
    Group transactions by store location and calculate the total revenue per location.
    """
    revenue_by_location = data.groupby("StoreLocation")["TotalPrice"].sum()
    print("Total Revenue by Store Location:")
    print(revenue_by_location)

def summary_by_store(data, store_location):
    """
    Provide a summary of sales for a specific store location.
    """
    store_data = data[data["StoreLocation"] == store_location]
    if not store_data.empty:
        total_transactions = len(store_data)
        total_revenue = store_data["TotalPrice"].sum()
        avg_transaction_value = store_data["TotalPrice"].mean()
        total_quantity = store_data["Quantity"].sum()
        avg_customer_satisfaction = store_data["CustomerSatisfaction"].mean()
        payment_method_percentage = (
            store_data["PaymentMethod"].value_counts(normalize=True) * 100
        )

        print(f"Summary for {store_location}:")
        print(f"  Total Transactions: {total_transactions}")
        print(f"  Total Revenue: {total_revenue:.2f}")
        print(f"  Average Transaction Value: {avg_transaction_value:.2f}")
        print(f"  Total Quantity Sold: {total_quantity}")
        print(f"  Average Customer Satisfaction: {avg_customer_satisfaction:.2f}")
        print("  Payment Method Distribution (%):")
        print(payment_method_percentage)
    else:
        print(f"No transactions found for store location: {store_location}")

def process_data():
    """
    Main function to process the data with a menu-driven interface.
    """
    if data is None:
        print("No data loaded. Please load the data first.")
        return

    while True:
        print("\nProcess Data")
        print("====================")
        print("1. Retrieve Total Transactions")
        print("2. Retrieve Unique Store Locations")
        print("3. Retrieve Unique Product Categories")
        print("4. Retrieve Transaction by TransactionID")
        print("5. Retrieve Transactions by Store Location")
        print("6. Retrieve Transactions by Product Category")
        print("7. Group by Store and Calculate Revenue")
        print("8. Summary by Store Location")
        print("9. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            retrieve_total_transactions(data)
        elif choice == "2":
            retrieve_unique_values(data, "StoreLocation")
        elif choice == "3":
            retrieve_unique_values(data, "ProductCategory")
        elif choice == "4":
            transaction_id = int(input("Enter TransactionID: "))
            retrieve_transaction_by_id(data, transaction_id)
        elif choice == "5":
            store_location = input("Enter Store Location: ")
            retrieve_transactions_by_filter(data, "StoreLocation", store_location)
        elif choice == "6":
            product_category = input("Enter Product Category: ")
            retrieve_transactions_by_filter(data, "ProductCategory", product_category)
        elif choice == "7":
            group_by_store_and_calculate_revenue(data)
        elif choice == "8":
            store_location = input("Enter Store Location: ")
            summary_by_store(data, store_location)
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")


def visualize_data():
    """
    Option 3: Visualize Data.
    """
    def plot_revenue_by_store(data):
        """
        Plot a pie chart showing revenue contribution by each store location.

        Args:
            data (pd.DataFrame): The DataFrame containing sales data.
        """
        try:
            # Group data by StoreLocation and calculate total revenue
            revenue_by_store = data.groupby("StoreLocation")["TotalPrice"].sum()

            # Extract labels and values for the pie chart
            labels = revenue_by_store.index  # Store locations
            values = revenue_by_store.values  # Total revenue

            # Create the pie chart
            plt.figure(figsize=(8, 8))
            plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
            plt.title("Revenue Contribution by Store Location")
            plt.axis('equal')  # Ensure the pie chart is a circle
            plt.show()

        except KeyError:
            print("Error: The dataset must contain 'StoreLocation' and 'TotalPrice' columns.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Menu for visualizing data
    if data is None:
        print("No data loaded. Please load the data first.")
        return

    def plot_transaction_histogram(data):
        """
        Plot a histogram of transactional values.
        """
        try:
            transaction_values = data["TotalPrice"]
            plt.figure(figsize=(10, 6))
            plt.hist(transaction_values, bins=20, color='skyblue', edgecolor='black')
            plt.title("Distribution of Transactional Values")
            plt.xlabel("Transaction Value ($)")
            plt.ylabel("Frequency")
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.show()
        except KeyError:
            print("Error: The dataset must contain a 'TotalPrice' column.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def plot_transaction_histogram(data):
        """
        Plot a histogram of transactional values.
        """
        try:
            transaction_values = data["TotalPrice"]
            plt.figure(figsize=(10, 6))
            plt.hist(transaction_values, bins=20, color='skyblue', edgecolor='black')
            plt.title("Distribution of Transactional Values")
            plt.xlabel("Transaction Value ($)")
            plt.ylabel("Frequency")
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.show()
        except KeyError:
            print("Error: The dataset must contain a 'TotalPrice' column.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

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
            plot_revenue_by_store(data)
        elif choice == "2":
            plot_transaction_histogram(data)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

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