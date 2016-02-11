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

    def __repr__(self):
        return '<Order id=%r,location=%r>' % (self.id, self.location)
