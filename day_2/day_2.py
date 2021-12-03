



def part_1(lines):

	horizontal, depth = 0, 0

	for line in lines: 

		action, value = line.split()
		value = int(value)

		if action == "forward" :	horizontal += value
		elif action == "down" : depth += value
		elif action == "up" : depth -= value


	print(horizontal * depth)





def part_2(lines):

	depth, horizontal, aim = 0, 0, 0

	for line in lines: 

		action, value = line.split()
		value = int(value)

		if action == "forward" :
			horizontal += value
			depth += aim * value

		elif action == "down" : aim += value
		elif action == "up" : aim -= value


	print(depth * horizontal)

def main():

	with open("input.txt") as file:
		lines = file.read().split("\n")

	part_1(lines)

	part_2(lines)
	

if __name__ == '__main__':
	main()