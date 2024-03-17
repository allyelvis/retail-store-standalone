import json
import requests

# Cloud Integration Platform URL
CLOUD_API_URL = "https://cloud-integration-platform.com/api"

# Sales System URL
SALES_SYSTEM_URL = "https://sales-system.com/api"

# Inventory Management System URL
INVENTORY_SYSTEM_URL = "https://inventory-system.com/api"

def main():
    # Get the order details from the sales system
    order_response = requests.get(SALES_SYSTEM_URL + "/orders/1")
    order_data = order_response.json()

    # Extract the ordered items and quantities
    ordered_items = order_data["items"]

    # Update the inventory levels in the inventory management system
    for item in ordered_items:
        item_id = item["item_id"]
        quantity = item["quantity"]

        inventory_update_data = {"item_id": item_id, "quantity": -quantity}
        inventory_response = requests.put(INVENTORY_SYSTEM_URL + "/inventory", json=inventory_update_data)

        # Check if inventory update was successful
        if inventory_response.status_code != 200:
            raise Exception("Failed to update inventory: " + inventory_response.text)

    # Send the stock movement data to the cloud integration platform
    stock_movement_data = []
    for item in ordered_items:
        item_id = item["item_id"]
        quantity = item["quantity"]

        stock_movement_data.append({"item_id": item_id, "quantity": -quantity})

    cloud_response = requests.post(CLOUD_API_URL + "/stock-movements", json=stock_movement_data)

    # Check if stock movement data was sent successfully
    if cloud_response.status_code != 201:
        raise Exception("Failed to send stock movement data: " + cloud_response.text)

    print("Sales and stock movement data integrated successfully to the cloud.")

if __name__ == "__main__":
    main()