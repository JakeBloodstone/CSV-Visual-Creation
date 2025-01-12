def retrieve_total_transactions(data):
    """
    Retrieve the total number of transactions.
    """
    total = len(data)
    print(f"Total Transactions: {total}")

def retrieve_unique_values(data, column_name):
    """
    Retrieve unique values from a specified column.
    """
    unique_values = set(row[column_name] for row in data if column_name in row)
    print(f"Unique {column_name}: {unique_values}")

def retrieve_transaction_by_id(data, transaction_id):
    """
    Retrieve details of a specific transaction using TransactionID.
    """
    transaction = [row for row in data if row.get("TransactionID") == transaction_id]
    if transaction:
        print(transaction[0])
    else:
        print(f"No transaction found with TransactionID: {transaction_id}")

def retrieve_transactions_by_filter(data, column_name, value):
    """
    Retrieve all transactions filtered by a specific column and value.
    """
    filtered_data = [row for row in data if row.get(column_name) == value]
    if filtered_data:
        for row in filtered_data:
            print(row)
    else:
        print(f"No transactions found for {column_name}: {value}")

def group_by_store_and_calculate_revenue(data):
    """
    Group transactions by store location and calculate the total revenue per location.
    """
    revenue_by_location = {}
    for row in data:
        location = row.get("StoreLocation")
        revenue = float(row.get("TotalPrice", 0))
        revenue_by_location[location] = revenue_by_location.get(location, 0) + revenue

    print("Total Revenue by Store Location:")
    for location, revenue in revenue_by_location.items():
        print(f"{location}: {revenue:.2f}")

def summary_by_store(data, store_location):
    """
    Provide a summary of sales for a specific store location.
    """
    store_data = [row for row in data if row.get("StoreLocation") == store_location]
    if store_data:
        total_transactions = len(store_data)
        total_revenue = sum(float(row.get("TotalPrice", 0)) for row in store_data)
        avg_transaction_value = total_revenue / total_transactions
        total_quantity = sum(int(row.get("Quantity", 0)) for row in store_data)
        avg_customer_satisfaction = sum(float(row.get("CustomerSatisfaction", 0)) for row in store_data) / total_transactions
        payment_methods = {}
        for row in store_data:
            method = row.get("PaymentMethod")
            payment_methods[method] = payment_methods.get(method, 0) + 1

        print(f"Summary for {store_location}:")
        print(f"  Total Transactions: {total_transactions}")
        print(f"  Total Revenue: {total_revenue:.2f}")
        print(f"  Average Transaction Value: {avg_transaction_value:.2f}")
        print(f"  Total Quantity Sold: {total_quantity}")
        print(f"  Average Customer Satisfaction: {avg_customer_satisfaction:.2f}")
        print("  Payment Method Distribution:")
        for method, count in payment_methods.items():
            percentage = (count / total_transactions) * 100
            print(f"    {method}: {percentage:.2f}%")
    else:
        print(f"No transactions found for store location: {store_location}")
