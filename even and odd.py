list1=[2,4,23,19,18,17,28,47]
list2=[]
list3=[]
i=0
while i<len(list1):
    m=list1[i]
    if m%2==0:
        list2.append(m)
    else:
        list3.append(m)
    i=i+1
print(list2)
print(list3)