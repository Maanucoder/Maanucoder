#import random module
import random
# main function of the game
def game():
	move=0
#range of number is taken input
	a=int(input("please enter a number"))
	b=int(input("please enter a number"))
#genrate a random number in range a and b
	number=random.randint(a,b)
	while True:
			answer=int(input("gauss the number"))
			if answer>number:
			   print("little less")
			   move+=1
			elif answer<number:
			      print("little more")
			      move+=1
			elif answer==number:
			      move+=1
			      print(f"you gauss correct in {move} move" )
			      break
			else:
			 	print(" enter a vaild answer")
#return the move out of the function
	return move
print("player 1")
#take move value inside point1
point1=game()
Take move value inside move 2
print("player 2")
point2=game()
if point2>point1:
		print("...player 1 win...")
elif point2<point1:
		print("...player 2 win...")
else:
		print("....Tie....")
		
		
