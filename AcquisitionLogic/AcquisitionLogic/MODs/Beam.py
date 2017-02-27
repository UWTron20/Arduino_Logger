import numpy as np
class Beam:
    """Describes the Properties of a Beam"""
    def __init__(self, width, height, elasticModulus, startPoint, endPoint, ultimateShearStress, ultimateNormalStress):
        self.width = width
        self.height = height
        self.elasticModulus = elasticModulus
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.ultimateShearStress = ultimateShearStress
        self.ultimateNormalStress = ultimateNormalStress
        self.beamLength = np.linalg.norm(self.endPoint - self.startPoint)

    def RuptureForce(self, Pin, forceCoefficient):
        length = self.height - Pin.diameter
        return self.ultimateNormalStress * length * self.width / forceCoefficient

    def BucklingForce(self, forceCoefficient):
        return math.pi * math.pi * self.elasticModulus * self.width * math.pow(self.height,3) / (12 * self.beamLength * self.beamLength * forceCoefficient)

    def TearingForce(self, bMin, forceCoefficient):
        return self.ultimateNormalStress * self.width * bMin / forceCoefficient

    def BearingForce(self, forceCoefficient):
        return self.ultimateNormalStress * self.height * self.width / forceCoefficient