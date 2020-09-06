puzzle = [
	[7,8,0,4,0,0,1,2,0],
	[6,0,0,0,7,5,0,0,9],
	[0,0,0,6,0,1,0,7,8],
	[0,0,7,0,4,0,2,6,0],
	[0,0,1,0,5,0,9,3,0],
	[9,0,4,0,6,0,0,0,5],
	[0,7,0,3,0,0,0,1,2],
	[1,2,0,0,0,7,4,0,0],
	[0,4,9,2,0,6,0,0,7]
]

def print_puzzle(puzz):
	for row in range(len(puzz)):
		# Every third row is separated with a dotted line
		if row % 3 == 0 and row != 0:
			print('- - - - - - - - - - - - - -')

		for col in range(len(puzz[0])):
			# Every third coloumn is separate with a line
			if col % 3 == 0:
				print('|', end = ' ')
			# If at the last column, print the number and end it with a line
			if col == 8:
				print(str(puzz[row][col]) + ' | ')
			# If not at the last coloumn, separate each number with a space
			else:
				print(str(puzz[row][col]) + ' ', end = '')

def find_space(puzz):
	# Returns the position of the empty space in the format of (row, column)
	for row in range(len(puzz)):
		for col in range(len(puzz[0])):
			if puzz[row][col] == 0:
				return (row, col)

	# Return nothing if no empty spaces are found
	return None

def is_valid(puzz, number, pos):
	# Check if the inserted number is valid in the row
	for i in range(len(puzz[0])):
		if puzz[pos[0]][i] == number and pos[1] != i:
			return False

	# Check if the inserted number is valid in the column
	for i in range(len(puzz)):
		if puzz[i][pos[1]] == number and pos[0] != i:
			return False

	# Check if the inserted number is valid in the 3x3 square
	# Find which 3x3 square the inserted number is in
	square_x = pos[1] // 3
	square_y = pos[0] // 3

	# Multiplying by 3 to find the correct index and add by 3 to iterate through the square
	for i in range(square_y * 3, square_y * 3 + 3):
		for j in range(square_x * 3, square_x * 3 + 3):
			if puzz[i][j] == number and (i, j) != pos:
				return False

	return True

def solve_puzzle(puzz):
	# Base case: the puzzle contains no empty spaces
	empty = find_space(puzz)
	# Returns true if the board is all filled
	if not empty:
		return True
	else:
		row, col = empty
	
	# Find a valid number between 1-10
	for num in range(1,10):
		if is_valid(puzz, num, (row, col)):
			puzz[row][col] = num

			# Call solve_puzzle again 
			if solve_puzzle(puzz):
				return True
			# If the number is not valid, reset the number to 0
			puzz[row][col] = 0

	# Return false if the number is not valid
	return False

print("Original puzzle")
print_puzzle(puzzle)
print("-----------------------------")
print("Solved puzzle")
solve_puzzle(puzzle)
print_puzzle(puzzle)
