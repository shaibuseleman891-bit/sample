from math import sqrt
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self,width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2*(self.width+self.height)
    def get_diagonal(self):
        return sqrt(self.width**2 + self.height**2)
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        numb_line = ''
        line = '*' * self.width
        for i in range(self.height):
            numb_line += line + "\n"
        return numb_line     
    def get_amount_inside(self, figure_2):
           value = self.get_area() // figure_2.get_area()
           return value
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, side):
        self.width = side
        self.height = side
    def set_height(self,side):
        self.width = side
        self.height = side
    def set_side(self,side):
        self.width = side
        self.height = side 

    def __str__(self):
        return f"Square(side={self.width})"    

print(Rectangle(3, 6).get_area())
print(Rectangle(10, 3).get_picture()) 
print(Rectangle(15,10).get_amount_inside(Square(5)))
print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))