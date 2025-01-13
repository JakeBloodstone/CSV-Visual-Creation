import matplotlib.pyplot as plt

def plot_revenue_by_store(data):
    """
    Plot a pie chart showing revenue contribution by each store location.
    """
    try:
        revenue_by_store = {}
        for row in data:
            location = row.get("StoreLocation")
            revenue = float(row.get("TotalPrice", 0))
            revenue_by_store[location] = revenue_by_store.get(location, 0) + revenue

        labels = list(revenue_by_store.keys())
        values = list(revenue_by_store.values())

        plt.figure(figsize=(8, 8))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        plt.title("Revenue Contribution by Store Location")
        plt.axis('equal')
        plt.show()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def plot_transaction_histogram(data):
    """
    Plot a histogram of transactional values.
    """
    try:
        transaction_values = [float(row.get("TotalPrice", 0)) for row in data]
        plt.figure(figsize=(10, 6))
        plt.hist(transaction_values, bins=20, color='skyblue', edgecolor='black')
        plt.title("Distribution of Transactional Values")
        plt.xlabel("Transaction Value (£)")
        plt.ylabel("Frequency")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")