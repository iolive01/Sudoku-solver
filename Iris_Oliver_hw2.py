# Iris Oliver
# Comp 131 HW2
# Sudoku Solver
# Collaborated with: Leah Stern, Cathy Cowell, Ki Ki Chan

#
#	To run this program on both the hard and easy puzzle:
#		 python Iris_Oliver_hw2.py 
#


from __future__ import print_function

# Write a Sudoku puzzle solver using a Constraint Satisfaction Problems 
# approach that can calculate the solution for the puzzle below. 
# Traditional Sudoku is a 9 X 9 puzzle grid made up of nine 3 X 3 regions. 
# Each region, row and column, contains nine cells each. The numbers shown on 
# the board are given and cannot be changed. The object of the puzzle is to 
# place the numbers 1 to 9 in the empty cells so that each row, each column 
# and each 3 X 3 region contains the same number only once. 
Puzzle = [[6, 0, 8, 7, 0, 2, 1, 0, 0], 
		  [4, 0, 0, 0, 1, 0, 0, 0, 2],
		  [0, 2, 5, 4, 0, 0, 0, 0, 0],
		  [7, 0, 1, 0, 8, 0, 4, 0, 5],
		  [0, 8, 0, 0, 0, 0, 0, 7, 0],
		  [5, 0, 9, 0, 6, 0, 3, 0, 1],
		  [0, 0, 0, 0, 0, 6, 7, 5, 0],
   	      [2, 0, 0, 0, 9, 0, 0, 0, 8],
	      [0, 0, 6, 8, 0, 5, 2, 0, 3]]

HardPuzzle = [[0, 7, 0, 0, 4, 2, 0, 0, 0], 
		  	  [0, 0, 0, 0, 0, 8, 6, 1, 0],
		 	  [3, 9, 0, 0, 0, 0, 0, 0, 7],
		  	  [0, 0, 0, 0, 0, 4, 0, 0, 9],
		  	  [0, 0, 3, 0, 0, 0, 7, 0, 0],
			  [5, 0, 0, 1, 0, 0, 0, 0, 0],
			  [8, 0, 0, 0, 0, 0, 0, 7, 6],
   	   	      [0, 5, 4, 8, 0, 0, 0, 0, 0],
	    	  [0, 0, 0, 6, 1, 0, 0, 5, 0]]

# Used to create colors, reference 
# https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Used to print the puzzle with colors and in a grid format
def printPuzzle(puzzle):
	print(color.DARKCYAN, "-----------------------------------", 
			color.END, sep="")

	for i in range(9):
		#print(" || ", end=" ")
		for j in range(9):
			if ((j + 1) % 3 == 0 and j != 8):
				print(color.END, color.BOLD, puzzle[i][j], color.END, 
						color.DARKCYAN, end = " || ", sep="")
			elif (j == 8):
				print(color.END, color.BOLD, puzzle[i][j], color.END, 
						color.DARKCYAN, end ="", sep="")
			else:
				print(color.END, color.BOLD, puzzle[i][j], color.END, 
						color.DARKCYAN, end =" | ", sep="")
			
			#print('hi', end =' ')
		print("")
		if ((i + 1) % 3 == 0 and i != 8):
			print(color.DARKCYAN, "___________________________________", 
					color.END, sep="")
		print(color.DARKCYAN, "-----------------------------------", 
				color.END, sep="")

# Checks if the given variable satisfies horizontal line
def isInRow(currSolution, newNumber, rowNumber):
	for i in range(9):
		if (currSolution[rowNumber][i] == newNumber):
			return True
	return False

# Checks if the given variable satisfies vertical line
def isInCol(currSolution, newNumber, colNumber):
	for i in range(9):
		if (currSolution[i][colNumber] == newNumber):
			return True
	return False

# Checks if the given variable satisfies constraints within a block
def isInBlock(currSolution, newNumber, rowNumber, colNumber):
	# scale to the correct index of the block
	blockRow = (rowNumber / 3) * 3
	blockCol = (colNumber / 3) * 3

	for row in range(blockRow, blockRow + 3):
		for col in range(blockCol, blockCol + 3):
			if (newNumber == currSolution[row][col]):
				return True
	return False

# Finds the next 0 value to be filled, returns -1 if no more 0s remain
def findNextEmpty(currSolution):
	for row in range(9):
		for col in range(9):
			if (currSolution[row][col] == 0):
				return row, col
	return -1, -1

# Counters for the number of backtracks and announcements
backtracks = 0
assignments = 0

# Recursive and backtracking solve function
def solve(currSolution):

	currRow = findNextEmpty(currSolution)[0]
	currCol = findNextEmpty(currSolution)[1]

	if (currRow == -1 or currCol == -1): 
		return currSolution
	else:
		for currNum in range(1,10): # testing all the numbers from 1 - 9
			if((not isInCol(currSolution, currNum, currCol)) and 
			   (not isInRow(currSolution, currNum, currRow)) and
			   (not isInBlock(currSolution, currNum, currRow, currCol))):
				currSolution[currRow][currCol] = currNum
				
				global assignments
				assignments += 1
				result = solve(currSolution)

				if (result != "failure"):
					return currSolution
				currSolution[currRow][currCol] = 0

		global backtracks
		backtracks += 1
		return "failure"

# Running all of the functions
print("Easy Puzzle:")
solve(Puzzle)
print("Number of backtracks:", backtracks)
print("Number of assignments:", assignments)
backtracks = 0		 # reset number of backtracks
assignments = 0	     # reset number of assignments
printPuzzle(Puzzle)

print("Hard Puzzle:")
solve(HardPuzzle)
print("Number of backtracks:", backtracks)
print("Number of assignments:", assignments)
printPuzzle(HardPuzzle)

