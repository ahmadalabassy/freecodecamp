# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 2022

@author: ahmadalabassy
"""

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50: return "Too big for picture."
        unit_height = ''.join(('*' for w in range(self.width))) + '\n' 
        return ''.join((unit_height for h in range(self.height)))
    
    def get_amount_inside(self, shape):
        return (self.width//shape.width) * (self.height//shape.height)


class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__(side, side)
    
    def __repr__(self):
        return f'Square(side={self.width})'
    
    def set_side(self, side=0):
        super().set_width(side)
        super().set_height(side)
    
    def set_width(self, width=0):
        self.set_side(width)
    
    def set_height(self, height=0):
        self.set_side(height)