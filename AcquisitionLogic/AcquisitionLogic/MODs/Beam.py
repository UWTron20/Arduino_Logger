class Beam(object):
    """Describes the Properties of a Beam"""
    def __init__(self, length, width, height, material, elasticModulus, shearModulus, startPoint, endPoint):
        self.length = length
        self.width = width
        self.height = height
        self.material = material
        self.elasticModulus = elasticModulus
        self.shearModulus = shearModulus
        self.startPoint = startPoint
        self.endPoint = endPoint        
