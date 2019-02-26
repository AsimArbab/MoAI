from warehouse import Warehouse
from wh_reader import WHreader
from wh_search import neighborhood
from wh_search import objective_function

info = WHreader("data/test2.txt")
ikea = Warehouse(info.get_stock(), info.get_psus(), "ikea")

#warehouse layout can be found in test2.txt
order1 = ["apple", "apple", "banana", "eclaire"]
order2 = ["donut", "apple", "banana", "cucumber"]
order3 = ["cucumber", "cucumber", "cucumber", "donut", "donut","donut"]
order4 = ["donut", "donut", "donut", "donut","donut","donut","donut","donut"]
order5 = ["apple","banana","cucumber","donut","eclaire"]


statespace1 = ikea.place_order(order3)

for part in statespace1:
    print("\n")
    for psu in part:
        print(psu.get_name()+" | ",end="")


statespace2 = [[1,3,6],[1,2,4,5,6],[1,2,3,4,5,6],[5,7],[5,6]]
state = [1,1,1,5,5]


print("\n\n\n")
print(neighborhood(state, statespace2))

print("\n\n\n")
curr_state = statespace1[:][0]
psu_neighborhood = neighborhood((curr_state), statespace1)
for configuration in psu_neighborhood:
    print("objective function: "+str(objective_function(configuration))+"\n")
    for psu in configuration:
        print(psu.get_name(),end=" | ")
same=ikea.psus[0]
print(objective_function([same,same,same]))