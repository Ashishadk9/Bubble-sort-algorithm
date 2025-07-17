list=[1,4,6,7,6]
sorted= False

while sorted== False:
    num_swaps=0
    for i in range(1,len(list)):
        if list[i-1]>list[i]:
            list[i-1],list[i]=list[i],list[i-1]
            num_swaps = num_swaps + 1
    if num_swaps==0:
        sorted=True
    else:
        sorted=False
    print(list)        
            