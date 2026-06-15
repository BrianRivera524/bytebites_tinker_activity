# ByteBites Tinker Activity

# Project Overview

ByteBites is a beginner-friendly Python backend design activity for a campus food ordering app. The goal of this project was to turn a vague feature request into a clear object-oriented system using UML-style design, Python classes, simple algorithms, and pytest tests.

The system models four core classes:

- 'Customer'
- 'FoodItem'
- 'Menu'
- 'Transaction'

These classes work together to represent customers, menu items, menu filtering, transaction totals, and purchase history.

# Workflow

# 1. System Design

I started by reading the ByteBites feature request and identifying the four main nouns that needed to become classes. From the request, I selected 'Customer', 'FoodItem', 'Menu', and 'Transaction' as the core components.

I created 'bytebites_spec.md' to store the client feature request and my candidate classes. Then I used my AI coding assistant to generate an initial UML-style diagram. After reviewing the draft, I checked whether it stayed within the four required classes, included the correct attributes, and avoided unnecessary extra features.

# 2. Custom AI Agent

I configured a custom ByteBites Design Agent in VS Code under:

'''
text
.github/agents/bytebites_design_agent.md

'''

The purpose of this agent was to guide AI suggestions so they stayed simple, beginner-friendly, and aligned with the ByteBites specification. The agent was instructed to avoid extra classes, databases, APIs, or advanced features.

I used the custom agent to refine the UML diagram and compare it against the original AI draft. The final design was saved in 'bytebites_design.md'.

# 3. Python Class Implementation

Next, I created 'models.py' and implemented the four Python classes.

Each class has a clear responsibility:

* 'Customer' stores a user's name and purchase history.
* 'FoodItem' stores item information such as name, price, category, and popularity rating.
* 'Menu' stores food items and supports filtering and sorting.
* 'Transaction' stores selected food items and calculates the total cost.

I used the AI assistant to plan the structure, draft scaffolds, and review the implementation. I accepted simple refinements, such as adding docstrings and keeping the methods beginner-friendly.

# 4. Algorithmic Methods

I implemented simple algorithmic behavior in the classes:

* 'filter_by_category()' filters menu items by category.
* 'sort_by_popularity()' sorts menu items from highest to lowest popularity rating.
* 'calculate_total()' computes the total cost of a transaction.
* 'add_item()' helps build menus and transactions.
* 'add_purchase()' records completed transactions for a customer.

I manually tested these methods using 'manual_check.py' before moving on to formal tests.

# 5. Testing and Validation

I created 'test_bytebites.py' using pytest. The test suite checks the main behaviors of the system:

* calculating a transaction total with multiple items
* returning zero for an empty transaction
* filtering menu items by category
* sorting menu items by popularity
* updating customer purchase history after a transaction

After refining the tests with the custom ByteBites Agent, I ran:

'''
python -m pytest

'''

The final result was:

'''
5 passed

'''

# Files in This Project

'''

bytebites_spec.md
bytebites_design.md
draft_from_copilot.md
models.py
manual_check.py
test_bytebites.py
.github/agents/bytebites_design_agent.md
README.md

'''

# Reflection

This activity helped me practice using AI as a design partner while still being responsible for the final decisions. I used AI to brainstorm, draft, and review ideas, but I checked the outputs carefully to make sure they matched the ByteBites specification.

The most important part of the workflow was keeping the design simple. Instead of adding unnecessary systems like databases, logins, or payment processing, I focused on the four required classes and the core behaviors described in the feature request.
