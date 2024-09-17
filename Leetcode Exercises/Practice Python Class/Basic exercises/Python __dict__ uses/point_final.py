import math

# add dynamic object attributes

class Point(object):

    defaults = {'x': 0, 'y': 0}

    @classmethod
    def set_defaults(cls, **kwargs):
        Point.defaults.update(kwargs)

    def __init__(self, *args, **kwargs):
        self.__dict__.update(Point.defaults)

        keys = list(Point.defaults.keys())
        for i, v in enumerate(args): #copy args to __dict__ in order
            self.__dict__[keys[i]] = v

        self.modify_attributes(**kwargs)
    
    def modify_attributes(self, **kwargs):
        self.__dict__.update(kwargs) # new

    def distance(self, other_point):
        return math.hypot(self.x - other_point.x, self.y - other_point.y)
    
    def __repr__(self):
        return str(self.__dict__)
    
def run(): # modified
    p1 = Point(1, 2, z=99, label = 'p1')
    print(p1)
    p1.modify_attributes(z = 88, colour='green')
    print(p1)

if __name__ == '__main__':
    run()