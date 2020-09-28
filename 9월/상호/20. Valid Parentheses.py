#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    def isValid(self, s: str) -> bool:
            
        stack=[]
        d={'(':')','[':']','{':'}'}
        
        for c in s:
            #Characters in the string cannot be modified directly by subscript 
            if len(stack)>0 and c==d.get(stack[-1],'?'):
            #c  ),}, or], the top bracket should be left bracket ([) ()]) is not a valid bracket
                stack.pop()
            else:
                stack.append(c)
              
        return len(stack)==0
            
        


# In[ ]:




