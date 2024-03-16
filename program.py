class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.id] = product

    def remove_product(self, id):
        if id in self.products:
            del self.products[id]

    def update_quantity(self, id, quantity):
        if id in self.products:
            self.products[id].quantity = quantity

class Sales:
    def __init__(self):
        self.sales = []

    def record_sale(self, product, quantity):
        self.sales.append((product, quantity))
        product.quantity -= quantity

class RetailStore:
    def __init__(self):
        self.inventory = Inventory()
        self.sales = Sales()

    def add_product_to_inventory(self, product):
        self.inventory.add_product(product)

    def sell_product(self, id, quantity):
        if id in self.inventory.products and self.inventory.products[id].quantity >= quantity:
            self.sales.record_sale(self.inventory.products[id], quantity)
        else:
            print("Product not available or insufficient quantity.")
