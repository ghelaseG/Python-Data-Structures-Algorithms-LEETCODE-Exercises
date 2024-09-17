import math

# basic point class

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return math.hypot(self.x - other_point.x, self.y - other_point.y)
    
def run():
    p1 = Point(1, 2)
    p2 = Point(2, 3)

    print(f'distance: {p1.distance(p2):.5f}')

if __name__ == '__main__':
    run()