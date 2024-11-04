
def findI(b,a,i):
    for j in range(len(a)):
        if a[j]==b[i]:
            return j
def inserti(a,val,i):
    nval=a[val]
    for j in range(val,0,-1):
        a[j]=a[j-1]
    a[0]=nval
    return a

a=input('enter the first value:')
b=input('enter the first value:')
count=0
a=list(a)
b=list(b)
for i in range(len(a)):
    if a[i]!=b[i]:
        val=findI(b,a,i)
        a=inserti(a,val,i)
        count+=1
        i=i-1
    print(a)
print(count)