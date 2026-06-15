# from models import Customer, FoodItem, Menu, Transaction

# # Create sample food items
# burger = FoodItem("Spicy Burger", 8.99, "Entrees", 9)
# soda = FoodItem("Large Soda", 2.50, "Drinks", 7)
# cake = FoodItem("Chocolate Cake", 4.25, "Desserts", 8)

# # Create a menu and add food items
# menu = Menu()
# menu.add_item(burger)
# menu.add_item(soda)
# menu.add_item(cake)

# # Print all menu items to check that attributes are stored correctly
# print("Menu items:\n")
# for item in menu.items:
#     print(f"Item: {item.name}")
#     print(f"Price: ${item.price:.2f}")
#     print(f"Category: {item.category}")
#     print(f"Popularity Rating: {item.popularity_rating}/10")
#     print()

# # Filter menu items by category
# drinks = menu.filter_by_category("Drinks")

# print("Filtered Drinks:\n")
# for item in drinks:
#     print(f"Item: {item.name}")
#     print(f"Price: ${item.price:.2f}")
#     print(f"Category: {item.category}")
#     print(f"Popularity Rating: {item.popularity_rating}/10")
#     print()

# # Create a transaction and add selected food items
# transaction = Transaction()
# transaction.add_item(burger)
# transaction.add_item(soda)

# print("Transaction total:")
# print(f"${transaction.calculate_total():.2f}")

# # Create a customer and check purchase history
# customer = Customer("Brian")

# print("\nCustomer has purchase history before purchase:")
# print(customer.has_purchase_history())

# customer.add_purchase(transaction)

# print("\nCustomer has purchase history after purchase:")
# print(customer.has_purchase_history())

# print("\nCustomer info:")
# print(f"Name: {customer.name}")
# print(f"Number of Past Purchases: {len(customer.purchase_history)}")



from models import Customer, FoodItem, Menu, Transaction

# Create sample food items
burger = FoodItem("Spicy Burger", 8.99, "Entrees", 9)
soda = FoodItem("Large Soda", 2.50, "Drinks", 7)
cake = FoodItem("Chocolate Cake", 4.25, "Desserts", 8)

# Create a menu and add items
menu = Menu()
menu.add_item(burger)
menu.add_item(soda)
menu.add_item(cake)

# Check that all menu item attributes are stored correctly
print("Menu items:\n")
for item in menu.items:
    print(f"Item: {item.name}")
    print(f"Price: ${item.price:.2f}")
    print(f"Category: {item.category}")
    print(f"Popularity Rating: {item.popularity_rating}/10")
    print()

# Check filtering by category
drinks = menu.filter_by_category("Drinks")

print("Filtered Drinks:\n")
for item in drinks:
    print(f"Item: {item.name}")
    print(f"Price: ${item.price:.2f}")
    print(f"Category: {item.category}")
    print(f"Popularity Rating: {item.popularity_rating}/10")
    print()

# Check sorting by popularity
popular_items = menu.sort_by_popularity()

print("Menu items sorted by popularity:\n")
for item in popular_items:
    print(f"Item: {item.name}")
    print(f"Popularity Rating: {item.popularity_rating}/10")
    print()

# Check transaction total
transaction = Transaction()
transaction.add_item(burger)
transaction.add_item(soda)

print("Transaction total:")
print(f"${transaction.calculate_total():.2f}")

# Check customer purchase history
customer = Customer("Brian")

print("\nCustomer has purchase history before purchase:")
print(customer.has_purchase_history())

customer.add_purchase(transaction)

print("\nCustomer has purchase history after purchase:")
print(customer.has_purchase_history())

print("\nCustomer info:")
print(f"Name: {customer.name}")
print(f"Number of Past Purchases: {len(customer.purchase_history)}")