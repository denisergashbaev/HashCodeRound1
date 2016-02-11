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
        if item_count < 0:
            raise Exception("Item count cannot be less than zero %s" % item_count)
        self.items[product] = item_count

    def completed(self):
        for _, value in self.items.iteritems():
            if value > 0:
                return False
        return True

    def __repr__(self):
        return '<Order id=%r,location=%r>' % (self.id, self.location)
