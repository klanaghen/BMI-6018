#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Write a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. 
#This is to be done with a while loop. Note: the input will contain only integers or lists. 

nested_list = [20, 4, 6, [12, 17, [18, 7, 3, 9]]]
current = nested_list

found = True #if there is a deeper list we will keep going
while found:
    found = False  #if there is no deeper nested list, the code turns back around to the last nested list it found
    i = 0          #looks at elements in the current list we are looking into
    while i < len(current): #'i' cannot go further than the length of the list
        if type(current[i]) == list:   # checks if the element it is looking at is a list
            current = current[i]       # if it is a list, then go deeper
            found = True               #if the current list has a deeper list, the outer loop contiunes until it finds the innermost loop where then it goes to "false" in the outer loop
            break                          
        i += 1  #if the element is not a list, move to the next

# At this point, "current" is the innermost list

final_list = [x+1 for x in current] #adding 1 to each element in the innermost list

print(final_list)

