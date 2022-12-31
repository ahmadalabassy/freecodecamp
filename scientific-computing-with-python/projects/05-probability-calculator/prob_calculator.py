# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 2022

@author: ahmadalabassy
"""

import copy
import random

class Hat:
    def __init__(self=0, **balls):
        self.contents = [color for color, count in balls.items() for ball in range(count)]
        
    def draw(self, count):
        if count >= len(self.contents):
            temp = copy.copy(self.contents)
            self.contents = []
            return temp
        else:
            return [self.contents.pop(random.randint(0, len(self.contents)-1)) for ball in range(count)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls = expected_balls.items()
    num_matches = 0
    for experiment in range(num_experiments):
        draw = copy.deepcopy(hat).draw(num_balls_drawn)
        does_match = True
        for color, count in expected_balls:
            if draw.count(color) < count:
                does_match = False
                break
        if does_match: num_matches += 1
    return num_matches / num_experiments
