import re 
import pandas as pd
import numpy as np
from copy import deepcopy

def part_1(numbers, tables):

	length, _ = tables[0].shape

	infos = [{'line':{}, 'col':{}} for _ in range(len(tables))]

	for n in numbers:
		for i, t in enumerate(tables):
			index = list(zip(*np.where(t==n)))

			if index:

				line, col = index[0]
				tables[i][line, col] = -1

				infos[i]['line'][line] = infos[i]['line'].get(line, 0) + 1
				infos[i]['col'][col] = infos[i]['col'].get(col, 0) + 1

				if infos[i]['line'][line] == length or infos[i]['col'][col] == length:
					tables[i][tables[i] == -1] = 0
					return tables[i].sum() * n

def part_2(numbers, tables):
	
	length, _ = tables[0].shape

	infos = [{'line':{}, 'col':{}} for _ in range(len(tables))]

	for n in numbers:
		if n == 13 :
			a = 1
			pass
		for i in range(len(tables)-1, -1, -1):
			index = list(zip(*np.where(tables[i]==n)))

			if index:
				line, col = index[0]
				tables[i][line, col] = -1

				infos[i]['line'][line] = infos[i]['line'].get(line, 0) + 1
				infos[i]['col'][col] = infos[i]['col'].get(col, 0) + 1

				if infos[i]['line'][line] == length or infos[i]['col'][col] == length:
					tables[i][tables[i] == -1] = 0
					last_to_win = tables[i]
					l_n = n
					del infos[i]
					del tables[i]

	return last_to_win.sum() * l_n

def tab2mat(table):
	df = pd.DataFrame([t.split() for t in table.split('\n')])
	return df.to_numpy().astype('int32')


def main():
	with open("input.txt") as file:
		tables = file.read().rstrip()

	tables = re.split("\n\n", tables)

	numbers, tables = tables[0].split(','), tables[1:]

	numbers = [int(n) for n in numbers]

	tables = [tab2mat(t) for t in tables]


	print(part_1(numbers, deepcopy(tables)))
	print(part_2(numbers, deepcopy(tables)))

	
	
	



if __name__ == "__main__":
	main()
	


	

