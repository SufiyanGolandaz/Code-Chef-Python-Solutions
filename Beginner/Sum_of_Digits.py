testcase=int(input())
count=0
for i in range(testcase):
    n=int(input())
    y=list(map(int,str(n)))
    for i in y:
        count+=i
    print(count) 
    count=0   