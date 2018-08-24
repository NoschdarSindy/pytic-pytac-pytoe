import os, random

noChoice = notOver = True
p = []
marks = ('X','O')
grid = list(range(9))
#The eight winning possibilities - 3 horizontal, 3 vertical and 2 diagonal ones
wins = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#Randomly give the first turn to one of the two players 
turn = random.randint(0,1)
numTurns = 0

"""
Clears the screen and updates the playing field according to the players' set marks
"""
def printGrid():
	os.system('cls') 
	result = ""
	for i, f in enumerate(grid):
		result += " " + (str(f+1) if type(f) is int else f) + (" |" if (i+1) % 3 != 0 else "\n")
	print(result)

print("Welcome to pytic-pytac-pytoe!\nPlease enter your names below.\n")
for i in range(1, 3): p.append(input("Player " + str(i) + ": "))
printGrid()
print(p[turn] + " begins.\nEnter the number you want to set your mark at, then press enter.\n")

while notOver:
	while noChoice:
		try:
			choice = int(input(p[turn] + "'s turn: ")) - 1
		except (ValueError, TypeError):
			choice = -1
		
		if choice in grid:
			noChoice = False
			grid[choice] = marks[turn]
			numTurns += 1
		else:
			print("This choice is not available!")

	printGrid()
	if any([all([grid[w] == marks[turn] for w in win]) for win in wins]): #win
		print(p[turn] + " has won the game. Congratulations!")
		notOver = False
	elif numTurns == 9: #draw
		print("It's a draw!")
		notOver = False
	else: #nothing unusual happened
		turn = not turn
		noChoice = True

input("\nPress Enter to quit.")