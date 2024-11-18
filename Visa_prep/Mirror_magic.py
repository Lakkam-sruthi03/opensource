n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    print(" ".join(map(str,l[::-1])))
