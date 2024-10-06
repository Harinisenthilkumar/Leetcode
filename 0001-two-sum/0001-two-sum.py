from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store numbers and their corresponding indices
        num_to_index = {}
        
        for index, num in enumerate(nums):
            # Calculate the difference needed to reach the target
            difference = target - num
            
            # Check if the difference is already in the dictionary
            if difference in num_to_index:
                return [num_to_index[difference], index]  # Return the indices of the two numbers
            
            # Store the current number with its index in the dictionary
            num_to_index[num] = index

# Example usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))        # Output: [1, 2]
print(solution.twoSum([3, 3], 6))           # Output: [0, 1]
