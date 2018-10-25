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

test = Solution()
print(test.isValid("()"))
        
            