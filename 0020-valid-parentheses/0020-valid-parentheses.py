class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in mapping:
                temp = stack.pop() if stack else '#'
                if temp != mapping[i]:
                    return False
            else:
                stack += [i]
        return not stack