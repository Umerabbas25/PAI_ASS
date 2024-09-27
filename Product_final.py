# SP23_BAI_053(MINTAINER)
# SP23_BAI_029(COLLABORATOR)
class Product:
    def _init_(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        if quantity < 10:
            discount = 0
        elif 10 <= quantity < 100:
            discount = 0.10 
        else:
            discount = 0.20 

        total_price = self.price * quantity * (1 - discount)
        return total_price
    
    def make_purchase(self, quantity):
        """Reduces the stock by the purchased amount and prints the total cost."""
        try:
            if quantity <= 0:
                raise ValueError("Purchase quantity must be greater than zero.")
            if quantity > self.amount:
                raise ValueError("Insufficient stock available.")

            total_price = self.get_price(quantity)
            self.amount -= quantity
        # Create product object
product = Product("Laptop", 150, 1000)

# Test cases
product.make_purchase(5)   # No discount
product.make_purchase(50)  # 10% discount
product.make_purchase(120) # 20% discount
product.make_purchase(-5)  # Invalid quantity
product.make_purchase(200) # Insufficient stock
            print(f"Purchased {quantity} items of {self.name} for ${total_price:.2f}.")
            print(f"Remaining stock: {self.amount}")

        except ValueError as e:
            print(f"Error: {e}")
