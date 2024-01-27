import matplotlib.pyplot as plt
from ObstacleField import generateObstacleField
from GridSearchBFS import runBFS
from GridSearchDFS import runDFS
from GridSearchRandom import runRandom
from GridSearchDijkstra import runDijkstra



def main():
    go, rate = generateObstacleField(70)
    #runBFS(go,(0,128),(128,0),rate)
    #runDFS(go,(0,128),(128,0),rate)
    #runRandom(go,(0,128),(128,0),rate)
    runDijkstra(go,(0,128),(128,0),rate)
    plt.show()




if __name__ == "__main__":
    main()  # Runs the script