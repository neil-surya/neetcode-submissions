class Solution:
    def isValid(self, s: str) -> bool:
        stack: list = []
        for char in s:
            if char in '({[':
                stack.append(char)
            elif not stack:
                return False
            elif char == ')' and stack.pop() != '(':
                return False
            elif char == '}' and stack.pop() != '{':
                return False
            elif char == ']' and stack.pop() != "[":
                return False 
        if not stack:
            return True
        return False