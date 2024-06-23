n=10
a=0
b=1
c=a+b
print("Fibonacci Serie : ")

for i in range(n):
    print(a,end=" ")
    a=b
    b=c
    c=a+b