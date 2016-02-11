class Drone(object):
    def __init__(self, id, location, max_payload):
        self.id = id
        self.location = location
        self.max_payload = max_payload
        self.items = {}

    def load(self, product, quantity):
        try:
            item_count = self.items[product]
        except KeyError:
            item_count = 0
        self.items[product] = item_count + quantity

    def unload(self):
        pass

    def __repr__(self):
        return '<Drone id=%r,location=%r,max_payload=%r>' % (self.id, self.location, self.max_payload)
