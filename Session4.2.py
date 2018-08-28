
# coding: utf-8

# ## 1.Given a sequence of n values x1, x2, ..., xn and a window size k>0, the k-th moving
# average of the given sequence is defined as follows:
# The moving average sequence has n-k+1 elements as shown below.
# The moving averages with k=4 of a ten-value sequence (n=10) is shown below
# i 1 2 3 4 5 6 7 8 9 10
# ===== == == == == == == == == == ==
# Input 10 20 30 40 50 60 70 80 90 100
# y1 25 = (10+20+30+40)/4
# y2 35 = (20+30+40+50)/4
# y3 45 = (30+40+50+60)/4
# y4 55 = (40+50+60+70)/4
# y5 65 = (50+60+70+80)/4
# y6 75 = (60+70+80+90)/4
# y7 85 = (70+80+90+100)/4
# 
# Thus, the moving average sequence has n-k+1=10-4+1=7 values.

# In[1]:


import numpy as np
def Moving_avg(lst,n):
    
    if n<=0:
        raise ValueError("k must be greater then 0 .")
    elif n > len(lst):
        print("k must be less then or eqaul to length of sequence .")
    else:
        x = np.cumsum(lst, dtype=float) # numpy has feature called cumsum to calculate cumulative sum of given list it will sum 
        # the value with next value and keep the result in same.
        x[n:] = x[n:] - x[:-n] #
        return list(x[n - 1:] / n) # to calulate avrage over the window
        
    


# In[3]:


lst=[3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
Moving_avg(lst,3)


# In[16]:


x1=[1,2,3,4,5,6,7,8,9,10]
x = np.cumsum(x1, dtype=float)
x[3:]

