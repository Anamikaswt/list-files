list1=[1,2,3,4,5,6]
list2=[2,3,0,1,6,7]
i=0
length=len(list1)
while i<length:
    list1=[i]
    if i not in list2:
        print([i])
    i=i+1