class Rectangle:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
    
    def set_width (self, width):
        self.width = width
    
    def set_height (self, height):
        self.height = height
    
    def get_area (self):
        return self.width * self.height
    
    def get_perimeter (self):
        return 2 * self.height + 2 * self.width
    
    def get_diagonal (self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture (self):
        if (self.width > 50 or self.height > 50):
            return "Too big for picture."
        else:
            line = ''
            for i in range (0, self.height):
                for j in range (0, self.width):
                    line += '*'
                line += '\n'
            return line
    
    def get_amount_inside (self, shape):
        area = self.get_area()
        shapeArea = shape.get_area()
        total = 0
        while (area >= shapeArea):
            total += 1
            area -= shapeArea
        return total

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
        



class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width (self, width):
        self.width = width
        self.height = width
    
    def set_height (self, height):
        self.height = height
        self.width = height
    
    def __str__(self):
        return f'Square(side={self.width})'
        
