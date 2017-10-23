# Fizz Buzz

# A very popular interview question. Output numbers from 1 to n,
# but output Fizz if number is divisible by 3, and Buzz is number
# is divisible by 5

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for num in range(1, n+1):
            s = ""
            if num % 3 == 0:
                s += "Fizz"
            if num % 5 == 0:
                s += "Buzz"
            if not s:
                s = str(num)
            l.append(s)
        return l
