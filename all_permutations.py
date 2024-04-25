def all_permutations(array):
    perm=[]
    if len(array) == 0:
        perm.append([])
        return perm 
    def helper(array,i):
        if i==len(array)-1:
            perm.append(array[:])
        else:
            for j in range(i,len(array)):
                array[i],array[j]=array[j],array[i]
                helper(array,i+1)
                array[i],array[j]=array[j],array[i]
                
            
         
    helper(array,0)
    return perm

print(all_permutations([0]))


        
    