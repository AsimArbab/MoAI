from warehouse import Warehouse
from wh_reader import WHreader

info = WHreader("data/test2.txt")
ikea = Warehouse(info.get_stock(),info.get_psus())

order = ikea.place_order("data/testorder2.txt")

result = ikea.bring_item(order, search_algorithm="hc")

PSUanzahl= str(len(result))

print("es wurden "+PSUanzahl+" PSUs bewegt")
print("Details: \n")
for psu in result:
    name = psu.get_name()
    inventar = str(psu.get_inventory())
    print(name+" mit folgende items: "+inventar)

