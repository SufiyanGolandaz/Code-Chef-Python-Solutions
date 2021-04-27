t=int(input())
ans=0
x=0
y=0
for i in range(t):
    x1,y1=input().split()
    x=int(x1) +x
    y=int(y1) +y
    if x>y:
        diff=x-y
        if(diff>=ans):
            ps=1
            ans=diff
    else:
        diff=y-x
        if(diff>=ans):
            ps=2
            ans=diff
print(ps,ans)
