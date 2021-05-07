test=int(input())
for i in range(test):
    a=list(map(int,(input().split())))
    a=sorted(a)
    print(a[1])