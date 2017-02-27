import math
class Pin(object):
    """description of Joint Pin"""
    def __init__(self, diameter, length, elasticModulus, ultimateNormalStress, ultimateShearStress):
        self.diameter = diameter
        self.length = length
        self.elasticModulus = elasticModulus
        self.ultimateNormalStress = ultimateNormalStress
        self.ultimateShearStress = ultimateShearStress

    def getRadius(self):
        return self.diameter / 2

    def changeLength(self, length):
        self.length = length

    def PinShearForce(self, type, coefficientOfForce):
        return self.ultimateShearStress * math.pi * self.diameter * self.diameter * type / (4 * coefficientOfForce)

    def BendingForce(self):
        return self.ultimateNormalStress * math.pi * math.pow(self.getRadius(),3) / (2 * self.length)

