#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Write the a python program that, given an input list of any level of complexity/nestedness, 
#will return the inner most list plus 1. 
#This is to be done with recursion. Note: the input will contain only integers or lists. 

recur_list = [20, 4, 6, [12, 17, [18, 7, 3, 9]]]

def find_innermost(lst):
    for item in lst:
        if type(item) == list:  #checking if the item type is a list
            # go deeper into the first sublist
            return find_innermost(item) 
    # if no sublists, this is the innermost
    return lst

innermost = find_innermost(recur_list)

# Now add 1 to each element
innermost = [x + 1 for x in innermost]

print(innermost)   


# In[ ]:




