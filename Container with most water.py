def max_area(array): #O(n^2)
    area=0
    length = len(array)
    if length==0 or length==1:
        return  area
    for i in range(length):
        for j in range(i+1,length):
            hight=min(array[i],array[j])
            wight=(j-i)
            area=max(area,wight*hight)
    return area





print("Max area",max_area([1,2,1]))



fast O(n)
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        max_area=0
        while i<j:
            h=min(height[i],height[j])
            w= j-i
            max_area=max(max_area,h*w)
            if height[i]<height[j]:
                i+=1
            else:
                j=j-1
                    

        return max_area


if __name__ == "__main__":
    solution = Solution()
    height = [1, 2, 3, 4, 5, 6, 7, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    result = solution.maxArea(height)
    print(result)        
