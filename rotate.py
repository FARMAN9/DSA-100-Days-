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
        
    



Rotate(arr,R)