import math
from random import random


class Node:
    def __init__(self, state):
        self.state = state
        self.value = f(state)

    def get_highest_valued_successor(self, step_size):
        child1 = Node(self.state + step_size)
        child2 = Node(self.state - step_size)
        if child1.state > 10:
            return child2
        if child2.state < 0:
            return child1
        if child1.value > child2.value:
            return child1
        else:
            return child2

    def get_random_successor(self, step_size):
        random_number = random()
        left_suc = Node(self.state - step_size)
        right_suc = Node(self.state + step_size)
        if left_suc.state < 0:
            return right_suc
        if right_suc.state > 10:
            return left_suc
        if random_number < 0.5:
            return left_suc
        else:
            return right_suc


def f(x):
    return math.sin(math.pow(x, 2) / 2) / math.log(x + 4, 2)


# Starting points X_0
initial_states = []
for i in range(0, 11):
    initial_states.append(i)


def hill_climbing(starting_points):
    step_sizes = []
    for i in range(1, 11):
        step_sizes.append(i * 0.01)
    for step_size in step_sizes:
        print('\\begin{tabular}{||c c c c||} \\hline$X_0$ & $\\Delta X$ & Final result & n \\\\ [0.5ex] \\hline\\hline')
        for initial_state in starting_points:
            current = Node(initial_state)
            n = 0   # number of steps taken to convergence
            while True:
                neighbour = current.get_highest_valued_successor(step_size)
                n += 1
                if neighbour.value <= current.value:
                    print(str(initial_state) + ' & ' +
                          str(step_size) + ' & ' +
                          'P(' + '{0:.2f}'.format(current.state) + ', ' + '{0:.4f}'.format(current.value) + ')' + ' & ' +
                          str(n) + ' \\\\' +
                          # '\n\\hline')
                          '')
                    break
                else:
                    current = neighbour
        print("\end{tabular}\n")


def probability(Delta_E, T):
    random_number = random()    # generates a pseudo-random number between 0 and 1
    return random_number <= math.e**(Delta_E/T)


def simulated_annealing(starting_points):
    step_sizes = (0.01, 0.05, 0.08, 0.09, 0.10)
    for step_size in step_sizes:
        print('\\begin{tabular}{||c c c c||} \\hline$X_0$ & $\\Delta X$ & Final result & $n$ \\\\ [0.5ex] \\hline\\hline')
        for starting_point in starting_points:
            current = Node(starting_point)
            T = 1000
            n = 0
            while True:
                n += 1
                if T == 0:
                    print(str(starting_point) + ' & ' +
                          str(step_size) + ' & ' +
                          'P(' + '{0:.2f}'.format(current.state) + ', ' + '{0:.4f}'.format(current.value) + ') & ' +
                          str(n) + ' \\\\' +
                          '\n\\hline')
                    break
                next_ = current.get_random_successor(step_size)
                Delta_E = next_.value - current.value
                if Delta_E > 0:
                    current = next_
                elif probability(Delta_E, T):
                    current = next_
                T /= 2
        print("\end{tabular}\n")


hill_climbing(initial_states)
simulated_annealing(initial_states)
