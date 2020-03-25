class Solution:
    def isvalid(self, s):
        stack = []
        dict = {']': '[', ')': '(', '}': '{'}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

    # '{}[]()'
    # def isValid(self, s: str) -> bool:
#     #     d = {'{':'}','[':']','(':')','?':'?'}
#     #     stack = ['?']
#     #     for c in s:
#     #         if c in d.keys():
#     #             stack.append(c)
#     #         elif d[stack.pop()]!=c:
#     #             return False
#     #
