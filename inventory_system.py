class Product:
    def __init__(self, name: str, price: float, stock: int, low_stock_threshold: int = 5):
        self.name = name
        self._price = price
        self._stock = stock
        self.low_stock_threshold = low_stock_threshold

    # Property decorator for price validation
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    # Property decorator for stock validation (preventing negative stock values)
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock cannot be negative.")
        self._stock = value

    def add_stock(self, amount: int):
        if amount > 0:
            self.stock += amount
            print(f"-> Added {amount} units to {self.name}. New Stock: {self.stock}")
        else:
            print("Amount must be greater than zero.")

    def remove_stock(self, amount: int):
        if 0 < amount <= self.stock:
            self.stock -= amount
            print(f"-> Removed {amount} units from {self.name}. Remaining Stock: {self.stock}")
        else:
            print(f"-> Error: Cannot remove {amount} units (Insufficient stock or invalid amount).")

    def is_low_stock(self) -> bool:
        return self.stock <= self.low_stock_threshold

    # Bonus: __str__ method for clean object printing
    def __str__(self):
        return f"Product: {self.name} | Price: ${self._price:.2f} | Stock: {self._stock}"


class PerishableProduct(Product):
    def __init__(self, name: str, price: float, stock: int, expiry_date: str, low_stock_threshold: int = 5):
        super().__init__(name, price, stock, low_stock_threshold)
        self.expiry_date = expiry_date

    # Extending __str__ for perishable specific details (expiry tracking)
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} | Expiry Date: {self.expiry_date}"


# --- Testing the Inventory System ---
if __name__ == "__main__":
    print("=== Inventory Management System Demo ===\n")

    # Creating regular and perishable products
    p1 = Product("Laptop", 1200.0, 10, low_stock_threshold=3)
    p2 = PerishableProduct("Milk", 2.5, 4, expiry_date="2026-05-10", low_stock_threshold=5)

    print("Initial Inventory:")
    print(p1)
    print(p2)
    print("-" * 40)

    # Core Operations Demo
    print("\n[Performing Stock Operations]")
    p1.remove_stock(8)  # Should trigger low stock check soon
    p2.add_stock(6)

    print("\n[Checking Low-Inventory Alerts]")
    for item in [p1, p2]:
        if item.is_low_stock():
            print(f"ALERT: '{item.name}' is running low on stock! (Current: {item.stock})")

    print("\nFinal Inventory Status:")
    print(p1)
    print(p2)