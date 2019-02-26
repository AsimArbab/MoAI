from psu import PSU
from collections import Counter


class Warehouse:
    """
    PSU Warehouse Representation
    """
    def __init__(self, stock, psus, name=None):
        """
        Warehouse Object

        Args:
            stock (str[]): List of Items the WH will have in stock
            psus (str[]): List of each PSUs content the WH will contain
            name (str): Name for the WH, defaults to None object

        Attributes:
            name (str): Name/Identifier of the Warehouse
            stock (str[]): Items in Stock in the Warehouse
            psus (PSU[]): All PSUs the Warehouse contains.
            storage (dict of str: PSU[]): Hashtable with item names as keys for lists of PSUs that contain them

        """

        self.name = name
        self.stock = stock
        self.psus = [PSU("PSU_" + str(identifier), psu) for identifier, psu in enumerate(psus, 1)]
        self.storage = {}
        for item in stock:
            self.storage[item] = []
            for psu in self.psus:
                for hits in range(psu.check_for(item)):
                    self.storage[item].append(psu)


    def look_up(self, item):
        """
        looks up PSU Objects that contain a given item

        Args:
            item (str): name of the sought after item

        Returns:
           PSU[]: List of PSU Objects that contain the item. If a PSU contains multiple instances
            of the item, it will add that PSU multiple times to the list as well

        """
        return self.storage[item][:]


    def availability(self, item):
        """
        Checks availabilty of an items in terms of numbers in stock

        Args:
            item (str): the items to be checked for availability

        Returns:
            int: how many of the item are in stock

        """
        return len(self.look_up(item))


    def place_order(self, order):
        #check if input is a filepath
        if type(order) == str:
            with open(order, "r") as data:
                ordered = data.read().split('\n')[0].split(" ")

        else:
            ordered = order

        # check if all items are part of the warehouses stock
        for item in ordered:
            if item not in ordered:
                return []

        # check if enough of each product is in stock
        uniques = set(ordered)
        occurrences = Counter(ordered)
        for item in uniques:
            if occurrences[item] > self.availability(item):
                return []

        # if everything checks out return list of sets of what psus carry each item
        else:
            return [list(set(self.look_up(item))) for item in ordered]
