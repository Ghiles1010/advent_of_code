from copy import deepcopy


def part_1(lines):

	num_bits = len(lines[0])
	infos = [{'0':0, '1':0} for _ in range(num_bits)]

	
	for line in lines:
		idx = 0	
		for bit in line:
			if bit == '0' : infos[idx]['0'] = infos[idx]['0'] + 1
			else :          infos[idx]['1'] = infos[idx]['1'] + 1
			idx += 1

	most_used, least_used = "", ""

	for d in infos:
		if d['0'] > d['1'] : 
			most_used += '0'
			least_used += '1'
		else : 
			most_used += '1'
			least_used += '0'

	result = int(most_used, 2) * int(least_used, 2)
	print(result)



def get_new_lines(lines, infos, chosen, position):

	new_lines = []

	for num in lines:
		if num[position] != chosen:
			for i in range(position+1, len(num)) : 
				infos[i][num[i]]-=1 
		else :
			new_lines.append(num)
			
	return new_lines



def get_result(lines, infos, position, choose_bit):
	if len(lines) == 1 : return int(lines[0], 2)
	chosen = choose_bit(infos[position])
	lines = get_new_lines(lines, infos, chosen, position)
	return get_result(lines, infos, position+1, choose_bit)


def part_2(lines):

	num_bits = len(lines[0])
	infos = [{'0':0, '1':0} for _ in range(num_bits)]

	for line in lines:
		idx = 0	
		for bit in line:
			if bit == '0' : infos[idx]['0'] = infos[idx].get('0', 0) + 1
			else :          infos[idx]['1'] = infos[idx].get('1', 0) + 1
			idx += 1


	choose_co2_bit = lambda info :'1' if info['1'] < info['0'] else '0'
	choose_oxygen_bit = lambda info :'0' if info['0'] > info['1'] else '1'

	oxygen = get_result(deepcopy(lines), deepcopy(infos), 0, choose_oxygen_bit)
	carbon = get_result(deepcopy(lines), deepcopy(infos), 0, choose_co2_bit)

	print(oxygen * carbon)


def main():

	with open("input.txt") as file:
		lines = file.read().rstrip().split("\n")

	part_1(lines)
	part_2(lines)
	

if __name__ == '__main__':
	main()