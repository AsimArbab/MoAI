from wh_reader import WHreader
from warehouse import Warehouse
from psu import PSU

#read the test file
info = WHreader("data/test.txt")

#print the contents of the test file
for i, psu in enumerate(info.get_psus()):
    print("PSU_"+str(i)+" contains: "+str(psu),"\n")

#create warehouse object from info
ikea = Warehouse(info.get_stock(),info.get_psus(), "ikea")

#will continue this later
