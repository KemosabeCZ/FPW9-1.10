class Rectangle:

    def __init__(self, x, y, wid, hei):
        self.x = x
        self.y = y
        self.wid = wid
        self.hei = hei

    def pr(self):
        return (self.x, self.y, self.wid, self.hei)


rect1 = Rectangle(5, 10, 50, 100)
print('Rectangle', rect1.pr())