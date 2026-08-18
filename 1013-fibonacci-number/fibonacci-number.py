class Solution(object):
    def fib(self, n):
        k=0
        j=1
        f=0
        for i in range(n):
            f=k+j
            k=j
            j=f
        return k



  