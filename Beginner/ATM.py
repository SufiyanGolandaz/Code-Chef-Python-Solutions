x, y = map(float, input().split())

if x%5!=0 or x+0.5>y: 
    print('{:.2f}'.format(y))
else:
    print('{:.2f}'.format(y-x-0.50))    



