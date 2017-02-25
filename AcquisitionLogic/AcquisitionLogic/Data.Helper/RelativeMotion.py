import numpy as np

class Particle:
    dispalcement = 0
    velocity = 0
    acceleration = 0
    def __init__(self, displacement, velocity, acceleration):
        self.displacement = displacement
        self.velocity = velocity
        self.acceleration = acceleration
 
    def RelativeDisplacementTo(self, p):
        return self.displacement + p.displacement
