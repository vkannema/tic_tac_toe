# user_input = input('Give me a number: ')
# print user_input
# name = []
# name[0] = input('Hey, what is the name of the player 1 ?')
# name[1] = input('and what is the name of the player 2 ?')
from random import randint

def reset_game():
	global p
	global coordonates

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
				line += ' | '
		if y > 0 and y < 3:
			print '----------'
		print line

def check_line(coordonates, player):
	for y in range(3):
		x = 1
		if (coordonates[y][x] == player and coordonates[y][x - 1] == player and coordonates[y][x + 1] == player):
			print 'the winner is ' + player
			return True
	return False

def check_column(coordonates, player):
	for x in range(3):
		y = 1
		if (coordonates[y][x] == player and coordonates[y - 1][x] == player and coordonates[y + 1][x] == player):
			print 'the winner is ' + player
			return True
	return False

def check_diag(coordonates, player):
	x = 1
	y = 1
	if coordonates[y][x] == player and coordonates[y - 1][x - 1] == player and coordonates[y + 1][x + 1] == player:
		print 'the winner is ' + player
		return True
	elif coordonates[y][x] == player and coordonates[y + 1][x - 1] == player and coordonates[y - 1][x + 1] == player:
		print 'the winner is ' + player
		return True
	return False

def game_tie(coordonates, player):
	for y in range(3):
		for x in range(3):
			if coordonates[y][x] == ' ':
				return False
	print 'Tie game'
	return True

def is_complete(coordonates, player):
	if check_line(coordonates, player) == True or \
	check_column(coordonates, player) == True or \
	check_diag(coordonates, player) == True or \
	game_tie(coordonates, player) == True:
		return True
	return False

def put_in_board(coordonates, player, user_input):
	x = user_input[0]
	y = user_input[1]
	if x > 2 or y > 2:
		print 'x or y are too high to fit in the board, try again'
		return False
	if coordonates[y][x] == ' ':
		coordonates[y][x] = player
		return True
	else:
		print 'Error : you can\'t overwrite a player\'s position, try again'
		return False

def play_game(coordonates, p):
	id_player = 0
	user_input = None
	while (is_complete(coordonates, p[id_player]) == False):
		user_input = input('Hey' + p[id_player] +', what\'s your move ? (x, y)\n')
		if put_in_board(coordonates, p[id_player], user_input) == True and \
		is_complete(coordonates, p[id_player]) == False:
			if id_player == 0:
				id_player = 1
			elif id_player == 1:
				id_player = 0
		display_board(coordonates)

reset_game()
display_board(coordonates)
play_game(coordonates, p)
rematch = raw_input('Do you want to play again ? y/n\n')
if (rematch == 'y'):
	reset_game()
	play_game(coordonates,p)
else:
	print 'Ok goodbye !'
