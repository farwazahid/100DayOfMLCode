#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# # Basics

# import numpy as np

# In[12]:


a = np.array([1,2,3], dtype='int16')
print(a)


# In[6]:


b = np.array([[9,5,4],[9,8,5]])
print(b)


# In[8]:


# Get Dimension
a.ndim


# In[9]:


b.ndim


# In[10]:


#Get shape
b.shape


# In[13]:


# Get Type
a.dtype


# In[14]:


b.dtype


# In[15]:


#Get Size
a.itemsize


# In[16]:


b.itemsize


# In[17]:


# Get total size
a.nbytes


# b.nbytes

# # Accessing /Changing specific elements, rows, columns, etc

# a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(a)

# In[21]:


a[1,5]


# In[22]:


a[1,-2]


# In[23]:


a[-2,-2]


# In[24]:


# Get a specific row
a[0,:]


# In[26]:


# Get a specific column
a[:,6]


# In[27]:


# Gettind a little more fancy[startindex:endindex:stepsize]
a[0, 1:6:2]


# In[28]:


a[0, 1:-2:2]


# In[29]:


a[1,5] = 17
print(a)
a[:,2] = 5
print(a)


# In[30]:


b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)


# In[32]:


# get specific element
b[1,0,0]


# In[33]:


b[1,1,1]


# In[34]:


b[0,1,1]


# In[35]:


b[:,1,:]


# In[36]:


b[1,:]


# In[37]:


b[:,0,:]


# In[38]:


b[:,0,:]


# # Initializing different types of Arrays

# In[39]:


# All 0s matrix
np.zeros((2,3))


# In[41]:


np.zeros((3,2,3,1))


# In[47]:


# All 1s matrix
np.ones((3,3,3), dtype = 'float32')


# In[50]:


# Any other name
np.full((2,2), 99)


# In[10]:


a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print (a)


# In[11]:


#Any other number(full_like)
np.full_like(a, 4)


# In[12]:


np.full_like(a.shape, 4)


# In[13]:


np.full(a.shape, 4)


# In[15]:


# Random decimal number
np.random.rand(4,2)


# In[17]:


np.random.rand(3,2,2)


# In[18]:


np.random.rand(3,2,1)


# In[19]:


np.random.random_sample(a.shape)


# In[23]:


np.random.random_sample(2)


# In[21]:


#random integer values
np.random.randint(7, size=(3,3))


# In[24]:


np.random.randint(-7,7, size=(3,3))


# In[25]:


#the identity matrix
np.identity(5)


# In[26]:


arr = np.array([1,2,3])
r1 = np.repeat(arr,3)
print(r1)


# In[27]:


arr = np.array([4,5,6])
r1 = np.repeat(arr,4)
print(r1)


# In[31]:


arr = np.array([4,5,6])
r1 = np.repeat(arr,4,axis =0)
print(r1)


# In[33]:


arr = np.array([[4,5,6]])
r1 = np.repeat(arr,4, axis=0)
print(r1)


# In[44]:


output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:4,1:4] = z
print(output)


# In[50]:


a = np.array([1,2,3])
b = a
b[0] = 100
print(a)
print(b)


# In[49]:


a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print(a)
print(b)


# # Mathematics
# 

# In[52]:


a = np.array([1,2,3,4])
print(a)


# In[53]:


a+2


# In[54]:


a-2


# In[55]:


a*2


# In[56]:


a/2


# In[57]:


b = np.array([1,0,1,0])
a + b 


# In[58]:


a**2


# In[59]:


#Take the sin
np.sin(a)


# In[60]:


#Take the cos
np.cos(a)


# # Linear Algebra
# 

# In[65]:


a = np.ones((2,3))
print(a)

b = np.full((3,2),2)
print(b)

np.matmul(a,b)


# In[68]:


#Find rhe determinantc = np.identity(3)
np.linalg.det(c)


# In[69]:


#Reference docs (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)


# # Statistics

# In[72]:


stats = np.array([[1,2,3],[4,5,6]])
stats


# In[73]:


np.min(stats)


# In[74]:


np.max(stats)


# In[78]:


np.max(stats,axis=1)
#1 means column


# In[79]:


np.max(stats,axis=0)
#0 means row


# # Reorganizing arrays

# In[82]:


before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((8,1))
print(after)


# In[90]:


#vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(v1)
print(v2)

np.vstack([v1,v2])


# In[88]:


# Horizontal stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print(h1)
print(h2)

np.hstack((h1,h2))


# # Miscellaneous

# # Load Data from File

# In[101]:


filedata = np.genfromtxt('data.txt', delimiter=',')



# # Boolen Masking and Indexing

# In[95]:


filedata >50

