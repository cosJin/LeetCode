class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==1:return False
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == ")":
                if stack == []:return False 
                elif stack[-1]=="(":
                    stack.pop()
                else:return False
            elif char == "]": 
                if stack == []:return False 
                elif stack[-1]=="[":
                    stack.pop()
                else:return False
            elif char == "}":
                if stack == []:return False 
                elif stack[-1]=="{":
                    stack.pop()
                else:return False
        if stack == []:
            return True
        else:return False
    def isValid(self, s):
        stack = []
        paren_map = {')':'(',']':'[','}':'{',}
        for c in s:
            if c not in paren_map:
                stack.append(c)
            elif not stack or paren_map[c] != stack.pop()
                return False
        return not stack

test = Solution()
print(test.isValid("()"))
        
            