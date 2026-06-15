ByteBites Design Agent Instructions

You are helping design and implement the ByteBites backend system for a beginner-friendly Python object-oriented programming activity.

Follow these project rules:

Stay within the four required classes unless the user explicitly asks for something else:

Customer
FoodItem
Menu
Transaction

Do not add unnecessary extra classes, databases, APIs, login systems, payment systems, or advanced architecture.
Keep all suggestions simple, readable, and aligned with the ByteBites feature request.
For UML-style diagrams, include:

Class name
Main attributes
Simple methods
Clear relationships between classes

For Python scaffolds, use beginner-friendly Python code with clear constructors and simple attributes.
Each class should have one clear responsibility:

Customer stores the customer information and purchase history.
FoodItem stores item information such as name, price, category, and popularity rating.
Menu stores the full collection of FoodItem objects and filters items by category.
Transaction stores selected FoodItem objects and computes the total cost.

When reviewing diagrams or code, check whether the design matches the original ByteBites specification before suggesting changes.
Avoid over-engineering. Prefer simple methods such as:

add_purchase
filter_by_category
add_item
calculate_total

If a suggestion does not directly support the ByteBites feature request, explain that it may be unnecessary.