class WHreader:
    """
    Warehouse Reader
    Reads a properly formatted warehouse *.txt file and converts its content into lists


    """
    def __init__(self, input_file):

        """
        Warehouse Reader Object

        Args:
             input_file (str): path to txt file

        Attributes:
            stock (str[]): List of items the Warehouse has in stock
            psus (str[]): List of the inventories of each PSU

        """

        with open(input_file, "r") as data:
            warehouse = data.read().split('\n')

        self.stock = warehouse[0].split(' ')
        self.psus = [psu.split(' ') for psu in warehouse[2:]]


    def get_stock(self):
        """
        Getter Method for the Warehouse stock

        Return:
            str[]: the list of items in stock

        Example:
            stock = ['i1', 'i2', 'i3']
        """
        return self.stock

    def get_psus(self):
        """
        Getter Method for the Warehouse's PSUs

        Returns:
            str[]: the list of the contents of each psu

        Example:
            psus = [['i2', 'i3'],  ['i1', 'i1', 'i3', 'i2'], ['i3', 'i1', 'i3']]
        """
        return self.psus

