import re 
import pandas as pd
import numpy as np
from copy import deepcopy


def is_hvd(coords):
	x1, y1, x2, y2 = coords
	if x1 == x2 or y1 == y2 : return 'hv'
	if abs(x2-x1) == abs(y2-y1) : return 'd'
	return None
	


def get_points(coords, allignement):
	x1, y1, x2, y2 = coords

	if allignement == 'hv':
		if x1 == x2:
			if y1 > y2 : y2, y1 = y1, y2
			return [(x1, i) for i in range(y1, y2+1)]

		if y1 == y2:
			if x1 > x2 : x2, x1 = x1, x2
			return [(i, y1) for i in range(x1, x2+1)]

	if allignement == 'd':

		points = []

		p_x = 1 if x2 > x1 else -1 
		p_y = 1 if y2 > y1 else -1 

		x, y = x1, y1
		while(x!=x2 and y!=y2):
			
			points.append((x,y))
			x+=p_x
			y+=p_y

		points.append((x,y))

		return points

def part_1(coord_list):

	infos = {}

	for coords in coord_list:
		if is_hvd(coords) == 'hv':
			
			for point in get_points(coords, 'hv'):
				infos[point] = infos.get(point, 0) + 1
	
	cpt = 0
	for point in infos:
		if infos[point] >= 2 : cpt+=1

	print(cpt)


def part_2(coord_list):
	infos = {}

	for coords in coord_list:
		
		allignement = is_hvd(coords)
		if allignement :
			for point in get_points(coords, allignement):
				infos[point] = infos.get(point, 0) + 1
	
	cpt = 0

	for point in infos:
		if infos[point] >= 2 : cpt+=1

	print(cpt)

def main():
	with open("input.txt") as file:
		lines = file.read().rstrip().split("\n")

	coord_list = [[int(x) for x in re.split(",| -> ", line)] for line in lines]

	part_1(coord_list)
	part_2(coord_list)


if __name__ == "__main__":
	main()
	


	

