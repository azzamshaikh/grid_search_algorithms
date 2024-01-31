# GridObstacle.py

def in_bound(idx):
    # Static function to check if the indices past from the ObstacleGenerator class are within the bounds of the grid
    if 0 <= idx[0] <= 128 and 0 <= idx[1] <= 128:
        return True
    else:
        print("The following obstacle at " + str(idx) + " is out of bounds.")
        return False


class GridObstacle:
    # This class stores the master list of all obstacle objects

    def __init__(self, obstacles):
        # Class constructor
        self.obstacles = obstacles

    def print_obstacles(self):
        # Function to print all obstacles in the list to the command window
        print(self.obstacles)

    def get_obstacles(self):
        # Getter method to return list of obstacles
        return self.obstacles

    def get_size(self):
        # Getter method to return number of obstacles
        return len(self.obstacles)

    def is_obstacle(self, idx):
        # Function to check if a cell is an obstacle or not
        grid = self.get_obstacles()  # Gets the master list of obstacles
        if idx in grid:
            return True
        else:
            return False

    def add_custom_obs(self, idx):
        # Function to add a custom obstacle (needs to be an array of size 2 or more).
        # Used for checking if planner start point function is working
        self.obstacles.append(idx)

    def check_collision_and_add(self, idx):
        # This function checks if certain obstacles (individual cells) already exist. If they exist, they do not get
        # duplicated to the list
        grid = self.get_obstacles()  # Gets the master list of obstacles
        for obs in idx:              # Loop through new obstacles (a single (x,y) pair)
            if in_bound(obs):        # Only move forward if x,y pair are within grid bounds
                # If the x,y pair is not already in the grid, add it. Otherwise, don't.
                if obs not in grid:
                    self.obstacles.append(obs)
                else:
                    print("The following obstacle at " + str(obs) + " already exists.")
