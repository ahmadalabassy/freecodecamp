# This entrypoint file to be used in development. Start by reading README.md

import prob_calculator
from prob_calculator import Hat, experiment

hat = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
print(hat.draw(5))

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

hat = prob_calculator.Hat(blue=3,red=2,green=6)
probability = prob_calculator.experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)