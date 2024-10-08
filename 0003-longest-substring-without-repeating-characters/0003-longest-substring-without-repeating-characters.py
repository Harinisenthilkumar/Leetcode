class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # To store the unique characters
        max_length = 0
        start = 0  # Left pointer for the sliding window
        
        for end in range(len(s)):  # Right pointer for the sliding window
            while s[end] in char_set:
                char_set.remove(s[start])  # Remove the leftmost character
                start += 1  # Move the start pointer to the right
            char_set.add(s[end])  # Add the current character
            max_length = max(max_length, end - start + 1)  # Update the max length
        
        return max_length

# Example usage:
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
