# Inventory data structures
item_names = []
item_prices = {}

while True:
    print("\n--- Inventory Menu ---")
    print("1. Add New Item")
    print("2. Update Item Price")
    print("3. View Inventory")
    print("4. Exit")

    choice = input("Enter choice: ")

    # Add new item
    if choice == "1":
        name = input("Enter item name: ").strip()

        if name in item_names:
            print("Error: Item already exists.")
            continue

        try:
            price = float(input("Enter item price: "))
        except ValueError:
            print("Invalid price. Must be a number.")
            continue

        item_names.append(name)
        item_prices[name] = price
        print(f"Item '{name}' added.")

    # Update existing item
    elif choice == "2":
        name = input("Enter item name to update: ").strip()

        if name not in item_names:
            print("Error: Item not found.")
            continue

        try:
            new_price = float(input("Enter new price: "))
        except ValueError:
            print("Invalid price. Must be a number.")
            continue

        item_prices[name] = new_price
        print(f"Price of '{name}' updated.")

    # View all items
    elif choice == "3":
        print("\n--- Inventory List ---")
        if not item_names:
            print("No items found.")
        else:
            for item in item_names:
                print(f"{item}: ₱{item_prices[item]}")
    
    # Exit
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
