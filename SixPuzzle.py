from collections import deque

INITIAL_STATE = (1, 4, 2, 5, 3, 0)
GOAL_STATE = (0, 1, 2, 5, 4, 3)

class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1

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

    def expand(self):
        """
        :return: a collection of successor of this node
        """
        successors = []
        for each_action in self.possible_actions():
            successors.append(self.child_after(each_action))
        return successors


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
            if child.state not in explored and child not in frontier:
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


# Iterative deepening search
def ids():
    depth = 0
    while True:
        result = dls(depth)
        if result != 'cutoff':
            return result
        else:
            depth += 1


# Depth-limited search
def dls(limit):
    return rec_dls(Node(INITIAL_STATE, None, None, 0), limit)


# Recursive depth-limited search
def rec_dls(node, limit):
    cutoff_occurred = False
    if node.is_goal():
        return node.solution()
    elif node.depth == limit:
        return 'cutoff'
    else:
        for each_successor in node.expand():
            result = rec_dls(each_successor, limit)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result != 'failure':
                return result
    if cutoff_occurred:
        return 'cutoff'
    else:
        return 'failure'


print(bfs())

r = Node(INITIAL_STATE, None, None, 0)
e = set()
dfs(r, e)

print(ids())

if bfs() == ids():
    print('BFS and IDS return the same path.')
