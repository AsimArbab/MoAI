#will contain the methods for objective function and searching

import random as rd

def objective(state, order):
    """
    calculates the value of the objective function of a given state, which is the number of different PSUs used in a state
    :param state: list of PSUs of the length of the order, which contains for every item of the order from which PSU the
     item is taken
    :return: val of the objective function of the given state
    """
    # check if your state takes more pieces of a certain item from a PSU than this PSU contains, if so return worse
    # objective function than for taking each item from another PSU
    for i, psu1 in enumerate(state):
        num = 0
        for j, psu2 in enumerate(state):
            if psu1 == psu2 and order[i] == order[j]:
                num += 1
        if num > psu1.check_for(order[i]):
            return len(state)+1

    #count number of used PSUs in the state
    val = len(state)
    for i in range(len(state)):
        if state[i] in state[i + 1:]:
            val -= 1
    return val


def neighborhood(Warehouse, state, order):
    """
    calculates the neighboorhood of a given state, which are all states with one item taken from another PSU than in the given state
    :param Warehouse: object of the class warehouse
    :param state: list of PSUs of the length of the order, which contains for every item of the order the PSU, that the
     item is taken from
    :param order: list of items that are ordered
    :return: list of all neighbor states of the given state
    """
    neighbors = []
    for i in range(len(state)):
        for j in range(len(Warehouse.look_up(order[i]))):
            #slicing neccessary for really copying the state, not referencing it!
            n = state[:]
            n[i] = Warehouse.look_up(order[i])[j]
            neighbors.append(n)
    return neighbors


def first_choice_hill_climbing(Warehouse, order):
    """
    applies first choice hill climbing to the order and warehouse
    :param Warehouse: object of the class warehouse
    :param order: list of items that are ordered
    :return: tuple of first choice hill climbing best state and its objective function value
    """
    # random initial state
    state = []
    for i in order:
        state.append(rd.choice(Warehouse.look_up(i)))

    val = objective(state, order)

    # take randomly one item from another PSU than in the current state, if the objective function of the neighbor state
    # is equal or better, use that state as current state
    # by testing, 100000 seemed like a good maximum number of steps
    i = 0
    while val > 1 and i < 100000:
        index = rd.randint(0, len(state) - 1)
        # slicing neccessary for really copying the state, not referencing it!
        neighbor = state[:]
        neighbor[index] = rd.choice(Warehouse.look_up(order[index]))
        val_neighbor = objective(neighbor, order)
        if val_neighbor <= val:
            state = neighbor
            val = objective(state, order)
        i += 1

    return state, val

def hill_climbing(Warehouse, order):
    # random initial state
    state = []
    for i in order:
        state.append(rd.choice(Warehouse.look_up(i)))

    val = objective(state, order)

    neighborhood1 = neighborhood(Warehouse, state, order)

    neigh_vals = {}
    for i, neighbor in enumerate(neighborhood1):
        neigh_vals[i] = objective(neighbor, order)

    print(neighborhood1)
    print(neigh_vals)

    return

def local_beam_search(Warehouse):
    return

def simulated_annealing(Warehouse):
    return



