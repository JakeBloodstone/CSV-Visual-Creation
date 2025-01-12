from tkinter import Tk, filedialog
import json

def export_revenue_as_json(data):
    """
    Calculate revenue by store and export it as a JSON file using a save dialog.

    Args:
        data (list of dict): The sales data loaded from the CSV.
    """
    try:
        # Step 1: Calculate revenue by store
        revenue_by_store = {}
        for row in data:
            store = row["StoreLocation"]
            revenue = float(row["TotalPrice"])
            revenue_by_store[store] = revenue_by_store.get(store, 0) + revenue

        # Step 2: Prepare data for JSON export
        revenue_list = [{"StoreLocation": store, "Revenue": revenue}
                        for store, revenue in revenue_by_store.items()]

        # Step 3: Use file dialog to choose save location
        root = Tk()
        root.withdraw()  # Hide the main Tkinter window
        root.attributes("-topmost", True)  # Bring dialog to the front
        output_file = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            title="Save Revenue Data"
        )

        if not output_file:
            print("Export canceled.")
            return

        # Step 4: Write to JSON file
        with open(output_file, mode="w") as file:
            json.dump(revenue_list, file, indent=4)

        print(f"Revenue data successfully exported to {output_file}.")
    except KeyError as e:
        print(f"Error: Missing expected column in the data - {e}.")
    except Exception as e:
        print(f"An error occurred: {e}")
