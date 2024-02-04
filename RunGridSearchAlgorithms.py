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
        ax.plot(algorithm[0], algorithm[1],marker = 'o', color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)), label=algorithm[2])
    plt.suptitle('Performance plot comparing number of iterations versus time')
    plt.title('Obstacle Field\nCoverage rate of ' + str(rate) + '%')  # Add plot title
    plt.legend()
    plt.show()


def main():
    # Main function to run planners
    go, rate = generateObstacleField(50)        # Create obstacle field objects at a preset density

    plotdata = []
    # Run BFS
    bfs_data = runBFS(go, (0, 128), (128, 0), rate)
    plotdata.append(bfs_data)

    # Run DFS
    dfs_data = runDFS(go, (0, 128), (128, 0), rate)
    plotdata.append(dfs_data)

    # Run Dijkstra's without diagonal moves
    dijkstra_data = runDijkstra(go, (0, 128), (128, 0), rate, False)
    plotdata.append(dijkstra_data)

    # Run Dijkstra's with diagonal moves
    dijkstra_dia_data = runDijkstra(go, (0, 128), (128, 0), rate, True)
    plotdata.append(dijkstra_dia_data)

    # Run Random planner
    rnd_data = runRandom(go, (0, 128), (128, 0), rate)
    plotdata.append(rnd_data)

    # Create an iteration vs time performance plot
    plot_iteration_vs_time(plotdata,rate)


if __name__ == "__main__":
    main()  # Runs the script
