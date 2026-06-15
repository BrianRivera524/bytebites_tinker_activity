# ByteBites Models

# This file will contain the main Python classes for the ByteBites backend system.

# Customer:
# Represents a ByteBites user and stores the customer's name and purchase history.

# FoodItem:
# Represents one food or drink item with a name, price, category, and popularity rating.

# Menu:
# Represents the full collection of FoodItem objects and allows filtering by category.

# Transaction:
# Represents a customer's order, stores selected FoodItem objects, and calculates the total cost.

'''
Implementation Plan for models.py

The project will use four beginner-friendly Python classes: Customer, FoodItem, Menu, and Transaction.

Customer:
- Stores the customer's name as a string.
- Stores purchase_history as a list of Transaction objects.
- Uses add_purchase(transaction) to add a completed transaction to the customer's history.
- Uses has_purchase_history() to check whether the customer has made past purchases.

FoodItem:
- Stores the item's name, price, category, and popularity_rating.
- Uses is_popular(threshold) to check whether the item's popularity rating is high enough.

Menu:
- Stores items as a list of FoodItem objects.
- Uses add_item(item) to add a FoodItem to the menu.
- Uses filter_by_category(category) to return only items from a matching category.

Transaction:
- Stores items as a list of FoodItem objects selected by the customer.
- Uses add_item(item) to add a FoodItem to the transaction.
- Uses calculate_total() to return the sum of all selected item prices.

'''

class Customer:
    """Represents a ByteBites customer with a name and purchase history."""

    def __init__(self, name, purchase_history=None):
        self.name = name
        self.purchase_history = purchase_history or []

    def add_purchase(self, transaction):
        self.purchase_history.append(transaction)

    def has_purchase_history(self):
        return len(self.purchase_history) > 0


class FoodItem:
    """Represents a ByteBites menu item with price, category, and popularity."""

    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def is_popular(self, threshold):
        return self.popularity_rating >= threshold


class Menu:
    """Represents the ByteBites menu and supports category filtering."""

    def __init__(self, items=None):
        self.items = items or []

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        # Return only the menu items that match the requested category.
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self):
        # Return menu items sorted from highest popularity rating to lowest.
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Transaction:
    """Represents a ByteBites customer's order and calculates the total cost."""

    def __init__(self, items=None):
        self.items = items or []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        # Add and return the prices of all selected food items.
        return sum(item.price for item in self.items)
    
# I reviewed the generated scaffold and confirmed that it only uses the four planned classes: 
# Customer, FoodItem, Menu, and Transaction. The attributes match the UML diagram and ByteBites feature request.
# I added add_item() methods to Menu and Transaction because they fit the design and make it easier to build 
# and test the system later.


# I accepted the custom ByteBites Agent's suggestion to add docstrings.
# The docstrings briefly describe the purpose of each class while keeping the code simple
# and aligned with the ByteBites specification.


# Part 3a: Algorithmic Plan
# Customer:
# - add_purchase(transaction): adds a completed Transaction to the customer's purchase history.
# - has_purchase_history(): checks whether the customer has any past transactions.
#
# FoodItem:
# - is_popular(threshold): checks whether the item's popularity rating meets or exceeds the threshold.
#
# Menu:
# - add_item(item): adds a FoodItem object to the menu.
# - filter_by_category(category): returns FoodItem objects whose category matches the requested category.
# - sort_by_popularity(): returns menu items sorted from highest popularity rating to lowest.
#
# Transaction:
# - add_item(item): adds a selected FoodItem to the transaction.
# - calculate_total(): adds together the prices of all selected FoodItem objects and returns the total.
#
# This plan keeps the algorithmic work aligned with the ByteBites spec and UML diagram.


# Part 3c Review:
# I used the custom ByteBites Agent to review the algorithmic methods.
# The agent confirmed that filter_by_category, sort_by_popularity, and calculate_total
# are clear, beginner-friendly, and aligned with the ByteBites UML design.
# I accepted the suggestion to add short docstrings for extra clarity.