class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ClosetoOpen = {")": "(", "]":"[", "}":"{"}

        for b in s:
            if b in ClosetoOpen:
                if stack and stack[-1] == ClosetoOpen[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b) 

        return True if not stack else False