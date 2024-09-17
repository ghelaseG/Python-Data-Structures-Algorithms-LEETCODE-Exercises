import math

# created template and class method to update it
class Point(object):

    defaults = {'x': 0, 'y': 0} # new

    @classmethod
    def set_defaults(cls, **kwargs): # new method
        Point.defaults.update(kwargs)

    def __init__(self):
        self.__dict__.update(Point.defaults) # new body

    def distance(self, other_point):
        return math.hypot(self.x - other_point.x, self.y - other_point.y)
    
    def __repr__(self): 
        return str(self.__dict__)
    
def run(): # modified
    p1 = Point()
    print(f'p1:{p1}')
    Point.set_defaults(x = 99)

    p2 = Point()
    print(f'p2:{p2}')

    # surprise
    Point.set_defaults(z = 0)
    p3 = Point()
    print(f'p3:{p3}')
    p3.z = 42
    print(f'p3:{p3}')

if __name__ == '__main__':
    run()