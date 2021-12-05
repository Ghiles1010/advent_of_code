

def part_1(lines):

	cpt = 0
	for idx, num in enumerate(lines):
		if idx != 0 and lines[idx] > lines[idx-1]:
			cpt += 1

	print(cpt)



def part_2(lines):

	top = len(lines)
	low, high, cpt = 0, 3, 0

	while(high <= top):
		s = sum(lines[low : high])

		if( low != 0 and  s > previous_sum ):
			cpt += 1

		previous_sum = s
		low += 1
		high += 1


	print(cpt)

def main():
	with open("input.txt") as file:
		lines = file.read().rstrip().split("\n")
	
	lines = [int(i) for i in lines]
	
	part_1(lines)
	part_2(lines)
	
	



if __name__ == "__main__":
	main()
	


	

