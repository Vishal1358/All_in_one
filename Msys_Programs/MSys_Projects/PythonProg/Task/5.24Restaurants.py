'''
24. Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders,
and methods like add_item_to_menu, book_tables, and customer_order. Perform the following tasks now:
- Now add items to the menu.
- Make table reservations.
- Take customer orders.
- Print the menu.
- Print table reservations.
- Print customer orders.
Note : Use dictionaries and lists to store the data.
'''

class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = []
        self.customer_orders = []

    def add_item_to_menu(self, item_name, price):
        self.menu_items[item_name] = price

    def book_table(self, table_number):
        self.booked_tables.append(table_number)

    def customer_order(self, table_number, order):
        self.customer_orders.append((table_number, order))

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: {price:.2f}")

    def print_booked_tables(self):
        print("Booked Tables:")
        for table in self.booked_tables:
            print(f"Table {table}")

    def print_customer_orders(self):
        print("Customer Orders:")
        for table, order in self.customer_orders:
            print(f"Table {table}: {order}")

restaurant = Restaurant()

restaurant.add_item_to_menu("Masala Dosa", 70)
restaurant.add_item_to_menu("Chapati" , 80)
restaurant.add_item_to_menu("Upma",35)

restaurant.book_table(1)
restaurant.book_table(2)
restaurant.book_table(4)

restaurant.customer_order(1, ["Masala Dosa", "Idly", "Puri"])
restaurant.customer_order(2, ["Chapati","Bhaji","Cool drinks"])
restaurant.customer_order(4, ["Upma", "Samosa", "Coke", "Ice Cream"])

restaurant.print_menu()
restaurant.print_booked_tables()
restaurant.print_customer_orders()
