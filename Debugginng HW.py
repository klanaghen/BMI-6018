#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Problem 1:
#1a

arg1 = [1,2,3]
arg2 = [1,1,1]

def wrong_add_function(arg1,arg2):
   
   #The function takes in two lists of integers, then it adds
   #all of arg2 to each item of arg1.
   
   #Example:
      wrong_add_function([1,2,3],[1,1,1])
      [6,9,12]

#expected correct answer is, [2,3,4]

arg1 : [1,2,3]
arg2 : [1,1,1]

   #Returns
   #-------
arg1 : list
      #Elements of arg1, with each element having had the contents of 
      #arg2 added to it.

print("1A")

def wrong_add_function(arg1, arg2):
    arg1_index = 0
    while arg1_index < len(arg1):
        arg_2_sum = 0
        for arg2_element in arg2:
            arg_2_sum = sum([arg1[arg1_index] + i for i in arg2])  # sum of arg1 index i and EVERY index i in arg2. that is what is wrong
        print(f' arg 2 sum at index i: {arg_2_sum} this is incorrect') #added f' print statement print the result from each time through the loop
        arg1[arg1_index] = arg_2_sum
        arg1_index += 1
    return arg1

wrong_function = wrong_add_function(arg1, arg2)
print("Incorrect answer:", wrong_function)

arg1 = [1,2,3]
arg2 = [1,1,1]


# In[9]:


#1B
print("1B")

def correct_add_function(arg1, arg2):
    arg1_index = 0
    while arg1_index < len(arg1):
        arg_2_sum = 0
        for arg2_element in arg2:
            arg_2_sum = sum([arg1[arg1_index]] + [arg2[arg1_index]])  #now arg1 index i is getting added to ONLY index i in arg2
        print(f' sum at index i : {arg_2_sum}')
        arg1[arg1_index] = arg_2_sum
        arg1_index += 1
    return arg1

function = correct_add_function(arg1, arg2)
print("Correct Answer:", function)

arg1 = [1,2,3]
arg2 = [1,1,1]


# In[50]:


#Problem 2
#2a
print("Problem 2")

arg1 = ['1','2','3'] #inputs are all strings, a type that will work in the string section of the function 
arg2 = ['1','1','1']

def wrong_add_function2(arg1, arg2):
    # numeric section
    if sum([type(i) == int for i in arg1]) == len(arg1) and \
       sum([type(i) == int for i in arg2]) == len(arg2):        
        print("Numeric section activated.")  # print check if all of the items in the list are integers, this section activates
        arg1_index = 0
        while arg1_index < len(arg1):
            arg_2_sum = sum([arg1[arg1_index]] + [arg2[arg1_index]])
            arg1[arg1_index] = arg_2_sum  
            arg1_index += 1          

    # string section
    elif sum([type(i) == str for i in arg1]) == len(arg1) and \
         sum([type(i) == str for i in arg2]) == len(arg2):
        print("String section activated. Function Successful")  # inserted to make sure that if all indexes within the arg1 and arg2 are strings, this section activates
        arg1_index = 0
        while arg1_index < len(arg1):
            arg_2_sum = [arg1[arg1_index]] + [arg2[arg1_index]]
            arg1[arg1_index] = arg_2_sum
            arg1_index += 1

    else:
        print("Type mismatch detected — entering else section.")
        try:
            for i in arg1:
                if type(i) == int:
                    print("i is int")
        except TypeError as e:
            print("Type mismatch between arg1 and arg2 elements — cannot add these.") #if there is a TypeError, this will print

    return arg1


string_function = wrong_add_function2(arg1, arg2)
print(string_function) #this should return added strings together i.e. ['1''1'], ['2','1']['3','1']

arg_str_1=['1','2','3'] #this is input for second pass through the function
arg_str_2=[4,'1','1']

wrong_add_function2(arg_str_1,arg_str_2) #Calls wrong_add_function2, this should send it through the try/except block to catch the TypeError


# In[ ]:




