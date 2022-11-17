import math

def paint(height, width, coverage):
	area = height * width
	num_of_cans = math.ceil(area/coverage)
	print(f"We need {num_of_cans} can of paints")

height = int(input())  
width = int(input())
coverage = int(input())
paint(height, width, coverage)