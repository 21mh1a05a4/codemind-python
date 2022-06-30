n=int(input())
a=list(map(int,input().split()))
sum=0
a=set(a)
for i in a:
    sum+=i
print(sum)    