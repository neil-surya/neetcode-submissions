class Solution:
    def maxDepth(self, s: str) -> int:
        maximum = 0
        curr = 0
        for char in s:
            if char == "(":
                curr += 1
            elif char == ")":
                curr -= 1
            maximum = max(maximum, curr)
        return maximum