from warehouse import Warehouse
from wh_reader import WHreader
from wh_search import neighbourhood
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

# for part in statespace1:
#     print("\n")
#     for psu in part:
#         print(psu.get_name()+" | ",end="")
#
#
statespace2 = [[1,3,6],[1,2,4,5,6],[1,2,3,4,5,6],[5,7],[5,6]]
# state = [1,1,1,5,5]
#
#
# print("\n\n\n")
# print(neighbourhood(state, statespace2))
#
# print("\n\n\n")
# curr_state = statespace1[:][0]
# psu_neighbourhood = neighbourhood((curr_state), statespace1)
# for configuration in psu_neighbourhood:
#     print("objective function: "+str(objective_function(configuration)))
#     for psu in configuration:
#         print(psu.get_name(),end=" | ")
#
# print("\n\n\n")
# print(order2[:][1])
#
# from wh_search import  randomstate
# print(randomstate(statespace2))

# from wh_search import hill_climbing,first_choice_hill_climbing
#
# result = hill_climbing(statespace2)
# print(result)
#
# result2=first_choice_hill_climbing(statespace2)
# print(result2)
#
# from wh_search import parallel_hill_climbing
# result3 = parallel_hill_climbing(statespace2,3)
#
# print(result3)

info1 = WHreader("data/problem1.txt")
ikea1 = Warehouse(info1.get_stock(), info1.get_psus(), "ikea")

statespace3 = ikea1.place_order("data/order12.txt")

# from wh_search import simulated_annealing
# result4 = simulated_annealing(statespace3)
#
# print(result4)

from wh_search import first_choice_hill_climbing
result5 = first_choice_hill_climbing(statespace3)

print(objective_function(result5))