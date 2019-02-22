class PSU:
    """
    Respresentation of a Portable Storage Unit
    """

    def __init__(self, identifier, inventory):
        """
        PSU Object

        Args:
            identifier (str): the PSUs identifier, e.g. PSU_42
            inventory (str[]): a list of objects to be stored in the PSU

        Attributes:
            identifier (str): the PSUs identifiert
            inventory (str[]): the PSUs inventory
        """
        self.identifier = identifier
        self.inventory = inventory

    def get_name(self):
        """
        Getter Method for the PSUs identifier

        Returns:
            str: PSUs identifier

        """
        return self.identifier

    def get_inventory(self):
        """
        Getter Method for PSUs inventory

        Returns:
            str[]: all items the PSU is holding

        """
        return self.inventory

    def check_for(self, some_item):
        """
        Checks how many instances of a given item the PSU is holding

        some_item (str): The item to be checked for

        Returns:
            int: how many instances of some_item are contained in the PSU

        """
        item_count = 0
        for item in self.inventory:
            if item == some_item:
                item_count += 1
        return item_count
