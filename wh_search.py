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

    return len(state)-len(set(state))

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


def first_choice_hill_climbing(statespace):

    return

def hill_climbing(statespace):
    # select random initial state
    current = randomstate(statespace)
    return

def parallel_hill_climbing():
    #look up threads in pyhton
    return

def local_beam_search():
    return
#with lambda

def simulated_annealing():
    return



