import math

class Point(object):

    defaults = {'x': 0, 'y': 0} # new

    def __init__(self):
        self.__dict__.update(Point.defaults) # new body

    def distance(self, other_point):
        return math.hypot(self.x - other_point.x, self.y - other_point.y)

    def __repr__(self): return str(self.__dict__)


def run(): #modified
    p1 = Point()
    print(f'p1: {p1}')
    print(p1.x)

if __name__ == '__main__':
    run() 