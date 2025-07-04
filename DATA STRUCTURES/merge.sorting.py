def mergesort(nlist):
    print("splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]    # left means 1st part , right means 2nd part 
        righthalf = nlist[mid:]     #comparing one part with another

        mergesort(lefthalf)
        mergesort(righthalf)
        i=j=k=0
        while i< len(lefthalf) and j< len(righthalf):
            if lefthalf[i] > righthalf[j]:
                nlist[k] = lefthalf[i]
                i = i + 1
            else:
                nlist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            nlist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            nlist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ",nlist)

nlist = [30 , 50 ,10 , 40 , 20]
mergesort(nlist)
print(nlist)
