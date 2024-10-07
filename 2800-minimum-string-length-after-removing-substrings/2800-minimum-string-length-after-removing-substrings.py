class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        # Traverse each character in the string
        for char in s:
            if stack:
                # Check for "AB" or "CD" substrings
                if stack[-1] == 'A' and char == 'B':
                    stack.pop()  # Remove "AB"
                elif stack[-1] == 'C' and char == 'D':
                    stack.pop()  # Remove "CD"
                else:
                    stack.append(char)  # No removal, push current char
            else:
                stack.append(char)  # Push the first char
        
        # The size of the stack is the length of the final string
        return len(stack)
