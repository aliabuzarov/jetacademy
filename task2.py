start=int(input())
end=int(input())
for i in range(start,end):
    s=0
    for j in range(1,i):
        if i%j==0:
            s+=1
    if s==1:
        print(i)