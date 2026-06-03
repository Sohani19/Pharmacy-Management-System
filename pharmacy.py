
# Pharmacy Management System

# DATABASE............

import sqlite3

conn=sqlite3.connect("pharmacy.db")
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS drugs(
               name TEXT PRIMARY KEY,
               price REAL,
               quantity INTEGER
)
""")

conn.commit()



# Adding Drugs__


def add_drug():
    name = input("Enter drug name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    cursor.execute(
        "INSERT OR REPLACE INTO drugs VALUES(?,?,?)",
        (name,price,quantity)
    )
    conn.commit()
    print("Drugs added successfully ")


# Updating Drug Information__

def update_drug():
    name = input("Enter drug name: ")
    cursor.execute("SELECT *FROM drugs WHERE name=?",(name,))
    drug=cursor.fetchone()

    if drug:
        price=float(input("Enter new price: "))
        quantity=int(input("Enter new quantity:"))

        cursor.execute(
            "UPDATE drugs SET price=?,quantity=?, WHERE name=?",
            (price,quantity,name)
        )
        conn.commit()
        print("Drug updated successfully ")
    else:
        print("Drug not found ")

# Delete the details of drug__

def delete_drug():
    name=input("Enter the drug name to delete ")
    cursor.execute("DELETE FROM drugs WHERE name=?",(name,))
    conn.commit()
    print("Drug deleted successfully ")

# Searching a drug__

def search_drug():
    name=input("Enter the drug name ")
    cursor.execute("SELECT *FROM drugs WHERE name=?",(name,))
    drug=cursor.fetchone()

    if drug:
        print(f"Name : {drug[0]}")
        print(f"Price: ₹{drug[1]}")
        print(f"Quantity: {drug[2]}")

    else:
        print("Drug not found")   

# Viewing Drug Information___


def view_inventory():
   cursor.execute("SELECT *FROM drugs")
   drugs=cursor.fetchall()
   
   if not drugs:
       print("Inventory is empty...")
       return 
   
   print("\n ---INVENTORY---")
   for drug in drugs:
       print(f"Name: {drug[0]} | Price ₹{drug[1]} | Quantity: {drug[2]}")



# Recording Purchases__


def record_purchase():
    name = input("Enter drug name: ")
    quantity=int(input("Enter quantity purchased: "))

    cursor.execute("SELECT *FROM drugs  WHERE name=?",(name,))
    drug=cursor.fetchone()

    if not drug:
        print("Drug not found ")
        return
    
    if quantity>drug[2]:
        print("Insufficient stock ")
        return
    
    total=quantity * drug[1]

    cursor.execute(
        "UPDATE drugs SET quantity=? WHERE name=?",
        (drug[2] - quantity)
    )
    conn.commit()

    print("\n ---BILL---")
    print("Medicine => ",name)
    print("Quantity => ",quantity)
    print("Unit Price => ₹",drug[1])
    print("Total Bill =>total")


# Low Stock Alert....

def low_stock_alert():
    cursor.execute("SELECT *FROM drugs WHERE quantity < 10")
    drugs=cursor.fetchall()

    print("\n--- Low Stock Medicines---")
    if not drugs:
        print("NO Low Stock Medicines ")

    for drug in drugs:
        print(f"{drug[0]} => Remaining {drug[2]}")



# Menu System___


def menu():
    while True:
        print("\nPharmacy Management System")
        print("1. Add Drug")
        print("2. Update Drug Information")
        print("3. View Inventory ")
        print("4. Record Purchase")
        print("4. Record Purchase")
        print("5. Search Drug")
        print("6. Delete Drug")
        print("7. Low Stock Alert")
        print("8. Exit")
        

        choice = input("Enter your choice: ")

        if choice == '1':
            add_drug()
        elif choice == '2':
            update_drug()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            record_purchase()
        elif choice == '5':
            search_drug()
        elif choice =='6':
            delete_drug()
        elif choice =='7':
            low_stock_alert()
        elif choice =='8':
            print("See you soon")
            conn.close()
            break
        else:
            print("Invalid Choice ")

menu()


