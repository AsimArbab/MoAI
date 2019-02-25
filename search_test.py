from wh_reader import WHreader
from warehouse import Warehouse
from psu import PSU
from wh_search import first_choice_hill_climbing, neighborhood, hill_climbing, objective
import random as rd

#read text file containing warehouse information into a WHreader Object
info = WHreader("data/problem1.txt")

#use the get_stock and get_psus methods of the WHreader Object as input for the Warehouse Object
ikea = Warehouse(stock=info.get_stock(),psus=info.get_psus(), name="ikea")

psu_list = ikea.psus

order_obj = WHreader("data/order11.txt")

order = order_obj.get_stock()

# print(ikea.look_up('magic-tv'))
#
search = first_choice_hill_climbing(ikea, order)
state1 = search[0]
val = search[1]

print(state1)
print(val)
# print(objective(state1))

# state1 = []
# for i in order:
#     state1.append(rd.choice(ikea.look_up(i)))
#
state = [state1[i].get_name() for i in range(len(state1))]
print(state)
val = objective(state)
print(val)
#
# print(state)
# val1 = objective(state)
# print(val)
#
# neighborhood1 = neighborhood(ikea, state1, order)
#
# for i in range(len(neighborhood1)):
#     neighborhood1[i] = [neighborhood1[i][j].get_name()  for j in range(len(neighborhood1[i]))]
# print(neighborhood1)
