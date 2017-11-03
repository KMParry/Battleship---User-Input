import sys

class board:
	
	def __init__(self,user):
		
		# user can be 1 or 2
		self.user = user
		
		# grid is the users board
		# plays keeps track of the hits and misses
		self.grid = []
		self.plays = []	
	
		# these are user stats on turns
		self.hits = 0
		self.misses = 0
		
		# Check that board is fully occupied. Total of 17 allowed
		self.occupied = 0	
		
		# number of hits against player
		self.num_hit = 0		
		
		# keeps track of the size and hits against each ship
		self.ships_vals = { 'carrier':5 , 'battleship': 4, 'cruiser': 3, 
		'submarine': 3, 'destroyer': 2 } 
	
	def create_board(self):
		self.grid = [[0 for x in range(10)] for y in range(10)]
		self.plays = [[0 for x in range(10)] for y in range(10)]

	def print_board(self):

		print "\n+++++++++++++++ User %d board is as follows +++++++++++++++\n" % self.user
		for i in range(len(self.grid)):
			print self.grid[i]
		#print self.grid	

	def add_hits_and_misses(self,row,col,result):
		
		self.plays[row-1][col-1]=result
		return

	def print_hits_and_misses(self):

		print "\n+++++++++ These are User %d's hits and misses ++++++++"% self.user	
		for i in range(len(self.plays)):
			print self.plays[i]
		#print self.plays

	def print_stats(self):
		print "\n+++++++++++++++ User %d stats are as follows ++++++++++++++++" % self.user
		print "The number of occupied spots: %d" % self.occupied
		print "The number of hits against user %d = %d" % (self.user, self.num_hit)
		print "User %d has made %d hits and %d misses" % (self.user, self.hits, self.misses)
		print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"		

	def check_occupied(self, row, col, direction, size, ship):
		

		if ship == 'carrier':
			symbol = 'c' 
		if ship == 'cruiser':
			symbol = 'r'
		if ship == 'battleship':
			symbol = 'b'
		if ship == 'destroyer':
			symbol = 'd'
		if ship == 'submarine':
			symbol = 's'
		

		# add in the horizontal direction
		if direction == 'h':
			
			if col-1 + size-1 > 9:
				print "Your ship is out of bounds!" 
				return 0

			for j in range(col-1, col-1+size):
				if self.grid[row-1][j] != 0:
					print "This spot (%d, %d) is occupied!" % (row-1,j)
 					return 0
					
			for j in range(col-1, col-1+size):
				self.grid[row-1][j] = symbol
				self.occupied += 1
 			
			return 1

		# add in the vertical direction
		if direction == 'v':

			if row - 1 + size-1 > 9:
				print "Your ship is out of bounds!" 
				return 0
		
			for i in range(row-1, row-1+size):
				if self.grid[i][col-1] != 0:
					print "This spot (%d,%d) is occupied!" % (i, col-1)
 					return 0
			for i in range(row-1, row-1+size):
				self.grid[i][col-1] = symbol
				self.occupied += 1
			return 1


	def add_ships(self):

		print "\n User %d, start adding ships to your grid." % self.user
		print "Choose row and column values between 1 and 10"
		print "and direction 'h' for 'horizontal or 'v' for 'vertical'."

	
		ships = { 'carrier': 5, 'battleship': 4, 'cruiser': 3, 
		'submarine': 3, 'destroyer': 2 } 

		for ship,size in ships.iteritems():
		
			print  "\nFor ship %s with size %d " % (ship, size)
			
			success = 0
			while success < 1:

				# get user input
				try:
					row_guess = int(raw_input("Guess your row "))
					col_guess = int(raw_input("Guess your column "))
				except ValueError:
					print "Value Error. Enter numeric value between (1,10)."
					continue

				direction = str(raw_input("Choose your direction "))

				success=(check_grid_points(row_guess, col_guess) and check_direction(direction) and self.check_occupied(row_guess, col_guess,direction, size,ship))
			
			print "Succesfully added ship %s to (row,column) = (%d, %d) " % (ship, row_guess,col_guess)
		
		if self.occupied == 17:
			print "User %d added all ships succesfully..." % self.user 
			return 1
		else:
			return 0
		

	def take_turns(self,user):

		print "User %d ... it's your turn!" % self.user

		ship = 0

		try:
			row_guess = int(raw_input("Guess your row "))
			col_guess = int(raw_input("Guess your column "))
		except ValueError:
			print "Value Error. Enter numeric value between (1,10)."
			return 1	


		# check input
		if check_grid_points(row_guess, col_guess) == 0:
			print "You are out of bounds!"
			return 1
		
		# check if empty
		if self.grid[row_guess-1][col_guess-1] == 0:	
			print "You missed!"
			self.add_hits_and_misses(row_guess,col_guess,'M')
			self.print_hits_and_misses()
			return 0
		
		# check if this has already been played
		if self.plays[row_guess-1][col_guess-1] == 'H' or self.plays[row_guess-1][col_guess-1] == 'M':	
			print "You already guessed this spot!"
			return 1
		
		if self.grid[row_guess-1][col_guess-1] == 'r':
			ship = 'cruiser'
		if self.grid[row_guess-1][col_guess-1]=='c':
			ship = 'carrier'
		if self.grid[row_guess-1][col_guess-1] == 'b':
			ship = 'battleship'
		if self.grid[row_guess-1][col_guess-1] =='s':
			ship = 'submarine'
		if self.grid[row_guess-1][col_guess-1]=='d':
			ship = 'destroyer'	
		
		# now make a hit
		if ship != 0:	
			
			# decrement count of appropriate ship
			self.ships_vals[ship] -= 1
		
			#check if user sunk the boat
			if self.ships_vals[ship] == 0:
				print "You sunk my %s! Guess again." % ship
			else:
				print "You made a hit! Guess again."
			
			self.hits += 1
			self.grid[row_guess-1][col_guess-1] = -1	
			self.add_hits_and_misses(row_guess,col_guess,'H')
			self.print_hits_and_misses()
			return 1

	
		print "Something is wrong..."
		return -1	
		

	def check_if_winner(self):

		if self.hits == 17:
			print "User %d is a winner!" % self.user
			return 1
		
		return 0
			
	
def check_grid_points(row,col):
	
	
	if row > 10 or row < 1 or col > 10 or col < 1:
		print "You are out of bounds! Choose a row/column value between (1,10)"
		return 0
	
	return 1

def check_direction(direction):
	
	if direction != "h" and direction !="v":
		print "Select an appropriate direction! Choose 'h' or 'v'."
		return 0

	return 1



def main():
	
	user1=board(1)
	user2=board(2)
	
	user1.create_board()
	user2.create_board()

	user1.add_ships()
	user1.print_board()
	
	user2.add_ships()
	user2.print_board()


	turns=0
	winner = 0

	# as long as nobody has won yet, keep alternating turns
	while winner < 1:
		
		if turns%2==0:
			success = 1
			while success > 0:
				success = user1.take_turns(1)
				winner = user1.check_if_winner()
		elif turns%2==1:
			success = 1
			while success > 0:
				success=user2.take_turns(2)
				winner = user2.check_if_winner()
		
		turns+=1
	
		

	
if __name__ == "__main__":

	main()
