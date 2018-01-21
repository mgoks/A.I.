from collections import deque
import copy


class SixPuzzle:
    initial_state = [['1', '4', '2'], ['5', '3', ' ']]
    goal_state = [[' ', '1', '2'], ['5', '4', '3']]

    @staticmethod
    def get_step_cost(state, action):
        return 1

    def bfs(self):
        root = Node(SixPuzzle.initial_state, None, None, 0)
        if root.is_goal():
            return root.solution()
        frontier = deque([root])
        explored = set()
        while True:
            if not frontier:  # if frontier is empty
                raise Exception('frontier empty')
            node = frontier.popleft()
            explored.add(tuple(node.state[0]) + tuple(node.state[1]))  # because you can't add a list to set
            for action in node.possible_actions():
                child = node.make_child(action)
                if tuple(node.state[0]) + tuple(node.state[1]) not in explored or child.state not in frontier:
                    if child.is_goal():
                        return child.solution()
                    frontier.append(child)


class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def make_child(self, action):
        return Node(
            self.new_state_after(action),
            self,
            action,
            self.path_cost + SixPuzzle.get_step_cost(self.state, action)
        )

    def new_state_after(self, action):
        pos_of_blank = self.get_pos_of_blank()
        row = pos_of_blank[0]
        col = pos_of_blank[1]
        new_state = copy.deepcopy(self.state)
        if action == 'right':
            new_state[row][col] = new_state[row][col + 1]
            new_state[row][col + 1] = ' '
        elif action == 'left':
            new_state[row][col] = new_state[row][col - 1]
            new_state[row][col - 1] = ' '
        elif action == 'up':
            new_state[row][col] = new_state[row - 1][col]
            new_state[row - 1][col] = ' '
        elif action == 'down':
            new_state[row][col] = new_state[row + 1][col]
            new_state[row + 1][col] = ' '
        return new_state

    def get_pos_of_blank(self):
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state[i])):
                if self.state[i][j] == ' ':
                    return i, j

    def possible_actions(self):
        if self.state[0][0] == ' ':
            return ['down', 'right']
        elif self.state[0][1] == ' ':
            return ['left', 'down', 'right']
        elif self.state[0][2] == ' ':
            return ['left', 'down']
        elif self.state[1][0] == ' ':
            return ['up', 'right']
        elif self.state[1][1] == ' ':
            return ['left', 'up', 'right']
        elif self.state[1][2] == ' ':
            return ['left', 'up']

    def solution(self):
        path = [self.state]
        node = self
        while node.parent is not None:
            node = node.parent
            path.append(node.state)
        return path

    def is_goal(self):
        if self.state == SixPuzzle.goal_state:
            return True
        return False


problem = SixPuzzle()
print(problem.bfs())
