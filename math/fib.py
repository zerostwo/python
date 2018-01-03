
n=input("n=")
n=int(n)
def fib(n):
	a=1
	b=1
	while a<n:
		print(a,end=" ")
		a,b=b,a+b
	print()

fib(n)

