def mergesort(x):
	if len(x)==0 or len(x)==1:
		return x
	else:
		mid=len(x)//2
		a=mergesort(x[:mid])
		b=mergesort(x[mid:])
		return merge(a,b)