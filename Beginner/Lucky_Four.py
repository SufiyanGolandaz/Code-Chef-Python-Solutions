t=int(input())
for i in range(t):
    n=input()
    count=0
    for j in range(len(n)):
        if int(n[j])==4:
            count+=1
            
    print(count)
         