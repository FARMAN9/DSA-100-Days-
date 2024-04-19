from array import *
arr=array('i',[1,2,3,4,5,6,7])
R=4
def Rotate(arr,R):
    print("\n Rotate an array \n")
    print("\n Orginal \n")
    print("\n",arr,"\n")
    n=len(arr)
    print("\nlength of array" ,n)
    R=R%n
    arr = arr[R:] + arr[:R]
    print("\nrotated_array", arr)
        
    

#-------------------------calling

Rotate(arr,R)

#__________________________________________________________________

def rotate_array(array,k):
    #write code 
    n=len(array)
    if n==0:
        return array
    print("\nlength of array" ,n)
    k=k%n
    temp=array[-k:]
    for i in reversed(range(len(array)-k)):
        array[i+k]=array[i]
    for i in range(len(temp)):
        array[i]=temp[i]
        
    #array = array[k:] + array[:k]
    #print("\nrotated_array", array)
    
    return array
