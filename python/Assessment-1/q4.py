# 4. Create a ShoppingCart class for an online shopping application.

# The class should contain:

# Variables:

# productName

# price

# quantity

# Methods:

# addProduct()

# removeProduct()

# calculateTotal()

# displayCart()

# Requirements:

# addProduct() should add a product to the cart.

# removeProduct() should remove a product from the cart.

# calculateTotal() should return price × quantity.

# displayCart() should display the product details and total price.

# Use a constructor to initialize the product details.


# Example Output:

# Product: Laptop

# Price: ₹50,000

# Quantity: 2

# Total: ₹1,00,000


class ShoppingCart:
    def __init__(self, productName, price, quantity):
        self.productName = productName
        self.price = price
        self.quantity = quantity

    def addProduct(self, productName, price, quantity):
        self.productName = productName
        self.price = price
        self.quantity = quantity

        print(f"The product is added with a product name {self.productName}")

    def removeProduct(self):
        self.productName = None
        self.price = 0
        self.quantity = 0

    def calculateTotal(self):
        return self.price * self.quantity

    def displayCart(self):
        if self.productName:
            print(f"The product is {self.productName}")
            print(f"The price is {self.price}")
            print(f"The quantity is {self.quantity}")
            print(f"Total price is {self.calculateTotal()}")
        else:
            print("No product")


cart = ShoppingCart("Notebook", 10, 2)
cart.displayCart()
cart.removeProduct()
cart.displayCart()
cart.addProduct("mobile", 1000, 1)
cart.displayCart()

cart.addProduct("pen", 1000, 1)
cart.displayCart()
cart.removeProduct()
cart.displayCart()
