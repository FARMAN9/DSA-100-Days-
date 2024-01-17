from array import *
arr=array('i',[1,2,5,7,6,9,3])


def sec_largest(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"
    fmx=arr[0]
    for i in range(len(arr)):
        if(arr[i]>fmx):
            fmx=arr[i]
    smx=arr[0]
    print('Ist',fmx)     
    for i in range(len(arr)):
        if(arr[i]>smx  and arr[i] != fmx ):
            smx=arr[i]
    print('2nd',smx)    
sec_largest(arr)
#O(2n)
#2nd way 
def s2nd(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"
    FMX=SMX=arr[0]
    for i in arr:
        if i>FMX:
            SMX=FMX
            FMX=i
        elif i > SMX and i != FMX:
            SMX = i
    print('IST:',FMX,"\nSEC:",SMX)
s2nd(arr)      
#O(n)