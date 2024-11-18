n=int(input())
l=list(map(int,input().split()))
ls=0
rs=0
ba=[]
for i in range(n):
    ls=sum(l[:i])
    rs=sum(l[i+1:])
    b=abs(ls-rs)
    ba.append(b)
print(" ".join(map(str,ba)))
