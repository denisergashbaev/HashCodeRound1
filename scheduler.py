from numpy import inf
from math import sqrt, floor


class Scheduler(object):
    def __init__(self, config):
        self.config = config

    @staticmethod
    def distance(loc1, loc2):
        return floor(sqrt(abs(loc1[0] - loc2[0])^2 + abs(loc1[1] - loc2[1])^2))

    def find_closest_warehouse_with_item(self, item, drone):
        min_dist = inf
        for w in self.config.warehouses:
            if item in w.items and min_dist < self.distance(drone.location, w.location):
                min_dist = self.distance(drone.location, w.location)
                closest_warehouse = w

        return closest_warehouse

    def compute_time_for_order(self, drone, order):
        time = 0
        drone_location = drone.location
        warehouses = {w.id: [] for w in self.config.warehouses}
        for item in order.items:
            w = self.find_closest_warehouse_with_item(item, drone)
            warehouses[w.id].append(item)

        for key in warehouses:
            if warehouses[key]:
                time += self.distance(drone_location, w.location)
                time += self.distance(w.location, order.location)
                drone_location = order.location
        return time

