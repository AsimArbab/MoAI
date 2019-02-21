import PSU


class Warehouse:
    '''
    PSU Warehouse Representation
    '''

    def __init__(self, stock, psus, name=""):
        """
        Constructor for Warehouse Object
        Creates/Initializes Warehouse Object

        Args:
            stock (str[]): List of Items the WH will have in stock
            psus (str[]): List of each PSUs content the WH will contain
            name (str): Name for the WH, defaults to empty String

        Attributes:
            name (str): Name/Identifier of the Warehouse
            stock (str[]): Items in Stock in the Warehouse
            psus (PSU[]): List of PSU Objects
            storage (dict of str: PSU): Hashtable with item names as keys for PSUs that contain them
            productIDs (dict of str: int): assigns each item on stock a productID
                                           starting with one
               Examples:
                    productIDs = {'i1': 1, 'i2': 2, 'i3': 3, 'i4': 4, 'i5': 5, 'i6': 6}

                    storage["i3"] =
        """

        self.name = name
        self.stock = stock
        self.psus = [PSU("psu" + str(identifier), psu) for identifier, psu in enumerate(psus, 1)]  # add psu as String
        self.storage = {}
        for item in stock:
            self.storage[item] = []
            for psu in self.psus:
                for hits in range(psu.check_for(item)):
                    self.storage[item].append(psu)

        # self.storage = {item: psu for item in stock for psu in self.psus for hit in range(psu.check_for(item))}
        # self.productIDs = {product_name: product_ID for product_ID, product_name in enumerate(stock, 1)} might use this later for efficiency

    def look_up(self, item):
        return self.storage[item][:]

    def place_order(self):
        return

    # thinking about saving items in psus as ints for faster/easier comparison
    def PrdctToID(self):
        return True

    def IDtoPrdct(self):
        return True
