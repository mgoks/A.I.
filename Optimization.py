import math


class Node:
    def __init__(self, state):
        self.state = state
        self.value = f(state)

    def get_highest_valued_successor(self, step_size):
        child1 = Node(self.state + step_size)
        child2 = Node(self.state - step_size)
        if child1.value > child2.value:
            return child1
        else:
            return child2


def f(x):
    return math.sin(math.pow(x, 2) / 2) / math.log(x + 4, 2)


def hill_climbing():
    step_sizes = []
    for i in range(1, 11):
        step_sizes.append(i * 0.01)
    initial_states = []  # starting points X_0
    for i in range(0, 11):
        initial_states.append(i)

    for step_size in step_sizes:
        for initial_state in initial_states:
            current = Node(initial_state)
            n = 0   # number of steps taken to convergence
            while True:
                neighbour = current.get_highest_valued_successor(step_size)
                n += 1
                if neighbour.value <= current.value:
                    print('X_0: ' + str(initial_state) +
                          ', Delta X: ' + str(step_size) +
                          ', final result = P(' + '{0:.2f}'.format(current.state) + ', ' + '{0:.3f}'.format(current.value) + ')' +
                          ', n = ' + str(n) +
                          '')
                    break
                else:
                    current = neighbour
        print("")


hill_climbing()
