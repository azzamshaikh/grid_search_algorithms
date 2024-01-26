import matplotlib.pyplot as plt

def out_of_bound(idx):
    # Static function to check if the indices for the neighbors are valid
    if 0 <= idx[0] <= 128 and 0 <= idx[1] <= 128:
        return False
    else:
        #print("The following neighbor at " + str(idx) + " is out of bounds.")
        return True


def is_obstacle(idx,grid):
    # Function to check if a cell is an obstacle or not
    #print(grid)
    #print(idx)

    if idx in grid:
        #print('true')
        return True
    else:
        #print('false')
        return False

class GridSearch:

    def __init__(self,initial,obs,goal=None):
        self.initial = initial
        self.obs = obs
        self.goal = goal

    def action(self,state):
        possible_actions = ['Up','Left','Down','Right']
        x,y = state[0], state[1]

        # add logic to prevent obstacle and bound collisions
        if out_of_bound((x,y+1)) or is_obstacle((x,y+1),self.obs):
            if 'Up' in possible_actions:
                possible_actions.remove('Up')
        if out_of_bound((x-1,y)) or is_obstacle((x-1,y),self.obs):
            if 'Left' in possible_actions:
                possible_actions.remove('Left')
        if out_of_bound((x,y-1)) or is_obstacle((x,y-1),self.obs):
            if 'Down' in possible_actions:
                possible_actions.remove('Down')
        if out_of_bound((x+1,y)) or is_obstacle((x+1,y),self.obs):
            if 'Right' in possible_actions:
                possible_actions.remove('Right')

        return possible_actions


    def result(self,state,action):
        x = state[0]
        y = state[1]
        possible_location = list()

        # Move Up
        if action == 'Up':
            possible_location = (x,y+1)

        elif action == 'Left':
            possible_location = (x-1,y)

        elif action == 'Down':
            possible_location = (x,y-1)

        elif action == 'Right':
            possible_location = (x+1,y)

        state = possible_location

        return state

    def goal_test(self, state):
        if state == self.goal:
            return True
        else:
            return False

class Node:

    def __init__(self,state,parent=None,action=None,path_cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self,search):
        return [self.child_node(search, action) for action in search.action(self.state)]

    def child_node(self,search,action):
        next_state = search.result(self.state,action)
        next_node = Node(next_state,self,action)
        return next_node

    def solution(self,algo_name,coverage_rate,iterations):
        return [node.action for node in self.path(algo_name,coverage_rate,iterations)[1:]]

    def path(self,algo_name,coverage_rate,iterations):
        node, path_back = self, []
        while node:
            plt.plot(node.state[0], node.state[1], 'ms', markersize=3)
            path_back.append(node)
            node = node.parent
        plt.title('Obstacle Field\nCoverage rate of ' + coverage_rate + '%')  # Add plot title
        plt.suptitle(algo_name + ' - Number of iterations: ' + str(iterations))
        plt.pause(0.01)

        return list(reversed(path_back))

    def __hash__(self):
        return hash(self.state)

