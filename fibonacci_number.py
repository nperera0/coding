
'''
    Fibonacci Number implimentation
    with Memoization

'''
class Solution(object):

    cache = {}
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """

        if N in self.cache:
            return self.cache[N]

        if N < 2:
            return N
        else:
            result = self.fib(N -1) + self.fib(N -2)


        self.cache[N] = result

        return result
