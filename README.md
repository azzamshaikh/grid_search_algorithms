# Grid Search Algorithms
This repo contains code to implement various grid search algorithms.

Below are a few GIFs of depth first search, breadth first search, and Dijkstra's algorithm in action. 

## Depth First Search

![](./media/DFS.gif)

## Breadth First Search

![](./media/BFS.gif)

## Dijkstra's algorithm

![](./media/Dijkstra.gif)

## Running the Code

To run the code, follow the commands below: 

```
git clone https://github.com/azzamshaikh/grid_search_algorithms.git 
cd grid_search_algorithms
python RunGridSearchAlgorithms.py
```
If an IDE is preferred, such as PyCharm, open the RunGridSearchAlgorithms.py and run the file. 

The different search algorithms can be toggled on and off by commenting the different lines. It is recommended to not run the random planner due to the time required to complete the search.  

The obstacle field density can also be changed. In the RunGridSearchAlgorithms.py, the argument in the following function below defines the obstacle density:

`go, rate = generateObstacleField(50)`

In the case above, 50 refers to the filling 50% of the obstacle field. 