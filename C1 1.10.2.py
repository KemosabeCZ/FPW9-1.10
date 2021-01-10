class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getSq(self):
        return self.a * self.b

rect1 = Rectangle(4,5)
print ('Ширина =', rect1.getA(), 'Длина =', rect1.getB(), 'Площадь =', rect1.getSq())
