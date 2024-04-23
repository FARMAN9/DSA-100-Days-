def fibonacci(n):
    #Write code here
    if n <= 0:
        return n
    else:
        return ( fibonacci(n-1) + fibonacci(n-2))
        
print(fibonacci(10))    



#memoization

def fibonacci(n):
    #Write code here
     hastable={0:0,1:1}
     
     if n in hastable:
         return hastable[n]
     else:
         hastable[n]=fibonacci(n-1)+fibonacci(n-2)
         return hastable[n]
     
     
print(fibonacci(50))     