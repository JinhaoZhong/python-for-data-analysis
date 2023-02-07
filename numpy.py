import numpy as np
a=np.array([100,2,3,4,5,6,7,8,9,10]) # set array
print(a)
print(a[1]) #print sec element: 2
print(a.size) # size of array: 10
print(a.ndim) # num of dimension: 1
print(a.shape) #shows the num of element in each dim: (10,)
print(type(a))# type of a: numpy.ndarray
print(a.dtype) # type of data in array: int
print("mean: ",a.mean())
print("standard_deviation: ", a.std())
print("max:", a.max(), "min: ", a.min(), "sum: ", a.sum())

## change item in array, first item from 100 to 1
a[0] =1
print(a)

## every elment in array times 2
b=2*a
print(b)

# array a+ array b
print(a+b)
print(np.add(a,b))

## array a - array b
print(a-b)
print(np.subtract(a,b))

## array multiply
print(a*b)
print(np.multiply(a,b))

## array division
print(a/b)
print(np.divide(a,b))

## array dot product
print(np.dot(a,b))


# print out the sec to 4th element: [2 3 4 5]
tmp = a[1:5]
print(tmp)

## print 0~8th element,隔一个[start:end:step]， [1 3 5 7]
tmp2 = a[0:8:2]
print(tmp2)

## print first element to 4th element
tmp3 = a[:4]
print(tmp3)

## print all element after the 4th element
tmp4 = a[4:]
print(tmp4)

## linspace: 生产范围内平均分布的数字, return evernly spaced num in specified interval
print(np.linspace(-2, 2, num=6))


## plot, 画向量相加的线
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, num=100)
y = np.sin(x)
plt.plot(x, y)
plt.plot(a,b)

print("####################################### 2d numpy ###########################################################")
list1 = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33,34]]
array1 = np.array(list1)
print(array1)
print("dim: ", array1.ndim, "num of dime and size of each dime: ",array1.shape, "total element in array: ", array1.size)

#    0      1    2    3
#0   11    12   13   14
#1   21    22   23   24
#2   31    32   33   34

## array(row,col)

## Access the element on the first and second rows and third column: [13 23]
print(array1[0:2,2])

# Access the element on the first row and first and second columns: [11 12]
print(array1[0][0:2])

## all the element in first, sec row
print(array1[0:2][0:2])

array2 =np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(array2)
## 2d array add
print(array1+ array2)

##all element in array 1 * element in array 2
print(array1 * array2)

## matrix 1 * matrix 2
m1= np.array([[1,2,3], [4,5,6],[7,8,9]])
m2=np.array([[6,6,6], [16,16,16], [26,26,26]])
print(np.dot(m1,m2))

## transposed
print(array1.T)


