class Warehouse(object):
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.items = {}

    def add_product(self, product, quantity):
        try:
            item_count = self.items[product]
        except KeyError:
            item_count = 0
        self.items[product] = item_count + quantity

    def __repr__(self):
        return '<Warehouse id=%r,location=%r>' % (self.id, self.location)
