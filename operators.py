from typing import Callable
from math import pow
from random import random

class Operators:
    def __init__(self, gama:float, p:float, alpha: float):
        if p is None:
            p = 1. + random()
        elif p < 1.:
            p = 1.
        if gama is None:
            gama = random()
        elif gama < 0.:
            gama = 0.
        elif gama > 1.:
            gama = 1.
        if alpha is None:
            alpha = random()
        elif alpha < 0.:
            alpha = 0.
        elif alpha > 1.:
            alpha = 1.
        
        self.p = p
        self.alpha = alpha
        self.gama = gama


    def minimum(self, x: float, y: float) -> float:
        return min(x,y)

    def maximum(self, x: float, y: float) -> float:
        return max(x,y)

    def drastic_product(self, x:float, y:float) -> float:
        if(max(x,y) == 1.):
            return min(x,y)
        else:
            return 0.

    def drastic_sum(self, x:float, y:float) -> float:
        if(min(x,y) == 0.):
            return max(x,y)
        else:
            return 1.

    def bounded_difference(self, x:float, y:float) -> float:
        return max(0., x + y - 1.)

    def bounded_sum(self, x:float, y:float) -> float:
        return min(1., x + y)

    def einstein_product(self, x:float, y:float) -> float:
        aux = x * y
        return aux/(2. - x + y - aux)

    def einstein_sum(self, x:float, y:float) -> float:
        return (x + y)/(1. - x * y)

    def hamacher_product(self, x:float, y:float) -> float:
        aux = x * y
        return aux / (x + y - aux)

    def hamacher_sum(self, x:float, y:float) -> float:
        aux = x * y
        return (x + y - 2. * aux)/(1. - aux)
    
    def hamacher_union(self, x:float, y:float) -> float:
        return ((self.gama - 1.) * y + x + y) / (1. + self.gama * x * y)
    
    def yaeger_intersection(self, x:float, y:float) -> float:
        return 1 - min(1, pow(pow(1. - x, self.p) + pow(1. - y, self.p), self.p))
    
    def yaeger_union(self, x:float, y:float) -> float:
        return min(1., pow((x ** self.p + y ** self.p), 1./self.p))
    
    def dubois_prade_intersection(self, x:float, y:float) -> float:
        return (x * y)/(max(x, y, self.alpha))
    
    def union(self, x:float, y:float) -> float:
        return x + y - x * y - min(x, y, 1. - self.alpha)/max(1. - x, 1. - y, self.alpha)
    