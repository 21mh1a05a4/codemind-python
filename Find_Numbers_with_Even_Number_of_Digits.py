n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    i=str(i)
    if(len(i)%2==0):
        s+=1
print(s)    