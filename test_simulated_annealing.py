from warehouse import Warehouse
from wh_reader import WHreader
from wh_search import neighbourhood
from wh_search import objective_function
from wh_search import simulated_annealing

info = WHreader("data/problem1.txt")
ikea = Warehouse(info.get_stock(), info.get_psus(), "ikea")

#warehouse layout can be found in test2.txt
order1 = ["apple", "apple", "banana", "eclaire"]
order2 = ["magic-tv", "magnificient-computer", "trendy-mouse", "hip-keyboard", "awesome-phone-battery", "awesome-laptop-battery",
          "infamous-laptop-charger", "magic-dryer"]
orderx = ["donut", "apple", "banana", "cucumber"]
order3 = ["cucumber", "cucumber", "cucumber", "donut", "donut","donut"]
order4 = ["donut", "donut", "donut", "donut","donut","donut","donut","donut"]
order5 = ["apple","banana","cucumber","donut","eclaire"]


statespace = ikea.place_order(order2)

# print(statespace)
# print(info)
# for part in statespace:
#     print("\n")
#     for psu in part:
#         print(psu.get_name()+" | ",end="")





result = simulated_annealing(statespace)

for psu in result:
    print(psu.get_name()+" | ",end="")

# print(result)