class Drone(object):
    def __init__(self, id, location, max_payload):
        self.id = id
        self.location = location
        self.max_payload = max_payload
        self.items = {}
        self.commands = []
        self.current_payload = 0

    def load(self, warehouse, product, quantity):
        incoming_payload = product.max_weight * quantity
        if self.max_payload < self.current_payload + incoming_payload:
            raise Exception('Payload exceeded for %s' % self)

        try:
            item_count = self.items[product]
        except KeyError:
            item_count = 0
        self.items[product] = item_count + quantity
        self.current_payload += incoming_payload
        self._load_command(product.id, quantity, warehouse.id)
        self.location = warehouse.location

    def _load_command(self, product_id, product_quantity, warehouse_id):
        cmd = "%s L %s %s %s" % (self.id, warehouse_id, product_id, product_quantity)
        self.commands.append(cmd)
        return cmd

    def deliver(self, order, product, product_quantity):
        item_count = self.items[product]
        if item_count < product_quantity:
            raise Exception("Requested product quantity of %s is more than available %s for %s" % (product_quantity, item_count, self))
        item_count -= product_quantity
        self.items[product] = item_count
        self._deliver_command(product.id, product_quantity, order.id)
        self.location = order.location

    def _deliver_command(self, product_id, product_quantity, order_id):
        cmd = "%s D %s %s %s" % (self.id, order_id, product_id, product_quantity)
        self.commands.append(cmd)
        return cmd

    def __repr__(self):
        return '<Drone id=%r,location=%r,max_payload=%r>' % (self.id, self.location, self.max_payload)
