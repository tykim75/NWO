n= int(input("n= "))
r=int(input("r= "))
Sum = 1

i=1
for i in range(n,n-r,-1):
    Sum *= i

else:
    print("npr is %d"%Sum)