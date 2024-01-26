# ObstacleGenerator.py

import numpy as np


def create_line():
    # Static function to generate a line style tetromino
    # The output is an array containing four (x,y) points
    r = np.random.randint(0, 128)   # Get random row index
    c = np.random.randint(0, 128)   # Get random column index
    start_idx = [r, c]              # Create a starting (x,y) index
    shape_idx = [tuple(start_idx)]         # Create a shape_idx array to store all subsequent indicies to create the desired shape
    heading = np.random.randint(0, 3)  # Direction where 0 is north, 1 is east, 2 is south, 3 is west
    match heading:
        # Based on the heading direction, create appropriate indices per desired shape
        case 0:
            for i in range(1, 4):
                idx = start_idx
                new_idx = [start_idx[0], start_idx[1] + i]
                shape_idx.append(tuple(new_idx))
        case 1:
            for i in range(1, 4):
                idx = start_idx
                new_idx = [start_idx[0] + i, start_idx[1]]
                shape_idx.append(tuple(new_idx))
        case 2:
            for i in range(1, 4):
                idx = start_idx
                new_idx = [start_idx[0], start_idx[1] - i]
                shape_idx.append(tuple(new_idx))
        case 3:
            for i in range(1, 4):
                idx = start_idx
                new_idx = [start_idx[0] - i, start_idx[1]]
                shape_idx.append(tuple(new_idx))
    return shape_idx


def create_l():
    # Static function to generate a L style tetromino
    # The output is an array containing four (x,y) points
    # Refer to comments in the create_line() function for code comments
    r = np.random.randint(0, 128)
    c = np.random.randint(0, 128)
    start_idx = [r, c]
    shape_idx = [tuple(start_idx)]
    heading = np.random.randint(0, 3)  # Direction where 0 is north, 1 is east, 2 is south, 3 is west
    match heading:
        case 0:
            for i in range(1, 4):
                idx = start_idx
                if i == 1:
                    new_idx = [start_idx[0] - i, start_idx[1]]
                else:
                    new_idx = [start_idx[0] - 1, start_idx[1] + (i - 1)]
                shape_idx.append(tuple(new_idx))
        case 1:
            for i in range(1, 4):
                idx = start_idx
                if i == 1:
                    new_idx = [start_idx[0], start_idx[1] + i]
                else:
                    new_idx = [start_idx[0] + (i - 1), start_idx[1] + 1]
                shape_idx.append(tuple(new_idx))
        case 2:
            for i in range(1, 4):
                idx = start_idx
                if i == 1:
                    new_idx = [start_idx[0] + i, start_idx[1]]
                else:
                    new_idx = [start_idx[0] + 1, start_idx[1] - (i - 1)]
                shape_idx.append(tuple(new_idx))
        case 3:
            for i in range(1, 4):
                idx = start_idx
                if i == 1:
                    new_idx = [start_idx[0], start_idx[1] - i]
                else:
                    new_idx = [start_idx[0] - (i - 1), start_idx[1] + 1]
                shape_idx.append(tuple(new_idx))
    return shape_idx


