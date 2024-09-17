import math

# added __repr__ printing self.__dict__
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return math.hypot(self.x - other_point.x, self.y - other_point.y)
    
    def __repr__(self): return str(self.__dict__) # new

def run():
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    print(f'p1:{p1}  p2:{p2}') # new

    print(f'distance: {p1.distance(p2):.5f}')

if __name__ == '__main__':
    run()