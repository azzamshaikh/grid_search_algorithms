import matplotlib.pyplot as plt
from ObstacleField import generateObstacleField
from GridSearchBFS import runBFS
from GridSearchDFS import runDFS
from GridSearchRandom import runRandom
from GridSearchDijkstra import runDijkstra
import random


def plot_iteration_vs_time(algorithm_data,rate):
    fig, ax = plt.subplots(figsize=(7,7))
    ax.set_ylim([0, 18000])
    plt.xlabel('Time [sec]')
    plt.ylabel('Number of iterations')
    for algorithm in algorithm_data:
        ax.plot(algorithm[0], algorithm[1],marker = 'o', color=color_select(algorithm[2]), label=algorithm[2])
    plt.suptitle('Performance plot comparing number of iterations versus time')
    plt.title('Obstacle Field\nCoverage rate of ' + str(rate) + '%')  # Add plot title
    plt.legend()
    plt.show(block=False)
    plt.pause(0.01)


def color_select(name):
    match name:
        case 'Depth First Search':
            return 'blue'
        case 'Breadth First Search':
            return 'green'
        case 'Dijkstra Search with Diagonal':
            return 'red'
        case 'Dijkstra Search':
            return 'yellow'
        case 'Random Search':
            return 'pink'


def plot_iteration_vs_density(algorithm_data):
    fig, ax = plt.subplots(figsize=(7,7))
    ax.set_ylim([0, 18000])
    plt.xlabel('Density [%]')
    plt.ylabel('Number of iterations')
    for data in algorithm_data:
        for iterations in data[1]:
            ax.plot(data[0], iterations[1], marker = 'o', color=color_select(iterations[2]), label=iterations[2])
    plt.suptitle('Performance plot comparing number of iterations versus obstacle density')
    plt.legend()
    plt.show()


def main():
    # Main function to run planners

    densities = [25, 50, 75]
    num_iterations = list()

    for d in densities:
        go, rate = generateObstacleField(d)        # Create obstacle field objects at a preset density

        plot_data = []

        start_idx = (0, 128)
        goal_idx = (128, 0)

        # Run BFS
        bfs_data = runBFS(go, start_idx, goal_idx, rate)
        plot_data.append(bfs_data)

        # Run DFS
        dfs_data = runDFS(go, start_idx, goal_idx, rate)
        plot_data.append(dfs_data)

        # Run Dijkstra's without diagonal moves
        dijkstra_data = runDijkstra(go, start_idx, goal_idx, rate, False)
        plot_data.append(dijkstra_data)

        # Run Dijkstra's with diagonal moves
        dijkstra_dia_data = runDijkstra(go, start_idx, goal_idx, rate, True)
        plot_data.append(dijkstra_dia_data)

        # Run Random planner
        # rnd_data = runRandom(go, (0, 128), (128, 0), rate)
        # plot_data.append(rnd_data)

        # Create an iteration vs time performance plot
        plot_iteration_vs_time(plot_data,rate)

        num_iterations.append((d, plot_data))

    plot_iteration_vs_density(num_iterations)




if __name__ == "__main__":
    main()  # Runs the script
