n=int(input())
lnum=[]
for i in range(n):
    num=int(input())
    lnum.append(num)      
x=sorted(lnum)         
for i in x:
    print(i)
