'''
AI's test suggestions:

Pytest Test Ideas for ByteBites
Use the public class behaviors from models.py and verify expected outcomes.

1. Calculating transaction totals
Create several FoodItem objects with known price values.
Add them to a Transaction.
Assert transaction.calculate_total() returns the sum of those prices.
Example focus: two or three items with different prices.
2. Empty transaction totals
Create a Transaction with no items.
Assert calculate_total() returns 0.
This checks the default empty state works correctly.
3. Filtering menu items by category
Create a Menu with mixed FoodItem categories like "Drinks" and "Desserts".
Call menu.filter_by_category("Drinks").
Assert the result only contains items whose category equals "Drinks".
Assert non-matching items are excluded.
4. Sorting menu items by popularity
Create a Menu with FoodItem objects having varying popularity_rating.
Call menu.sort_by_popularity().
Assert the returned list is ordered from highest to lowest popularity.
Check the first item has the highest rating and the last has the lowest.
5. Checking customer purchase history
Create a Customer with no history.
Assert customer.has_purchase_history() is False.
Add a Transaction via customer.add_purchase(transaction).
Assert customer.has_purchase_history() is now True.
Optionally assert the added transaction appears in customer.purchase_history.
Notes
Keep tests focused on behavior, not implementation details.
Use only the four classes: Customer, FoodItem, Menu, Transaction.
These ideas match the ByteBites spec: totals for orders, category browsing, popularity sorting, and purchase history tracking.

'''

# I reviewed the AI-generated pytest ideas and kept the tests that matched 
# the ByteBites specification. The selected test ideas focus on public behavior: 
# calculating transaction totals, handling an empty transaction, filtering menu items 
# by category, sorting by popularity, and checking customer purchase history. 
# I avoided tests that depend on internal implementation details or add features 
# outside the UML design.

from models import Customer, FoodItem, Menu, Transaction


def test_calculate_total_with_multiple_items():
    burger = FoodItem("Spicy Burger", 8.99, "Entrees", 9)
    soda = FoodItem("Large Soda", 2.50, "Drinks", 7)

    transaction = Transaction()
    transaction.add_item(burger)
    transaction.add_item(soda)

    assert transaction.calculate_total() == 11.49


def test_order_total_is_zero_when_empty():
    transaction = Transaction()

    assert transaction.calculate_total() == 0


def test_filter_by_category_returns_matching_items():
    burger = FoodItem("Spicy Burger", 8.99, "Entrees", 9)
    soda = FoodItem("Large Soda", 2.50, "Drinks", 7)
    juice = FoodItem("Orange Juice", 3.00, "Drinks", 8)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(juice)

    drinks = menu.filter_by_category("Drinks")

    assert len(drinks) == 2
    assert soda in drinks
    assert juice in drinks
    assert burger not in drinks


def test_sort_by_popularity_highest_first():
    burger = FoodItem("Spicy Burger", 8.99, "Entrees", 9)
    soda = FoodItem("Large Soda", 2.50, "Drinks", 7)
    cake = FoodItem("Chocolate Cake", 4.25, "Desserts", 8)

    menu = Menu()
    menu.add_item(soda)
    menu.add_item(cake)
    menu.add_item(burger)

    sorted_items = menu.sort_by_popularity()

    assert sorted_items[0] == burger
    assert sorted_items[1] == cake
    assert sorted_items[2] == soda


def test_customer_purchase_history_updates_after_purchase():
    customer = Customer("Brian")
    transaction = Transaction()

    assert customer.has_purchase_history() is False

    customer.add_purchase(transaction)

    assert customer.has_purchase_history() is True
    assert transaction in customer.purchase_history