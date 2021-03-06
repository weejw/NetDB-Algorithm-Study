class Solution:
    def largestPerimeter(self, A):
        A.sort(reverse=True)
        
        for a , b , c in zip(A, A[1:], A[2:]):
            if b + c > a:
                return a + b + c
        return 0        return 0
        