x,y=map(int,input().split())
a=(y/100)-x
if a-int(a)>0:
    print(int(a)+1)
else:
    print(int(a))
