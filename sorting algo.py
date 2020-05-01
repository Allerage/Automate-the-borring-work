#!/usr/bin/env python
# coding: utf-8

# In[14]:


#selection sort
import random

j=[7,9,8,0,1,2,4]
l=j.copy()
print(l)
for i in range(len(j)):
    index=i
    for k in range(i+1,len(j)):
        if(j[index]>j[k]):
            index=k
    j[i],j[index]=j[index],j[i]
print(j)    
            


# In[17]:


# insertion sort
j=[7,9,8,0,1,2,4]
for i in range(1,len(j)):
    vs=j[i]
    while j[i-1]>vs and i>0:
        j[i],j[i-1]=j[i-1],j[i]
        i=i-1
print(j)        

        
    
    


# In[24]:


#merge sort
def merge(left,right):
    i,j=0,0
    result=[]
    while(i<len(left) and j<len(right)):
        if(left[i]<=right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:] # append remaning element in left array 
    result+=right[j:]#append remaning element in right array
    return result
def merge_sort(l):
    if (len(l)<=1):
        return l
    else:
        mid=int(len(l)/2)
        left=merge_sort(l[:mid])
        right=merge_sort(l[mid:])
        k=merge(left,right)
        return k
ki=merge_sort([1,2,3,6,3,2,2,-1])
print(ki)


# In[ ]:




