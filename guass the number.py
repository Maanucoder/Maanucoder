import random
def gam():
	move=0
	a=int(input("please enter a number"))
	b=int(input("please enter a number"))
	y=random.randint(a,b)
	ans=""
	while True:
			ans=int(input("guss"))
			if ans>y:
			   print("little less")
			   move+=1
			elif ans<y:
			      print("little more")
			      move+=1
			elif ans==y:
			      move+=1
			      print(" you guss correct in move",move)
			      break
			else:
			 	print(" enter a vaild answer")
	return move
print("player 1")
point1=gam()
print("player 2")
point2=gam()
if point2>point1:
		print("player 1 win")
elif point2<point1:
		print("player 2 win")
else:
		print("tie")
		
		