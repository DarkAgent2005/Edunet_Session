import numpy as np

ec= [1200,3400,2900,2500]
# Declaring a numpy array
energy_consumption = np.array(ec)

# print ("Energy consumption (in MHW)for different sources is ")
# print(energy_consumption)
# print(type(energy_consumption))

# MATRIX CREATION
# A = np.ones(4)
# A2 = np.ones((4,4))
# print(A)
# print("\n",A2)

M = np.identity(4)
# print(M)

total_consumption = np.sum(energy_consumption)
# print(f"Total energy consumption is {total_consumption} MHW")

mean_consumption = np.mean(energy_consumption)
# print(f"Mean energy consumption is {mean_consumption} MHW")

max_consumption = np.max(energy_consumption)
# print(f"Maximum energy consumption is {max_consumption} MHW")

min_consumption = np.min(energy_consumption)
# print(f"Minimum energy consumption is {min_consumption} MHW")

# reshpe the array to rows and column 
energy_consumption= np.array([1200,3400,2900,1800,2500,1800])

energy_consumption = energy_consumption.reshape(3,2)
# print("reshaped energy consumption array (3x2) is \n",energy_consumption)

# flatten x dimension array to a single array  reshapearray.flatten()

# print("Flattened array is \n",energy_consumption.flatten())

# transpose array reshape_array.T
# print("Transposed array is \n",energy_consumption.T)

# resizing array 
resizearray = np.resize(energy_consumption,(4,4))
# print("Resized array is \n",resizearray)


#np.array(): Creates a NumPy array from a lis
Third_semester_marks= np.array([80,85,80])
second_semester_marks= np.array([70,65,50])
square = np.array([4,16,25])
print("Third semester marks is \n",Third_semester_marks)

#np.reshape(): Changes the shape of an array
print("Reshaped array is : \n",Third_semester_marks.reshape(3,1))

#np.random.randint(0, 10, 1): Generates a randon integer between 0 and 10
print("Random integer is : \n",np.random.randint(0,10,1))

#np.unique(): Finds the unique elements in an array and returns them in sorted order
print("Unique elements in Third semester marks is : \n",np.unique(Third_semester_marks))

#np.dot(): Computes the dot product of two array
print("Dot product is : \n",np.dot(Third_semester_marks,second_semester_marks))

#np.power(a, 2): Raises each element of array a to the power of 2
print("square of array is : \n",np.power(square,2))

#np.sqrt(a): Returns the square root of each element in the array a.
print("Sqare root of array is : \n",np.sqrt(square))

# np.ones(): Creates a new array of the specified shape, filled with ones.
print("Ones array is : \n",np.ones((3,3)))
# np.zeros(): Creates a new array of the specified shape, filled with zeros.

# np.max(): Returns the maximum value in the array.

# np.arange(10): Creates an array with evenly spaced values from 0 to 9.


