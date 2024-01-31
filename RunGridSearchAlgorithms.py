import matplotlib.pyplot as plt
from ObstacleField import generateObstacleField
from GridSearchBFS import runBFS
from GridSearchDFS import runDFS
from GridSearchRandom import runRandom
from GridSearchDijkstra import runDijkstra


def main():
    # Main function to run planners
    go, rate = generateObstacleField(50)        # Create obstacle field objects at a preset density

    # Run BFS
    runBFS(go, (0, 128), (128, 0), rate)

    # Run DFS
    runDFS(go, (0, 128), (128, 0), rate)

    # Run Dijkstra's without diagonal moves
    runDijkstra(go, (0, 128), (128, 0), rate, False)

    # Run Dijkstra's with diagonal moves
    runDijkstra(go, (0, 128), (128, 0), rate, True)

    # Run Random planner
    # runRandom(go, (0, 128), (128, 0), rate)

    plt.show()


if __name__ == "__main__":
    main()  # Runs the script
