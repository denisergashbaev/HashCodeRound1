from drone import Drone
from file_utils import get_line
from order import Order
from product import Product
from warehouse import Warehouse


class Config(object):
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            self.rows, self.cols, self.num_drones, self.num_turns, self.max_payload = get_line(f.readline())
            self.drones = []
            for _ in range(self.num_drones):
                self.drones.append(Drone())
            self.num_product_types = get_line(f.readline())
            weights = f.readline().split(' ')
            self.products = []
            for idx in range(self.num_product_types):
                self.products.append(Product(idx, weights[idx]))

            self.num_warehouses = get_line(f.readline())
            self.warehouses = []
            for warehouse_idx in range(self.num_warehouses):
                loc = (get_line(f.readline()))
                warehouse = Warehouse(warehouse_idx, loc)
                for prod_idx, prod_quant in enumerate(get_line(f.readline())):
                    prod = self.products[prod_idx]
                    warehouse.add_product(prod, prod_quant)
                self.warehouses.append(warehouse)

            self.num_orders = get_line(f.readline())
            self.orders = []
            for order_idx in range(self.num_orders):
                loc = (get_line(f.readline()))
                order = Order(order_idx, loc)
                f.readline() #just skip cause we know it from the next line
                for prod_id in get_line(f.readline()):
                    prod = self.products[prod_id]
                    order.add_product(prod)
                self.orders.append(order)
