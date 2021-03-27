binary=[1,0,0,1,1,0,1,1]
exp=0
sum=0
n=7
i=0
length=len(binary)
while i<length:
    m=binary[n]
    exp=(2**i)*m
    i=i+1
    n=n-1
    sum=sum+exp
print(sum)