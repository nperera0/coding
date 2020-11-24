'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        bracket_dict = {')':'(', '}': '{', ']':'['}

        stack = []
        for bracket in s:
            if bracket in ['(', '{', '[']:
                stack.append(bracket)

            else:
                if len(stack) == 0 or stack.pop() != bracket_dict[bracket]:
                    return False


        if len(stack) == 0:
            return True

        return False
