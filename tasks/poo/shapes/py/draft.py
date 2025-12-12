class Shape:

    def getArea(self):
        pass

    def getPerimeter(self):
        pass

    def getName(self):
        pass


class Point2D:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x:.2f}, {self.y:.2f})'
    
class Circle(Shape):

    PI = 3.14159

    def __init__(self, center: Point2D, radius: float):
        self.name = 'Circ'
        self.center = center
        self.radius = radius

    def getName(self):
        return self.name

    def getArea(self):
        return Circle.PI * self.radius * self.radius

    def getPerimeter(self):
        return 2 * Circle.PI * self.radius

    def __str__(self):
        return f'{self.name}: C={self.center}, R={self.radius:.2f}'

class Rectangle(Shape):
    def __init__(self, p1: Point2D, p2: Point2D):
        self.name = 'Rect'
        self.p1 = p1
        self.p2 = p2

    def getName(self):
        return self.name
    
    def getArea(self):
        largura = abs(self.p1.x - self.p2.x)
        altura = abs(self.p1.y - self.p2.y)
        return largura * altura

    def getPerimeter(self):
        largura = abs(self.p1.x - self.p2.x)
        altura = abs(self.p1.y - self.p2.y)
        return 2 * (largura + altura)
    
    def __str__(self):
        return f'{self.name}: P1={self.p1} P2={self.p2}'

def main():
    shapes = []

    while True:
        line = input()
        print('$' + line)
        args = line.split()

        if args[0] == 'end':
            break
        elif args[0] == 'circle':
            x = float(args[1])
            y = float(args[2])
            r = float(args[3])
            shapes.append(Circle(Point2D(x, y), r))
        elif args[0] == 'rect':
            x1 = float(args[1])
            y1 = float(args[2])
            x2 = float(args[3])
            y2 = float(args[4])
            shapes.append(Rectangle(Point2D(x1, y1), Point2D(x2, y2)))
        elif args[0] == 'show':
            for s in shapes:
                print(s)
        elif args[0] == 'info':
            for s in shapes:
                area = s.getArea()
                peri = s.getPerimeter()
                print(f'{s.getName()}: A={area:.2f} P={peri:.2f}')
        else:
            print('error')
main()