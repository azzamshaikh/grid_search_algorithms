import matplotlib.pyplot as plt
import numpy as np

from GridObstacle import GridObstacle
from ObstacleGenerator import ObstacleGenerator
from DepthFirstSearch import DepthFirstSearch


def init_plot():
    # This function initializes the figure object that will contain the obstacle field
    fig, ax = plt.subplots(figsize=(10, 10))                    # Create figure and axis object
    ax.set_xlim([0, 128])                                       # Set x limit
    ax.set_ylim([0, 128])                                       # Set y limit
    ax.set_yticks(np.arange(0, 128.1, 1), minor=True)           # Assign minor y-axis ticks
    ax.set_yticks(np.arange(0, 128.1, 128 / 8), minor=False)    # Assign major y-axis ticks
    ax.set_xticks(np.arange(0, 128.1, 1), minor=True)           # Assign minor x-axis ticks
    ax.set_xticks(np.arange(0, 128.1, 128 / 8), minor=False)    # Assign major x-axis ticks
    return fig, ax


def plot_obstacles(go,axs):
    # This function plots the obstacles into the figure
    idx = go.get_obstacles()                                                        # Get list of obstacles
    for ii in range(go.get_size()):                                                 # Loop through range of obstacles
        axs.scatter([idx[ii][0]], [idx[ii][1]], marker="s", color='red', s=12)      # Plot obstacle
    return axs


def main():
    # Main function to run the script
    go = GridObstacle([])                               # Create a GridObstacle object
    obstacle_gen = ObstacleGenerator([],10)   # Create a ObstacleGenerator object. Initialize with coverage rate
    fig, axs = init_plot()                              # Initialize the figure
    num_obstacles = obstacle_gen.obstacle_coverage()        # Get number of obstacles based on coverage rate
    go = obstacle_gen.generate_obstacles(go,num_obstacles)  # Generate the obstacles based on the amount required
    plot_obstacles(go,axs)                                  # Plot the obstacles
    plt.title('Obstacle Field\nCoverage rate of ' + str(obstacle_gen.rate) + '%') # Add plot title
    #plt.show()                                             # Due to PyCharm backend, this function will show the figure
    dfs = DepthFirstSearch()
    dfs.set_starting_idx(go)
    axs.scatter(dfs.start_idx[0],dfs.start_idx[1])
    plt.show()

if __name__ == "__main__":
    main()  # Runs the script
