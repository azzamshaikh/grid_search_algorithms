import matplotlib.pyplot as plt
import numpy as np
from collections import deque


def out_of_bound(idx):
    # Static function to check if the indices for the neighbors are valid
    if 0 <= idx[0] <= 128 and 0 <= idx[1] <= 128:
        return False
    else:
        # print("The following neighbor at " + str(idx) + " is out of bounds.")
        return True


def is_obstacle(idx, grid):
    # Function to check if a cell is an obstacle or not
    if idx in grid:
        return True
    else:
        return False


class GridSearch:
    # GridSearch class is an agent to execute the grid search problem. It contains the information about the
    # initial and goal states, its possible actions, the results of its actions, if it has reached its goal,
    # and any path costs.

    def __init__(self, initial, obs, goal=None):
        # Initialization of GridSearch object
        self.initial = initial
        self.obs = obs
        self.goal = goal

    def action(self, state):
        # Determine any possible actions based on the current state

        possible_actions = ['Up', 'Left', 'Down', 'Right']
        x, y = state[0], state[1]

        # add logic to prevent obstacle and bound collisions
        if out_of_bound((x, y+1)) or is_obstacle((x, y+1), self.obs):
            if 'Up' in possible_actions:
                possible_actions.remove('Up')
        if out_of_bound((x-1, y)) or is_obstacle((x-1, y), self.obs):
            if 'Left' in possible_actions:
                possible_actions.remove('Left')
        if out_of_bound((x, y-1)) or is_obstacle((x, y-1), self.obs):
            if 'Down' in possible_actions:
                possible_actions.remove('Down')
        if out_of_bound((x+1, y)) or is_obstacle((x+1, y), self.obs):
            if 'Right' in possible_actions:
                possible_actions.remove('Right')

        return possible_actions

    def result(self, state, action):
        # Return the resulting new state from the action applied to the current state

        x = state[0]
        y = state[1]
        possible_location = list()

        if action == 'Up':
            possible_location = (x, y+1)
        elif action == 'Left':
            possible_location = (x-1, y)
        elif action == 'Down':
            possible_location = (x, y-1)
        elif action == 'Right':
            possible_location = (x+1, y)

        state = possible_location
        return state

    def goal_test(self, state):
        # Test to see if the current state is the goal state
        if state == self.goal:
            return True
        else:
            return False


class Node:
    # The Node class contains the information about each node/cell that the GridSearch algorithm traverses

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, search):
        # Search neighboring cells
        return [self.child_node(search, action) for action in search.action(self.state)]

    def child_node(self, search, action):
        # Obtain the child node of the current cell
        next_state = search.result(self.state, action)
        next_node = Node(next_state, self, action)
        return next_node

    def solution(self):
        # Return the solution of the path
        return [node.action for node in self.path()[1:]]

    def path(self):
        # Obtain the path back
        node, path_back = self, []
        while node:
            plt.plot(node.state[0], node.state[1], 'ms', markersize=3)
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))


class GridSearchBFS:
    # GridSearchBFS class that executes the BFS grid search

    name = 'Breadth First Search'

    def bfs(search: GridSearch):
        iterations = 0
        node = Node(search.initial)
        if search.goal_test(node.state):
            print("Success! Goal is found at " + str(node.state))
            return node, iterations
        frontier = deque([node])
        explored = {search.initial}
        while frontier:
            node = frontier.pop()
            iterations += 1
            if node.state == search.initial:
                plt.plot(node.state[0], node.state[1], 'bs', markersize=4)
            elif search.goal_test(node.state):
                print('Success! Reached the goal state of ' + str(search.goal))
                plt.pause(0.001)
                plt.plot(node.state[0], node.state[1], 'rs', markersize=4)
                plt.pause(0.001)
                return node, iterations
            else:
                plt.plot(node.state[0], node.state[1], 'gs', markersize=4)
            for child in node.expand(search):
                s = child.state
                if s not in explored:
                    explored.add(s)
                    plt.plot(child.state[0], child.state[1], 'ys', markersize=4)
                    frontier.appendleft(child)
            if iterations % 750 == 0:
                plt.pause(0.01)
                plt.suptitle(GridSearchBFS.name + ' - Number of iterations: ' + str(iterations))
        print('Failed to find goal.')
        return None, iterations


def init_plot():
    # This function initializes the figure object that will contain the obstacle field
    fig, ax = plt.subplots(figsize=(10, 10))                    # Create figure and axis object
    ax.set_xlim([-2, 130])                                      # Set x limit
    ax.set_ylim([-2, 130])                                      # Set y limit
    ax.set_yticks(np.arange(0, 128.1, 1), minor=True)           # Assign minor y-axis ticks
    ax.set_yticks(np.arange(0, 128.1, 128 / 8), minor=False)    # Assign major y-axis ticks
    ax.set_xticks(np.arange(0, 128.1, 1), minor=True)           # Assign minor x-axis ticks
    ax.set_xticks(np.arange(0, 128.1, 128 / 8), minor=False)    # Assign major x-axis ticks


def plot_obstacles(go):
    # This function plots the obstacles into the figure
    idx = go.get_obstacles()                                                        # Get list of obstacles
    for ii in idx:                                                 # Loop through range of obstacles
        plt.plot(ii[0], ii[1], 'sk', markersize=4)      # Plot obstacle


def set_starting_idx(start_idx, go):
    # Set the starting position for the grid. If an obstacle is present, move to another cell.
    start_idx = list(start_idx)
    print("Checking if the following start idx " + str(start_idx) + " is an obstacle.")
    if go.is_obstacle(start_idx):
        print("It is an obstacle. Updating the array")
        start_idx[0] = start_idx[0] + 1
        set_starting_idx(start_idx, go)
    else:
        print("The starting index of " + str(start_idx) + " is valid! Starting at this point!")
    return tuple(start_idx)


def set_goal_idx(goal_idx, go):
    # Set the goal position for the grid. If an obstacle is present, move to another cell.
    goal_idx = list(goal_idx)
    print("Checking if the following goal idx " + str(goal_idx) + " is an obstacle.")
    if go.is_obstacle(goal_idx):
        print("It is an obstacle. Updating the array")
        goal_idx[0] = goal_idx[0] - 1
        set_goal_idx(goal_idx, go)
    else:
        print("The goal index of " + str(goal_idx) + " is valid! Ending at this point!")
    return tuple(goal_idx)


def runBFS(go, startidx, goalidx, rate):
    # Run the BFS algorithm
    init_plot()
    plot_obstacles(go)
    start = set_starting_idx(startidx, go)
    goal = set_goal_idx(goalidx, go)
    gridsearch = GridSearch(start, go.get_obstacles(), goal)
    plt.title('Obstacle Field\nCoverage rate of ' + str(rate) + '%')  # Add plot title
    plt.plot(gridsearch.initial[0], gridsearch.initial[1], 'bs', markersize=4)
    plt.plot(gridsearch.goal[0], gridsearch.goal[1], 'rs', markersize=4)
    plt.pause(1)
    answer, iterations = GridSearchBFS.bfs(gridsearch)
    try:
        answer.solution()
        plt.title('Obstacle Field\nCoverage rate of ' + str(rate) + '%')  # Add plot title
        plt.suptitle(GridSearchBFS.name + ' - Number of iterations: ' + str(iterations))
        plt.pause(0.01)
    except AttributeError:
        print('No solution present.')
    plt.show(block=False)
