"""
Products Module for Best Buy Store System

This module defines the Product class for managing inventory in a
Best Buy store. It handles product information, stock management,
and purchase operations with proper validation.
"""


class Product:
    """
    Represents a product in the Best Buy store.
    Manages product information and purchase operations.
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Initialize a Product instance with validation.
        Raises ValueError for invalid inputs.
        """
        if not name or name.strip() == '':  # Validate name is not empty
            raise ValueError('Product name cannot be empty')
        if price < 0:
            raise ValueError('Product price cannot be negative')
        if quantity < 0:
            raise ValueError('Product quantity cannot be negative')

        self.name: str = name
        self.price: float = float(price)
        self.quantity: int = int(quantity)
        self.active: bool = True  # Products start as active

    def get_quantity(self) -> int:
        """
        Getter method for product quantity.
        Returns current stock level as integer.
        """
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Setter method for product quantity.
        Auto-deactivates product when quantity reaches zero.
        """
        if quantity < 0:  # Validate new quantity
            raise ValueError('Quantity cannot be negative')
        self.quantity = quantity
        if self.quantity == 0:  # Deactivate if out of stock
            self.deactivate()

    def is_active(self) -> bool:
        """Checks if product is currently active for sale."""
        return self.active

    def activate(self) -> None:
        """Activates product for sale."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivates product from sale."""
        self.active = False

    def show(self) -> str:
        """
        Creates formatted string representation of product.
        Format: 'Name, Price: X, Quantity: Y'
        """
        return (
            f'{self.name}, '
            f'Price: {self.price}, '
            f'Quantity: {self.quantity}'
        )

    def buy(self, quantity: int) -> float:
        """
        Process purchase of specified quantity.
        Returns total price, updates stock.
            Raises RuntimeError if product is not active.
            Raises ValueError if insufficient stock.
        """
        if not self.active:  # Validate product is available
            raise RuntimeError('Product is not active')
        if quantity > self.quantity:  # Check there is sufficient stock
            raise ValueError('Quantity requested exceeds available stock')
        total_price: float = quantity * self.price
        self.quantity -= quantity  # Update inventory
        if self.quantity == 0:  # Auto-deactivate if sold out
            self.deactivate()
        return float(total_price)


def main() -> None:
    """Test Product class functionality with provided examples."""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == '__main__':
    main()
