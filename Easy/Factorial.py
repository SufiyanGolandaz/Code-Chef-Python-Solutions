test=int(input())
for i in range(test):
    n=int(input())
    k=1
    if 5**(k+1)<n:
        n//(5**k)
print(n)