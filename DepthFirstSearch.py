# DepthFirstSearch.py

import matplotlib.pyplot as plt
from collections import deque
import matplotlib.animation as animation

def in_bound(idx):
    # Static function to check if the indices for the neighbors are valid
    if 0 <= idx[0] <= 128 and 0 <= idx[1] <= 128:
        return True
    else:
        print("The following neighbor at " + str(idx) + " is out of bounds.")
        return False


class DepthFirstSearch:
    # This object creates a DepthFirstSearch object that will traverse through the obstacle field
    start_idx = [0,128]
    goal_idx = [128,0]
    stack = deque()
    visited = []
    iterations = 0
    name = "Depth First Search"
    start_color = "purple"
    goal_color = "lime"
    neighbor_color = "orange"
    visited_color = "silver"
    lead_color = "cyan"


    def __init__(self):
        pass

    def set_starting_idx(self,go):
        print("Checking if the following start idx " + str(self.start_idx) + " is an obstacle.")
        if go.is_obstacle(self.start_idx):
            print("It is an obstacle. Updating the array")
            self.start_idx[0] = self.start_idx[0] + 1
            self.set_starting_idx(go)
        else:
            print("The starting index of " + str(self.start_idx) + " is valid! Starting at this point!")

    def set_goal_idx(self,go):
        print("Checking if the following goal idx " + str(self.goal_idx) + " is an obstacle.")
        if go.is_obstacle(self.goal_idx):
            print("It is an obstacle. Updating the array")
            self.goal_idx[0] = self.goal_idx[0] - 1
            self.set_goal_idx(go)
        else:
            print("The goal index of " + str(self.goal_idx) + " is valid! Ending at this point!")

    def mark_visited(self,idx):
        self.visited.append(idx)

    def get_mark_visited(self):
        return self.visited

    def not_visited(self,idx):
        if idx in self.get_mark_visited():
            return False
        else:
            return True


    def collect_neighbors(self,idx,go):
        neighbors = []
        for i in range(0,4):
            if i == 0:
                new_idx = [idx[0] + 1, idx[1]]
                if in_bound(new_idx) and not go.is_obstacle(new_idx):
                    neighbors.append(new_idx)
            if i == 1:
                new_idx = [idx[0], idx[1] + 1]
                if in_bound(new_idx) and not go.is_obstacle(new_idx):
                    neighbors.append(new_idx)
            if i == 2:
                new_idx = [idx[0] - 1, idx[1]]
                if in_bound(new_idx) and not go.is_obstacle(new_idx):
                    neighbors.append(new_idx)
            if i == 3:
                new_idx = [idx[0], idx[1] - 1]
                if in_bound(new_idx) and not go.is_obstacle(new_idx):
                    neighbors.append(new_idx)
        return neighbors

    def DFS(self,go):

        self.stack.append(self.start_idx)
        plt.plot(self.start_idx[0], self.start_idx[1], 'go',markersize = 4)
        # print(len(self.stack))
        self.mark_visited(self.start_idx)
        plt.plot(self.start_idx[0], self.start_idx[1], 'yo', markersize = 4)
        plt.pause(0.1)

        # def animate(i):
        while len(self.stack) != 0:
            # if len(self.stack) == 0:
            #     print("Failed! Couldn't reach ending point!")
            #     ani.event_source.stop()
            self.iterations += 1
            v = self.stack.popleft()
            if v == self.start_idx:
                plt.plot(v[0], v[1], 'go',markersize = 3)
            else:
                plt.plot(v[0], v[1], 'bo',markersize = 3)
            print(v)
            if v == self.goal_idx:
                print("Success! Reached ending point!")
                plt.plot(v[0], v[1], 'go',markersize = 3)
                # ani.event_source.stop()
                break
            # print(len(self.stack))
            neighbors = self.collect_neighbors(v,go)
            # print(neighbors)
            for ii in neighbors:
                # axs.scatter(ii[0], ii[1], color=self.neighbor_color, s=12)
                if self.not_visited(ii):
                    self.stack.append(ii)
                    self.mark_visited(ii)
                    plt.plot(ii[0], ii[1], 'mo',markersize=3)
            # fig.canvas.draw()
            plt.pause(0.0001)

        plt.suptitle(str(self.name) + ' - Number of iterations: ' + str(self.iterations))
        plt.show()


    def workingDFS(self,go,axs):
        # Backup in case function above breaks
        self.stack.append(self.start_idx)
        #print(len(self.stack))
        self.mark_visited(self.start_idx)
        while len(self.stack) != 0:
            self.iterations += 1
            v = self.stack.pop()
            print(v)
            if v == self.goal_idx:
                print("Success! Reached ending point!")
                break
            #print(len(self.stack))
            neighbors = self.collect_neighbors(v,go)
            #print(neighbors)
            for ii in neighbors:
                if self.not_visited(ii):
                    self.stack.append(ii)
                    self.mark_visited(ii)
            #print(len(self.stack))
