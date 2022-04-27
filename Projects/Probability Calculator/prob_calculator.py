import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **data):
        self.contents = list()
        for k, v in data.items():
            for i in range (0, v):
                self.contents.append(k)
    
    def draw(self, x):
        if (x <= len(self.contents)):
            drawed = list()
            self.contents
            for i in range(0, x):
                no = random.randint(0, len(self.contents) - 1)
                drawed.append(self.contents.pop(no))
            drawed.sort()
            return drawed
        else:
            return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    correct = 0
    expectedBalls = list()
    for k, v in expected_balls.items():
        for i in range(0, v):
            expectedBalls.append(k)
    b = expectedBalls

    for i in range(num_experiments):
        copyHat = copy.deepcopy(hat)
        randomList = copyHat.draw(num_balls_drawn)
        if (subsetList(randomList, b.copy())):
            correct += 1
    return correct / num_experiments

def subsetList(list1, list2):
    list1.sort()
    list2.sort()
    count = 0
    length = len(list2)

    for i in list1:
            for j in list2:
                if (i == j):
                    list2.remove(j)
                    count += 1
                    break
    return count == length

