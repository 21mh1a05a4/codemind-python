a=input()
a=a.split()
b=''
c=0
for i in a:
    i=str(i)
    d=0
    for j in i:
        if j in 'aeiouAEIOU':
            d+=1
    b+=str(d)
for i in b:
    if i==min(b):
        c+=1
print(c)        
            