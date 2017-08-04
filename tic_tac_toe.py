

# user_input = input('Give me a number: ')
# print user_input

from random import randint

print randint(0,1)
p = [0, 1]
if randint(0, 1) == 0:
	print 'The player 1 is starting and has the X'
	p[0] = 'X'
	p[1] = 'O'
else:
	print 'The player 2 is starting and has the X'
	p[0] = 'O'
	p[1] = 'X'

coordonates = [0, 1 , 2]
for i in range(3):
	coordonates[i] = [' ' , ' ' , ' ']

def display_board(coordonates):
	for y in range(3):
		line = ''
		for x in range(3):
			line += coordonates[y][x]
			if x < 2:
				line += '|'
		if y > 0 and y < 3:
			print '------'
		print line

def is_complete(coordonates):

	return False

def put_in_board(coordonates, player, user_input):
	print player
	x = user_input[0]
	y = user_input[1]
	if coordonates[y][x] == ' ':
		coordonates[y][x] = player
		return True
	else:
		print 'Error : you can\'t overwrite a player\'s position, try again'
		return False

id_player = 0
while (is_complete(coordonates) == False):
	user_input = input('Hey' + p[id_player] +', what\'s your move ? (x, y)\n')
	if put_in_board(coordonates, p[id_player], user_input) == True:
		if id_player == 0:
			id_player = 1
		elif id_player == 1:
			id_player = 0
	display_board(coordonates)
