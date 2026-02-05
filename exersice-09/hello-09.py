 display_menu(items):def
    print("\n--- Vending Machine Menu ---")
    for code, item in items.items():
        print(f"{code}: {item['name']} (£{item['price']}) - Stock: {item['stock']}")

def get_item(code, items):
    return items.get(code.upper(), None)

def suggest_item(code):
    if code == "D1":
        print("Suggestion: Would you like to buy biscuits with your coffee?")
    elif code == "S1":
        print("Suggestion: A cold drink goes well with chocolate!")

def vending_machine():
    items = {
        "D1": {"name": "Coffee", "price": 1.50, "stock": 5, "category": "Drink"},
        "D2": {"name": "Tea", "price": 1.20, "stock": 5, "category": "Drink"},
        "S1": {"name": "Chocolate Bar", "price": 1.00, "stock": 5, "category": "Snack"},
        "S2": {"name": "Crisps", "price": 0.80, "stock": 5, "category": "Snack"}
    }

    total_cost = 0.0
    shopping = True

    while shopping:
        display_menu(items)
        code = input("\nEnter item code (or X to finish): ").upper()

        if code == "X":
            break

        item = get_item(code, items)

        if item and item["stock"] > 0:
            total_cost += item["price"]
            item["stock"] -= 1
            print(f"{item['name']} added. Price: £{item['price']}")
            suggest_item(code)
        else:
            print("Invalid code or item out of stock.")

    if total_cost > 0:
        print(f"\nTotal cost: £{total_cost}")
        money = float(input("Insert money: £"))

        if money >= total_cost:
            change = round(money - total_cost, 2)
            print("Items dispensed successfully.")
            print(f"Change returned: £{change}")
        else:
            print("Insufficient money. Transaction cancelled.")
    else:
        print("No items selected.")

vending_machine()


