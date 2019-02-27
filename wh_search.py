from random import choice as pickrandom


def neighbourhood(state, statespace):
    """
    Creates a neighbourhood for a state given a statespace. The criterium being that a neighbour is each state
    that can be obtained by changing a single PSU to its possible other values.

    Args:
        state (PSU[]): the current state
        statespace ([PSU[]]): list of possible assignments for each partial state

    Returns:
        [PSU[]]: All configurations of states that statisfy the neigbourhood criterium

    """
    configurations = []
    # will always be <= state_length * possible assignments for each digit O(m*n)
    for index, digit in enumerate(state):
        for assignments in statespace[index]:
            current = state.copy()
            current[index] = assignments
            configurations.append(current)
    # remove the given state from the list afterwards
    while state in configurations:
        configurations.remove(state)

    return configurations


def objective_function(state):
    """
    Decides how good a state is in respect to the objective of using as few PSUs a possible

    Args:
        state (PSU[]): a list of (potentially identical) PSU objects

    Returns:
        int: value of objective function. Minimum of 0 being one PSU per ordered item, and
             Maximum of len(order) being a single PSU for all items

    """

    return len(state) - len(set(state))


def best_neighbour(neighbourhood):
    """
    Returns the best neighbour and its objective value according to the Objective Function

    Args:
        neighbourhood ([PSU[]]): possible configurations of the neighbourhood

    Returns:
        int, PSU[]: highest objective value in the neighbourhood and the corresponding neighbour

    """
    objective_neighbourhood = [objective_function(state) for state in neighbourhood]
    best_val = max(objective_neighbourhood)
    best_index = objective_neighbourhood.index(best_val)
    best_state = neighbourhood[best_index]

    return best_val, best_state


def randomstate(statespace):
    """
    Picks a random possible state from a given statespace

    Args:
        statespace ([PSU[]]): 2-Dimensional state space

    Returns:
        []: randomly chosen state
    """
    randomstate = [pickrandom(possibles) for index, possibles in enumerate(statespace)]
    return randomstate


def first_choice_hill_climbing(statespace, steps=100000):
    current = randomstate(statespace)
    for i in range(steps):
        hood = neighbourhood(current, statespace)
        values = [objective_function(state) for state in hood]
        # instead of the best neighbour, break out of the loop for any neighbour with a higher value
        for index, value in enumerate(values):
            if value > objective_function(current):
                current = hood[index].copy()
                break
    return current


def hill_climbing(statespace, steps=100000):
    current = randomstate(statespace)
    for i in range(steps):
        hood = neighbourhood(current, statespace)
        neighbour = best_neighbour(hood)
        if objective_function(current) < neighbour[0]:
            current = neighbour[1].copy()

    return current


def parallel_hill_climbing(statespace, n, steps=10000):
    candidates = []
    for i in range(n):
        candidates.append((hill_climbing(statespace, steps)))

    winner = best_neighbour(candidates)

    return winner[1]


def local_beam_search(statespace, n, steps=10000):
    candidates = []
   # for i in range(n):
    return



def simulated_annealing(statespace, temperature=1000):
    # linear cooling schedule
    cooling_schedule = lambda t: t-1
    return
