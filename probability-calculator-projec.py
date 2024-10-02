import copy
import random
from typing import Dict
class Hat:
    def __init__(self,**kwargs:Dict[str,int]):
        self.contents=[key  for key in kwargs.keys() for _ in range(kwargs[key])]

    def draw(self, number:int):
        if number > len(self.contents):
            draw_balls =  self.contents[:]
            self.contents.clear()   
            return draw_balls
        else:
            draw_balls = []

            for _ in range(number):
                i_random = random.randint(0,len(self.contents)-1)
                draw_balls.append(self.contents[i_random])
                self.contents.pop(i_random)

            return draw_balls
        



def experiment(hat: Hat, expected_balls: Dict[str,int], num_balls_drawn: int, num_experiments:int):
 
    count=0
    for _ in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        balls_drawn = copy_hat.draw(num_balls_drawn)
                
        for key,value in expected_balls.items():
            if balls_drawn.count(key) < value:
                break
        else:
                count+=1

    return count/num_experiments
    
            
        



