import math
import numpy as np

"""Import Issues so Moved objects into 1 file"""
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


def ThreePointBending(Beam, Pin, Force):
    k1 = Force.strength / (math.pi * Pin.getRadius())
    return k1 * Beam.length

def DoubleShear(Pin, Force):
    k2 = 2 / (math.pi * Pin.diameter * Pin.diameter)
    return k2 * Force.strength

def NormalStress(Beam, Force):
    return Force.strength / (Beam.width * Beam.height)

def BucklingForce(Beam):
    k5 = math.pi * Beam.elasticModulus / 12
    return k5 * (Beam.width * Beam.height * Beam.height * Beam.height / (Beam.length * Beam.length))

def MemberTearing(Beam, Pin, Force):
    k3 = Force.strength / Pin.diameter
    return k3 / Beam.width

def PlateTear(Beam, Force):
    k4 = Force.strength / 2
    return k4 / (Beam.ultimateShearStress * Beam.height)

def MaximumWeight(*args):
    m = 2000000
    for arg in args:
        if(arg < m):
            m = arg
    return m * 2 / 9.81 

def RunDesign():
    C1 = 6.0828
    dowel =  Pin(0.0032, 0.0610, 17000000000, 117000000, 23000000)
    beamBottom = Beam(0.0034, 0.015, 3370000000, np.array([0,0]), np.array([0.3,0]), 2000000, 17100000)
    PinShearForce = dowel.PinShearForce(2, C1)
    RuptureForce = beamBottom.RuptureForce(dowel, C1)
    BucklingForce = beamBottom.BucklingForce(C1)
    dowel.changeLength(0.01)
    BendingForce = dowel.BendingForce()
    TearingForce = beamBottom.TearingForce(0.01, C1)
    BearingForce = beamBottom.BearingForce(C1)
    
    print('Pin Shear: ' + str(PinShearForce))
    print('Rupture: ' + str(RuptureForce))
    print('Buckling: ' + str(BucklingForce))
    print('Bending: ' + str(BendingForce))
    print('Tearing: ' + str(TearingForce))
    print('Bearing: ' + str(BearingForce))

    print('Breaking Force is ' + str(MaximumWeight(PinShearForce, RuptureForce, BucklingForce, BendingForce, TearingForce, BearingForce)))

RunDesign()