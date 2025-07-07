"""
Product Module

This module contains the Product class for the Best Buy store system.
It handles product information, inventory management, and purchase operations.
"""


class Product:
    """
    Represents a product in the Best Buy store.
    Each product has a name, price, quantity, and active status.
    """

    def __init__(self, name, price, quantity):
        """
        Initialize a new Product instance with validation.
        """
        # Input validation
        if not name or name.strip() == '':  # Empty or whitespace-only names
            raise ValueError('Product name cannot be empty')
        if price < 0:
            raise ValueError('Product price cannot be negative')
        if quantity < 0:
            raise ValueError('Product quantity cannot be negative')

        # Initialize instance variables
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True  # Products are active by default

    def get_quantity(self) -> int:
        """
        Get the current quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Set the product quantity and update active status.
        """
        # Defensive programming - validate even in setters
        if quantity < 0:
            raise ValueError('Quantity cannot be negative')

        self.quantity = quantity

        # Business logic: no stock means inactive
        if self.quantity == 0:
            self.deactivate()

    # Active status management methods
    def is_active(self) -> bool:
        """Check if the product is active.

        Returns:
            bool: True if active, False otherwise
        """
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self) -> str:
        """Get a string representation of the product.

        Returns:
            str: Formatted product information
        """
        # Using f-string for readable formatting
        return f'{self.name}, Price: {self.price}, Quantity: {self.quantity}'

    def buy(self, quantity: int) -> float:
        """
        Purchase a specified quantity of the product.
        """
        # Input validation - check purchase is possible
        if quantity <= 0:
            raise ValueError('Purchase quantity must be positive')
        if quantity > self.quantity:
            # Defensive programming: prevent negative inventory
            raise ValueError('Insufficient stock available')

        # Business logic: price calculation
        total_price = quantity * self.price

        # Update inventory after purchase
        self.quantity -= quantity

        # Business rule: auto-deactivate when sold out
        if self.quantity == 0:
            self.deactivate()

        return total_price


# Test code - only runs when file is executed directly
if __name__ == '__main__':
    # Test the Product class implementation
    bose = Product('Bose QuietComfort Earbuds', price=250, quantity=500)
    mac = Product('MacBook Air M2', price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())
