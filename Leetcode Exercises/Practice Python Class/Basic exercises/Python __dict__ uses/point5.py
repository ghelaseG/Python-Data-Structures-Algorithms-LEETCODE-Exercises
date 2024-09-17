import math

# optional constructor parameters
class Point(object):

    defaults = {'x': 0, 'y': 0}

    @classmethod
    def set_defaults(cls, **kwargs):
        Point.defaults.update(kwargs)

    def __init__(self, *args): #modified
        self.__dict__.update(Point.defaults)

        keys = list(Point.defaults.keys())
        for i, v in enumerate(args): # copy args to __dict__ in order
            self.__dict__[keys[i]] = v

    def distance(self, other_point):
        return math.hypot(self.x - other_point.x, self.y - other_point.y)
    
    def __repr__(self):
        return str(self.__dict__)
    
def run(): # modified
    p1 = Point(1, 2)
    print(f'p1:{p1}')
    Point.set_defaults(x=99)

    p2 = Point(99)
    print(f'p2:{p2}')

    p3 = Point(3, 4)
    print(f'p2:{p3}')

if __name__ == '__main__':
    run()