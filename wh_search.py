import random as rd



def neighborhood(state, statespace):
    """
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
    """
    # reaches maximum (length of state), if all items are in the same PSU
    return (len(state)+1)-len(set(state))


def first_choice_hill_climbing():
    return

def hill_climbing():
    return

def local_beam_search():
    return

def simulated_annealing():
    return



