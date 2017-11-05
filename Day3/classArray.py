import random

class Grid:
    def __init__(self, x, y, value = 0,):
        self.xVal = x
        self.yVal = y
        self.value = value

    def __init__(self):
        pass

    def add_xyVals(self, x, y):
        self.xVal = x
        self.yVal = y

    def set_values(self, value):
        self.value = value


grid2d = [[Grid() for i in range(0, 10)] for j in range(0, 10)]

for x in range(0, 10):
    for y in range(0, 10):
        grid2d[x][y].add_xyVals(x, y)
        grid2d[x][y].set_values(random.randint(0, 10))

