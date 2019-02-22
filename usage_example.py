from wh_reader import WHreader
from warehouse import Warehouse
from psu import PSU

#to create a Warehouse

#read text file containing warehouse information into a WHreader Object
info = WHreader("data/test.txt")

#use the get_stock and get_psus methods of the WHreader Object as input for the Warehouse Object
ikea = Warehouse(stock=info.get_stock(),psus=info.get_psus(), name="ikea")


#this is the PSUs in list form before being fed to the Warehouse Object
for i, psu in enumerate(info.get_psus(),1):
    print("PSU_"+str(i)+" contains: "+str(psu),"\n")

print("\n\n\n")

#The warehouse object converts them into PSU objects, giving each an identifier (PSU_n)
#The get_name method returns the identifier of the PSU, and the get_items method returns all it's items as
#a String array
psu_list = ikea.psus
for psu in psu_list:
    print("Identifier: "+psu.get_name() + "\n Inventory:" + str(psu.get_inventory()))

print("\n\n\n")

#PSU_3 eg is at index 2 of the array and can be checked for its identifier or item "i3"
thirdpsu = psu_list[2]
print("this psus identifier is: " + thirdpsu.get_name())
print("it contains i3 " + str(thirdpsu.check_for("i3"))+" time")
print("this is its whole inventory "+str(thirdpsu.get_inventory()))
print("\n\n\n")

#but generally we want to know if an item is available in the warehouse and if so in which psus.
#this will return a list of PSU objects.
for item in ikea.stock:
    print(ikea.look_up(item))

print("\n\n\n")

#hence to see their identifiers or the inventories in String form we need to use the get_name or get_inventory method
for item in ikea.stock:
    print("\n\nitem "+item+ " can be found in: ")
    for hit in ikea.look_up(item):
        print(hit.get_name()+", ", end="")
