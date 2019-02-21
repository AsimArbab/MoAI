class PSU:

    def __init__(self, identifier, inventory):
        self.identifier = identifier
        self.inventory = inventory

    def get_name(self):
        return self.identifier

    def get_inventory(self):
        return self.inventory

    def check_for(self, some_item):
        item_count = 0
        for item in self.inventory:
            if item == some_item:
                item_count += 1
        return item_count
