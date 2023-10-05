'''Contains functions car_dict and num_sum'''

import math

def car_dict(Model, Make, Color = 'Unknown', Trailer = 'No'):
  '''Takes attributes: (Model, Make, Color, and Trailer) with Model and Make being required, and creates a car dictionary. At the end returns said dictionary as "car".'''
  car = {
      'Model' : Model,
      'Make' : Make,
      'Color' : Color,
      'Trailer' : Trailer
  }
  return car

def num_sum(num1, num2 = math.pi):
  '''Takes two numbers and finds the sum. Returns the sum and a list of given numbers. If not given a second number will use Pi.'''
  sum = num1 + num2
  num_list = [num1, num2]
  return sum, num_list