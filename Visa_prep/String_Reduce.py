s=input()
n=[]
c=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1
    else:
        n.append(f"{s[i-1]}{c}")
        c=1
n.append(f"{s[-1]}{c}")
print("".join(n))
