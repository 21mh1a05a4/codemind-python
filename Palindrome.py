n=int(input())
s=str(n)
rev=0
while(n!=0):
    r=n%10
    rev=rev*10+r
    n=n//10
t=str(rev)
if(s==t):
    print("True")
else:
    print("False")