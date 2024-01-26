import matplotlib.pyplot as plt
import numpy as np

from GridObstacle import GridObstacle
from ObstacleGenerator import ObstacleGenerator
from GridSearch import GridSearch
from GridSearch import Node
from collections import deque

def init_plot():
    # This function initializes the figure object that will contain the obstacle field
    fig, ax = plt.subplots(figsize=(10, 10))                    # Create figure and axis object
    ax.set_xlim([-2, 130])                                       # Set x limit
    ax.set_ylim([-2, 130])                                       # Set y limit
    ax.set_yticks(np.arange(0, 128.1, 1), minor=True)           # Assign minor y-axis ticks
    ax.set_yticks(np.arange(0, 128.1, 128 / 8), minor=False)    # Assign major y-axis ticks
    ax.set_xticks(np.arange(0, 128.1, 1), minor=True)           # Assign minor x-axis ticks
    ax.set_xticks(np.arange(0, 128.1, 128 / 8), minor=False)    # Assign major x-axis ticks


def plot_obstacles(go):
    # This function plots the obstacles into the figure
    idx = go.get_obstacles()                                                        # Get list of obstacles
    for ii in idx:                                                 # Loop through range of obstacles
        plt.plot(ii[0], ii[1], 'sk', markersize=4)      # Plot obstacle


def set_starting_idx(start_idx,go):
    start_idx = list(start_idx)
    print("Checking if the following start idx " + str(start_idx) + " is an obstacle.")
    if go.is_obstacle(start_idx):
        print("It is an obstacle. Updating the array")
        start_idx[0] = start_idx[0] + 1
        set_starting_idx(start_idx,go)
    else:
        print("The starting index of " + str(start_idx) + " is valid! Starting at this point!")
    return tuple(start_idx)


def set_goal_idx(goal_idx,go):
    goal_idx = list(goal_idx)
    print("Checking if the following goal idx " + str(goal_idx) + " is an obstacle.")
    if go.is_obstacle(goal_idx):
        print("It is an obstacle. Updating the array")
        goal_idx[0] = goal_idx[0] - 1
        set_goal_idx(goal_idx,go)
    else:
        print("The goal index of " + str(goal_idx) + " is valid! Ending at this point!")
    return tuple(goal_idx)


def bfs(search):
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
        if iterations % 500 == 0:
            plt.pause(0.001)
    print('Failed to find goal')
    return None, iterations


def main():
    # Main function to run the script
    go = GridObstacle([])                               # Create a GridObstacle object
    obstacle_gen = ObstacleGenerator([],70)   # Create a ObstacleGenerator object. Initialize with coverage rate
    init_plot()                              # Initialize the figure
    num_obstacles = obstacle_gen.obstacle_coverage()        # Get number of obstacles based on coverage rate
    go = obstacle_gen.generate_obstacles(go,num_obstacles)  # Generate the obstacles based on the amount required
    plot_obstacles(go)                                  # Plot the obstacles
    start = set_starting_idx((0,128),go)
    goal = set_goal_idx((128,0),go)
    obstacles = go.get_obstacles()
    gridsearch = GridSearch(start, obstacles, goal)
    plt.plot(gridsearch.initial[0], gridsearch.initial[1], 'bs', markersize=4)
    plt.plot(gridsearch.goal[0], gridsearch.goal[1], 'rs',markersize=4)
    plt.pause(1)
    answer, iterations = bfs(gridsearch)
    answer.solution(str('Breadth First Search'),str(obstacle_gen.rate),iterations)
    plt.show()


if __name__ == "__main__":
    main()  # Runs the script
