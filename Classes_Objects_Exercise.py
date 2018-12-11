class Store:
    def __init__(self,name):
        self.name = name
        self.items = []

    def add_item(self,name,price):
        item_property = {'name' : name, 'price' : price}
        self.items.append(item_property)

    def stock_price(self):
        return sum([item_property['price'] for item_property in self.items])
