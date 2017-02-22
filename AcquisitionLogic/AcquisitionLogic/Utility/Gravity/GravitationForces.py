import numpy as npy
import scipy as spy
from decimal import Decimal as dec

GravitationalConstant = '%.2E' % dec('6.674E-11')

class GravitationForces(object):
    """description of class"""
    def CalculateGravity(ReferenceMass, cc_displacement):
        return GravitationalConstant * ReferenceMass / (cc_displacement * cc_displacement) 
