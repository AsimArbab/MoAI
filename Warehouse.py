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
            productIDs (dict of str: int): assigns each item on stock a productID
                                           starting with one
               Example:
                    {'i1': 1, 'i2': 2, 'i3': 3, 'i4': 4, 'i5': 5, 'i6': 6}
        """

        self.name = name
        self.stock = stock
        self.productIDs = {product_name: product_ID for product_ID, product_name in enumerate(stock, 1)}
        self.storage = 0 #is going to be the hashtable of which items can be found in which psu



    def look_up(item):
        return #will return a list of PSUs containing given item


    def place_order(self):
        return

