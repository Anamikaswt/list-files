numbers=[50,40,23,70,56,12,5,10,7]
i=0
sum=numbers[i]
length=len(numbers)
while i<length:
    a=numbers[i]
    if a>sum:
        sum=a
    i=i+1
print(sum,"is greater value")