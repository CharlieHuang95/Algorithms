# Valid Parentheses

# An expression with valid parentheses is one, that when scanned
# from left to right, has a close brace for each open brace
# (of the same type) before encountering another brace of a
# different type.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_braces = ["(", "{", "["]
        close_braces = {")":"(", "}":"{", "]":"["}
        braces = []
        for c in s:
            if c in open_braces:
                braces.append(c)
            else:
                if not braces or braces.pop() != close_braces[c]:
                    return False
        # if there are any leftover opening braces unaccounted for, then
        # parentheses are not balanced
        if braces:
            return False
        return True
            
