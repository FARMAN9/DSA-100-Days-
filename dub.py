class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()  # Sort the list in place
        print(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:  # Check for duplicate
                return nums[i]


sol = Solution()
sol.findDuplicate([1, 2, 3, 4, 5, 7, 8, 7])


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)+1
        nums.sort()
        for i in range(n):
            if i != nums[i]:
                return i


sol = Solution()
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

# Example usage
sol = Solution()
print(sol.addDigits(38))  # Output: 2
print(sol.addDigits(7))   # Output: 0
