import re 
import pandas as pd
import numpy as np
from copy import deepcopy




def part_1(line):

	for _ in range(18):

		for idx in range(len(line)):
			if line[idx] == 0:
				line.append(8)
				line[idx] = 6

			else : 
				line[idx] -= 1

	print(len(line))

visited_states = {}
nb_days = 256
period = 7

def get_generated(init_state, on_day):

	global nb_days

	first_gen  = on_day + init_state + 1

	generated_days = [] 

	cpt = 0

	for day in range(first_gen, nb_days+1, period) :
		generated_days.append(day)
		cpt += 1

	return generated_days

def get_nb_fish(init_state, on_day):
	
	global visited_states

	key = (init_state, on_day)

	if key in visited_states:
		return visited_states[key]

	generated_days = get_generated(init_state, on_day)

	nb = 1
	for day in generated_days:
		result = get_nb_fish(8, day)
		visited_states[(8, day)] = result
		nb += result

	return nb


def part_2(init_states):

	total = 0
	for value in init_states:
		total += get_nb_fish(init_state=value, on_day=0)

	print(total)
		

def main():
	with open("input.txt") as file:
		line = file.read().rstrip().split(",")

	line = [int(i) for i in line]

	part_1(deepcopy(line))
	part_2(deepcopy(line))


if __name__ == "__main__":
	main()