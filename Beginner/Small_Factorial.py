def fact(n):
    fact=1
    for j in range(1,n+1):
        fact=fact*j  
    print(fact)
test=int(input())
for i in range(test):
    n=int(input())
    fact(n)