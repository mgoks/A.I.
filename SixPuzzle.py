from collections import deque


INITIAL_STATE = (1, 4, 2, 5, 3, 0)
GOAL_STATE = (0, 1, 2, 5, 4, 3)


class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def get_step_cost(self, action):
        return 1

    def is_goal(self):
        return self.state == GOAL_STATE

    def solution(self):
        path = [self.state]
        node = self
        while node.parent is not None:
            node = node.parent
            path.append(node.state)
        path.reverse()
        return path

    def __repr__(self):
        return str(self.state)

    def possible_actions(self):
        """

        :return: a collection of possible actions can be performed on this state (self)
        """
        blank_index = self.state.index(0)
        s = self.state
        actions = []
        if blank_index == 0:
            actions.extend([(s[3], 'D'), (s[1], 'R')])
        elif blank_index == 1:
            actions.extend([(s[0], 'L'), (s[2], 'R'), (s[4], 'D')])
        elif blank_index == 2:
            actions.extend([(s[1], 'L'), (s[5], 'D')])
        elif blank_index == 3:
            actions.extend([(s[0], 'U'), (s[4], 'R')])
        elif blank_index == 4:
            actions.extend([(s[3], 'L'), (s[1], 'U'), (s[5], 'R')])
        elif blank_index == 5:
            actions.extend([(s[4], 'L'), (s[2], 'U')])
        actions.sort()
        just_actions = []
        for each_tuple in actions:
            just_actions.append(each_tuple[1])
        return just_actions

    def child_after(self, action):
        return Node(
            self.new_state_after(action),
            self,
            action,
            self.path_cost + self.get_step_cost(action)
        )

    def new_state_after(self, action):
        blank_index = self.state.index(0)
        if action == 'U':
            return self.swap(blank_index, blank_index - 3)
        elif action == 'D':
            return self.swap(blank_index, blank_index + 3)
        elif action == 'L':
            return self.swap(blank_index, blank_index - 1)
        elif action == 'R':
            return self.swap(blank_index, blank_index + 1)

    def swap(self, blank, other):
        tmp = list(self.state)
        tmp[blank] = self.state[other]
        tmp[other] = 0
        return tuple(tmp)


def bfs():
    root = Node(INITIAL_STATE, None, None, 0)
    if root.is_goal():
        return root.solution()
    frontier = deque([root])
    explored = set()
    while True:
        if not frontier:  # if frontier is empty
            raise Exception('frontier empty')
        node = frontier.popleft()
        explored.add(node.state)
        for action in node.possible_actions():
            child = node.child_after(action)
            if node.state not in explored or child not in frontier:
                if child.is_goal():
                    return child.solution()
                frontier.append(child)


def dfs(node, explored):
    explored.add(node.state)
    if not node.is_goal():
        for each_move in node.possible_actions():
            child = node.child_after(each_move)
            if child.state not in explored:
                dfs(child, explored)
    else:
        print(node.solution())
        return


# path = bfs()
# for each_state in path:
#     print(each_state[0:3])
#     print(each_state[3:])
#     print("")
print(bfs())

r = Node(INITIAL_STATE, None, None, 0)
e = set()
dfs(r, e)
