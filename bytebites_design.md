ByteBites Backend UML Diagram

+-------------------------------+
|          Customer             |
+-------------------------------+
| - name: String                |
| - purchaseHistory: List<Transaction> |
+-------------------------------+
| + addPurchase(tx: Transaction): void |
| + hasPurchaseHistory(): bool         |
+-------------------------------+

Customer 1 ──── * Transaction

+-------------------------------+
|          FoodItem             |
+-------------------------------+
| - name: String                |
| - price: Decimal              |
| - category: String            |
| - popularityRating: Int       |
+-------------------------------+
| + isPopular(threshold: Int): bool |
+-------------------------------+

+-------------------------------+
|           Menu                |
+-------------------------------+
| - items: List<FoodItem>       |
+-------------------------------+
| + filterByCategory(category: String): List<FoodItem> |
+-------------------------------+

Menu 1s ──── * FoodItem

+-------------------------------+
|        Transaction            |
+-------------------------------+
| - items: List<FoodItem>       |
+-------------------------------+
| + calculateTotal(): Decimal   |
+-------------------------------+

Transaction * ──── * FoodItem

Customer stores a user’s name and past purchase history.
FoodItem stores item name, price, category, and popularity rating.
Menu holds the full food item collection and filters by category.
Transaction stores selected items and computes the total cost.