######		Battleship Game 	########
##### 		By Krista Parry 	########
##### 	Earnest Data Engineering Challenge #####


Game takes user input from command line for two users to create battleship boards
and then allows users to take turns to fire on opponent's board.


A sample board looks like this, where user provides the following
inputs when prompted:

name:'Cruiser', length=3 at position: (7,2), orientation: v
name:'Battleship', length=4 at position: (2,7), orientation: h
name:'Carrier', length=5 at position: (1,1), orientation: v
name:'Destroyer', length=2 at position: (9,5), orientation: h
name:'Submarine', length=3 at position: (5,8), orientation: v

User board:

	1	2	3	4	5	6	7	8	9	10
	__________________________________________________________________________
1 |	1	0	0	0	0	0	0	0	0	0
  |
2 |	1	0	0	0	0	0	1	1	1	1
  |	
3 |	1	0	0	0	0	0	0	0	0	0
  |
4 |	1	0	0	0	0	0	0	0	0	0
  |	
5 |	1	0	0	0	0	0	0	1	0	0
  |
6 |	0	0	0	0	0	0	0	1	0	0	
  |
7 |	0	1	0	0	0	0	0	1	0	0
  |
8 |	0	1	0	0	0	0	0	0	0	0
  |
9 |	0	1	0	0	1	1	0	0	0	0
  |	
10|	0	0	0	0	0	0	0	0	0	0

##### Game Play and Winning #####

Once each player sets up the board as they wish, the users begin to take turns 
firing a shot at their opponent's board. This is accomplished by selecting the row
and column they would like to fire a hit on.

If a user makes a hit on a ship placed at the provided input, the player is given
another turn. When the player misses, their turn is over. If the user manages to 
comletely sink a ship, a message is displayed, (e.g.):

"User 1 sank User 2's battleship!"

When a player sinks all of their opponent's ships, the player wins.

###### Playing against the computer #######

Computer should use this algorithm for best strategic plays.

http://www.datagenetics.com/blog/december32011/index.html







