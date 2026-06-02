
# Pharmacy Management System

drug_inventory = {}


# Adding Drugs__


def add_drug():
    name = input("Enter drug name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    drug_inventory[name] = {'price': price, 'quantity': quantity}
    print("Drug added successfully!")


# Updating Drug Information__

def update_drug():
    name = input("Enter drug name: ")
    if name in drug_inventory:
        price = float(input("Enter new price: "))
        quantity = int(input("Enter new quantity: "))
        drug_inventory[name]['price'] = price
        drug_inventory[name]['quantity'] = quantity
        print("Drug information updated successfully!")
    else:
        print("Drug not found in the inventory!")


# Viewing Drug Information___


def view_drug():
    name = input("Enter drug name (leave blank to view all drugs): ")
    if name:
        if name in drug_inventory:
            drug = drug_inventory[name]
            print(f"Drug Name: {name}")
            print(f"Price: {drug['price']}")
            print(f"Quantity: {drug['quantity']}")
        else:
            print("Drug not found in the inventory!")
    else:
        if not drug_inventory:
            print("No drugs in the inventory!")
        else:
            for name, drug in drug_inventory.items():
                print(f"Drug Name: {name}")
                print(f"Price: {drug['price']}")
                print(f"Quantity: {drug['quantity']}")



# Recording Purchases__


def record_purchase():
    name = input("Enter drug name: ")
    if name in drug_inventory:
        quantity = int(input("Enter quantity purchased: "))
        if quantity <= drug_inventory[name]['quantity']:
            drug_inventory[name]['quantity'] -= quantity
            print("Purchase recorded successfully!")
        else:
            print("Insufficient quantity in the inventory!")
    else:
        print("Drug not found in the inventory!")



# Menu System___


def menu():
    while True:
        print("\nPharmacy Management System")
        print("1. Add Drug")
        print("2. Update Drug Information")
        print("3. View Drug Information")
        print("4. Record Purchase")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_drug()
        elif choice == '2':
            update_drug()
        elif choice == '3':
            view_drug()
        elif choice == '4':
            record_purchase()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again!")

menu()


