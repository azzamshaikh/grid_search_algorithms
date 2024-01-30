import matplotlib.pyplot as plt
import numpy as np

from GridObstacle import GridObstacle
from ObstacleGenerator import ObstacleGenerator


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


def generateObstacleField(rate):
    # Main function to run the script
    go = GridObstacle([])                               # Create a GridObstacle object
    obstacle_gen = ObstacleGenerator([],rate)   # Create a ObstacleGenerator object. Initialize with coverage rate
    num_obstacles = obstacle_gen.obstacle_coverage()        # Get number of obstacles based on coverage rate
    go = obstacle_gen.generate_obstacles(go,num_obstacles)  # Generate the obstacles based on the amount required
    return go, rate


def main():
    # Main function to run the script
    for rate in [10, 50, 70]:
        go = GridObstacle([])                               # Create a GridObstacle object
        obstacle_gen = ObstacleGenerator([],rate)   # Create a ObstacleGenerator object. Initialize with coverage rate
        init_plot()                                     # Initialize the figure
        num_obstacles = obstacle_gen.obstacle_coverage()        # Get number of obstacles based on coverage rate
        go = obstacle_gen.generate_obstacles(go,num_obstacles)  # Generate the obstacles based on the amount required
        plot_obstacles(go)                                  # Plot the obstacles
        plt.title('Obstacle Field\nCoverage rate of ' + str(obstacle_gen.rate) + '%')  # Add plot title
        plt.show(block=False)
        plt.pause(0.01)
    plt.show()


if __name__ == "__main__":
    main()  # Runs the script
