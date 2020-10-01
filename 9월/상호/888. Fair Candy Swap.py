#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    # Basic solution, traverse the array, but Time Limit Exceeded
    def fairCandySwap(self, A, B):
        sumA = sum(A)
        sumB = sum(B)
        for i in range(len(A)):
            for j in range(len(B)):
                if sumA-A[i]+B[j] == sumB-B[j]+A[i]:
                    return [A[i],B[j]]
                
        return 0
    
 
 
class Solution:
         # Get the difference between the two arrays. Half of this difference is the difference between the elements to be exchanged between the two arrays. Here, a subset of the non-repeating elements of A and B is used as the traversal array, reducing the running time
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        delta = (sum(A)-sum(B)) // 2
        setA = set(A)
        setB = set(B)
        for i in setA:
            if i-delta in setB:
                return [i,i-delta]
        return 0

