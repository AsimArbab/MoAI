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

for part in statespace1:
    print("\n")
    for psu in part:
        print(psu.get_name()+" | ",end="")


statespace2 = [[1,3,6],[1,2,4,5,6],[1,2,3,4,5,6],[5,7],[5,6]]
state = [1,1,1,5,5]


print("\n\n\n")
print(neighbourhood(state, statespace2))

print("\n\n\n")
curr_state = statespace1[:][0]
psu_neighbourhood = neighbourhood((curr_state), statespace1)
for configuration in psu_neighbourhood:
    print("objective function: "+str(objective_function(configuration)))
    for psu in configuration:
        print(psu.get_name(),end=" | ")

print("\n\n\n")


from wh_search import  randomstate

# from wh_search import hill_climbing,first_choice_hill_climbing
#
# result = hill_climbing(statespace2)
# print(result)
#
# result2=first_choice_hill_climbing(statespace2)
# print(result2)

#from wh_search import parallel_hill_climbing
#result3 = parallel_hill_climbing(statespace2,3)

#print(result3)



# def best_neighbour2(neighbourhood, k=3):
#
#     objective_neighbourhood = [[objective_function(state), state] for state in neighbourhood]
#     k_best = sorted(objective_neighbourhood, reverse=True, key=lambda x: x[0])
#     #max = max(objective_neighbourhood, key=lambda x: x[0])
#     sort2 = [[k_best[i][0], k_best[i][1]] for i in range(k)]
#     return sort2

k_current = [randomstate(statespace2) for i in range(3)]

k_hood = []
for k_state in k_current:
    k_hood.extend(neighbourhood(k_state, statespace2))

from wh_search import best_neighbour

k_best_neighbours = best_neighbour(k_hood, 3)
print("best: ",k_best_neighbours)
print("current: ",k_current)


current_vals = [objective_function(k) for k in k_current]
print("current vals:",current_vals)
if any(new_value[0] > current_value for new_value in k_best_neighbours for current_value in current_vals):
    k_new = [neighbour[1] for neighbour in k_best_neighbours]

print("new cureent:",k_new)

print(best_neighbour(k_new))

#from wh_search import local_beam_search
#resultx = local_beam_search(statespace2,3)

#print(resultx)

from wh_search import simulated_annealing

resultv = simulated_annealing(statespace2)
print(resultv)