def create_spark():
    # Static function to generate a 'lighting/spark' style tetromino
    # The output is an array containing four (x,y) points
    # Refer to comments in the create_line() function for code comments
    r = np.random.randint(0, 128)
    c = np.random.randint(0, 128)
    start_idx = [r, c]
    shape_idx = [tuple(start_idx)]
    heading = np.random.randint(0, 3)  # Direction where 0 is north, 1 is east, 2 is south, 3 is west
    match heading:
        case 0:
            for i in range(1, 4):
                idx = start_idx
                if i == 1:
                    new_idx = [start_idx[0], start_idx[1] + i]
                elif i == 2:
                    new_idx = [start_idx[0] - (i - 1), start_idx[1] + 1]
                else:
                    new_idx = [start_idx[0] - 1, start_idx[1] + (i - 1)]
                shape_idx.append(tuple(new_idx))
        case 1:
            for i in range(1, 4):
                idx = start_idx
                if i == 1:
                    new_idx = [start_idx[0] + i, start_idx[1]]
                elif i == 2:
                    new_idx = [start_idx[0] + 1, start_idx[1] + (i - 1)]
                else:
                    new_idx = [start_idx[0] + (i - 1), start_idx[1] + 1]
                shape_idx.append(tuple(new_idx))
        case 2:
            for i in range(1, 4):
                idx = start_idx
                if i == 1:
                    new_idx = [start_idx[0], start_idx[1] - i]
                elif i == 2:
                    new_idx = [start_idx[0] + (i - 1), start_idx[1] - 1]
                else:
                    new_idx = [start_idx[0] + 1, start_idx[1] - (i - 1)]
                shape_idx.append(tuple(new_idx))
        case 3:
            for i in range(1, 4):
                idx = start_idx
                if i == 1:
                    new_idx = [start_idx[0] - i, start_idx[1]]
                elif i == 2:
                    new_idx = [start_idx[0] - 1, start_idx[1] - (i - 1)]
                else:
                    new_idx = [start_idx[0] - (i - 1), start_idx[1] - 1]
                shape_idx.append(tuple(new_idx))
    return shape_idx


def create_t():
    # Static function to generate a T style tetromino
    # The output is an array containing four (x,y) points
    # Refer to comments in the create_line() function for code comments
    r = np.random.randint(0, 128)
    c = np.random.randint(0, 128)
    start_idx = [r, c]
    shape_idx = [tuple(start_idx)]
    heading = np.random.randint(0, 3)  # Direction where 0 is north, 1 is east, 2 is south, 3 is west
    match heading:
        case 0:
            for i in range(1, 4):
                idx = start_idx
                if i == 3:
                    new_idx = [start_idx[0] + 1, start_idx[1] - 1]
                else:
                    new_idx = [start_idx[0] + i, start_idx[1]]
                shape_idx.append(tuple(new_idx))
        case 1:
            for i in range(1, 4):
                idx = start_idx
                if i == 3:
                    new_idx = [start_idx[0] - 1, start_idx[1] - 1]
                else:
                    new_idx = [start_idx[0], start_idx[1] - i]
                shape_idx.append(tuple(new_idx))
        case 2:
            for i in range(1, 4):
                idx = start_idx
                if i == 3:
                    new_idx = [start_idx[0] - 1, start_idx[1] + 1]
                else:
                    new_idx = [start_idx[0] - i, start_idx[1]]
                shape_idx.append(tuple(new_idx))
        case 3:
            for i in range(1, 4):
                idx = start_idx
                if i == 3:
                    new_idx = [start_idx[0] + 1, start_idx[1] + 1]
                else:
                    new_idx = [start_idx[0], start_idx[1] + i]
                shape_idx.append(tuple(new_idx))
    return shape_idx


class ObstacleGenerator:
    # This ObstacleGenerator class is used to create random obstacles for the Obstacle Field

    def __init__(self,obs,rate):
        # Class constructor
        self.obs = obs
        self.rate = rate

    def random_obstacle_selector(self):
        # Randomly select a tetromino shape to be generated
        rand = np.random.randint(0, 4)
        match rand:
            case 0:
                self.obs = create_line()
            case 1:
                self.obs = create_l()
            case 2:
                self.obs = create_spark()
            case 3:
                self.obs = create_t()
        return self.obs

    def generate_obstacles(self, go, num_obstacles):
        # Based on the number of obstacles required (input), create a random object
        # The object created will get sent to the GridObstacle class to get checked for collisions and then
        #    get added to the master list of grid obstacles
        for num in range(0, round(num_obstacles / 4)):
            indices = self.random_obstacle_selector()  # Generate obstacle (array of 4 indices are passed)
            go.check_collision_and_add(indices)  # Check if indices are new and then add them to master list
        return go

    def obstacle_coverage(self):
        # This function determines the number of obstacles needed based on the coverage rate input
        total_cells = 128*128
        cells_covered = (self.rate/100)*total_cells
        required_obstacles = cells_covered/4
        return round(required_obstacles)
