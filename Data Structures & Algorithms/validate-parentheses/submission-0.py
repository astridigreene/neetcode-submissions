class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dict_ps = {')': '(', '}': '{', ']': '['}
        
        for i, let in enumerate(s):
            if not bool(stack) or let not in dict_ps:
                stack.append(let)
            elif dict_ps[let] != stack[-1]:
                stack.append(let)
            else:
                stack.pop()
        
        for i, let in enumerate(stack):
            print(let)
        return not bool(stack)