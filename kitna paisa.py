kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
i=0
while i<len(kitna_paisa_hai):
    b=kitna_paisa_hai[i]
    if b>=10000000:
        print(a,"-","crorepati")
    elif b>=100000:
        print(a,"-","lakhpati")
    else:
        print(a,"-","dilwale")
    i=i+1