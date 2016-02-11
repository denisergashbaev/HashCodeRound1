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
