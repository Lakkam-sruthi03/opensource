m=input().split()
f=0
if len(m[0])==3 and m[0][0]=='+':
    for i in m[1]:
        if(i.isdigit()):
            f=1
            continue
        else:
            f=0
if f==0:
    print("Incorrect")
else:
    print("Correct")
