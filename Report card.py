#part1
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 
i=0
s=0
while i<len(marks):
    m=marks[i]
    a=sum(m)
    s=s+a
    i=i+1
print(s)

#part2

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 
i=0
s=0
marks1=len(marks)
while i<marks1:
    m=marks[i]
    length=len(marks[i])
    a=sum(m)//length
    print(a)
    i=i+1
    