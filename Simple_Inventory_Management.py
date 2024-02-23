# Inventory Project

date = input("What is the date? ")
company_name = input("What is the company name? ")

print(f"Inventory for {company_name} on {date}:")

# Master Inventory List
inventory = []

# Function to add an item to the inventory
def add_item():
    try:
        name = input("Item Name: ")
        quantity = int(input("Quantity: "))
        description = input("Description: ")
        new_item = {"name": name, "quantity": quantity, "description": description}
        inventory.append(new_item)
    except ValueError:
        print("Invalid input. Quantity must be a number.")

# Function to display the inventory
def display_inventory():
    print("Inventory:")
    for index, item in enumerate(inventory):
        print("-------------------")
        print(f"Item number: {index}")
        print(f"Item Name: {item['name']}")
        print(f"Item Quantity: {item['quantity']}")
        print(f"Description: {item['description']}")
        print("-------------------")

# Function to update the quantity of an item
def update_quantity():
    try:
        index = int(input('Enter the item number: '))
        item = inventory[index]
        new_quantity = int(input('Enter the new quantity: '))
        item['quantity'] = new_quantity
        print(f"Quantity updated for {item['name']}.") 
    except (IndexError, ValueError):
        print("Invalid input or item not found.")

# Function to remove an item from the inventory
def remove_item():
    try:
        index = int(input('Enter the item number to remove: '))
        inventory.pop(index)
        print("Item removed successfully.")
    except (IndexError, ValueError):
        print("Invalid input or item not found.")

add_item()
add_item()
display_inventory()
update_quantity()
remove_item()
display_inventory()
