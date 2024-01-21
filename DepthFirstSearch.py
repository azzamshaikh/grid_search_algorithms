# DepthFirstSearch.py

class DepthFirstSearch:
    # This object creates a DepthFirstSearch object that will traverse through the obstacle field
    start_idx = [0,128]

    def __init__(self):
        pass

    def set_starting_idx(self,go):
        print("Checking if the following start idx " + str(self.start_idx) + " its an obstacle.")
        if go.is_obstacle(self.start_idx):
            print("It is an obstacle. Updating the array")
            self.start_idx[0] = self.start_idx[0] + 1
            self.set_starting_idx(go)
        else:
            print("The starting index of " + str(self.start_idx) + " is valid! Starting at this point!")
