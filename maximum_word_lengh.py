n=input()
x=n.split()
b=[]
for i in x:
    p=str(i)
    q=len(p)
    b+=[q]
c=max(b)
for i in x:
    p=str(i)
    q=len(p)
    if(q==c):
        print(q)
        break