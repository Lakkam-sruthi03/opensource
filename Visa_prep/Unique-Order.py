n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    if i not in k:
        print(i,end=' ')
        k.append(i)
