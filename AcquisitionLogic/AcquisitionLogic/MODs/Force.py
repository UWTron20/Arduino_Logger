class Force(object):
    """Describes the properties and functionality of force vectors"""
    
    def __init__(self, strength, vector, displacement):
        self.strength = strength
        self.vector = vector
        self.displacement = displacement

    def CalculateMomentum(self, point):
        return self*point

def AddForces(*argv):
    resultant = 0
    for arg in argv:
        resultant = resultant + arg
    return resultant

def SubtractForces(*argv):
    resultant = 0
    for arg in argv:
        resultant = resultant - arg
    return resultant

