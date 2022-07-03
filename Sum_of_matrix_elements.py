n=int(input())
m=int(input())
sum=0
for i in range(n):
    arr=list(map(int,input().split()))
    for j in arr:
        sum+=j
print(sum)        