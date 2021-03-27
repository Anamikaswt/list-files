name=["annu","kritika","pooja","dhanu"]
name1=["annu","kritika","tannu","siddhi"]
i=0
while i<len(name1):
    m= name1[i]
    if m  not in name:
        name.append(m)
    i=i+1
print(name)