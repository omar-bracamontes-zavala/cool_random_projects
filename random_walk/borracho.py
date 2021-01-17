import random

class Borracho:
    
    def __init__(self,nombre):
        self.nombre=nombre

class BorrachoTradicional(Borracho):

    def __init__(self,nombre):
        super().__init__(nombre)
    
    def camina(self):
        return random.choice([(-1,0),(1,0),(0,1),(0,-1)])

class DrogadoTradicional(Borracho):

    def __init__(self,nombre):
        super().__init__(nombre)
    
    def camina(self):
        return random.choice([
            (random.random()*-1,0),
            (random.random()* 1,0),
            (0,random.random()* 1),
            (0,random.random()*-1),
            (random.random()*-1,random.random()*1),
            (random.random()*-1,random.random()*-1),
            (random.random()*1,random.random()*-1),
            (random.random()*1,random.random()*1)
            ])