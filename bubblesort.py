def Bubble(x):
	count = 0
	for i in range(len(x)-1):
		for j in range(len(x)-1):
			count +=1
			if x[j]>x[j+1]:
				x[j],x[j+1]=x[j+1},x[j]
		print(f"pass{i}:{x}")
		print("count:",count)
x=list(map(int,input("enter:").split())
Bubble(x)
print(x)