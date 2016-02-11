class Order(object):
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.items = {}

    def add_product(self, product):
        try:
            self.items[product] += 1
        except KeyError:
            self.items[product] = 1

    def deliver_product(self, product, product_quantity):
        item_count = self.items[product]
        if item_count < product_quantity:
            raise Exception("Remaining to deliver %s products, but delivering too many: %s for order %s" % (item_count, product_quantity, self))
        item_count -= product_quantity
        if item_count == 0:
            self.items.pop(product)
        else:
            self.items[product] = item_count

    def completed(self):
        return len(self.items.keys()) == 0

    def __repr__(self):
        return '<Order id=%r,location=%r>' % (self.id, self.location)
