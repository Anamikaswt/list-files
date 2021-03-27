numbers=[50,40,23,70,56,12,5,10,7]
i=0
sum=numbers[i]
while i<len(numbers):
    a=numbers[i]
    if a>sum:
        sum=a
    i=i+1
    while i<len(numbers):
        b=numbers[i]
        if b>a:
            b=a
        i=i+1
    print(b,"is second smallest value")