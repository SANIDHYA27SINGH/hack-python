#Finding the largest among 3
#using logic of making 2 checked for 3rd to be greatest or vise-versa

a=int(input("enter a"));
b=int(input("enter b"));
c=int(input("enter c"));
if a>b and a>c:
	print("a is the largest");
elif b>a and b>c:
	print("b is the largest");
else:
	print("c is the largest");
