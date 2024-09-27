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
