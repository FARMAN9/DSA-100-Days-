def sorted_squared(array):
    #write code here.make sure to return desired array
    for i in range(len(array)):
       
        array[i]=(array[i])**2
    array=sorted(array)
    return array


array=[1,0,6,7,9,-9]

print(sorted_squared(array))  

"""
Squared Array
Question

You are given an array of Integers in which each subsequent value is not less than the previous value. Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.

Remember

You can solve this question in multiple ways.

Think about the following -

1.What would be the brute force way of solving this question ? What would be the Time and Space complexity of this approach?

2.Is there a better way to solve this with a more optimum Time complexity than the Brute force way ?
"""