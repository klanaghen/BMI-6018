#!/usr/bin/env python
# coding: utf-8

# In[4]:


threshold_list = [4, 19, 54, 34, 9, 26, 14, 72, 6, 21, 85, 10]

def threshold_list(lst, threshold):
    result = []
    for x in lst:
        if x > threshold:
            result.append(x)
    return result

numbers = [4, 19, 54, 34, 9, 26, 14, 72, 6, 21, 85, 10]
threshold = int(input("Enter threshold: "))

filtered = threshold_list(numbers, threshold)
print("Filtered list:", filtered)


# In[ ]:




