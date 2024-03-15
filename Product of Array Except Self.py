from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length

        # Calculate the product of all elements to the left of each element
        product = 1
        for i in range(length):
            output[i] *= product
            product *= nums[i]

        # Calculate the product of all elements to the right of each element
        product = 1
        for i in range(length - 1, -1, -1):
            output[i] *= product
            product *= nums[i]

        return output