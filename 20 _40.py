numbers=[50,40,23,70,56,12,5,10,7]
i=0
sum=0
length=len(numbers)
while i<length:
    a=numbers[i]
    if a>20 and a<40:
        sum=a
    print(a)
    i=i+1
print(sum,"it is less then 40 and greater then 20")    