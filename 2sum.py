from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store value-to-index mappings
        value_to_index = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target value
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in value_to_index:
                # If found, return the indices as a list
                return [value_to_index[complement], i]
            
            # Store the current value and its index in the dictionary
            value_to_index[num] = i
        
        # If no valid pair is found, return an empty list (this case should not occur)
        return []



        