# STACK Question - Nested brackets 
# can we done recursively or using stacks
# keep appending all the elements to the stack until u hit ], after that get the substr, multiply it and push it again

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else: # we encountered ]
                substr = ""
                while stack[-1] != '[':  #we dont get [
                    substr = stack[-1] + substr
                    stack.pop()
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack[-1] + k
                    stack.pop()
                stack.append(int(k) * substr)
        
        return "".join(stack)

        