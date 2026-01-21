# Understanding the basic of Python
'''
Docstring for Python_Basic._01_Understanding_python_basic
'''

print(type(1))
# print(type())
print(type('1')) 
print(type(1.0))
print(type(True))
name = "prashant"
print(name[::-1])
print(name[0:4])

# creating a list of numbers and understanding slicing and list 
weekly_temp = [1,2,3,4,5,6,7]
print(weekly_temp[0:4])

# for line having our own statement which we want to print and the value we want to display
print(f"weekly temp is {weekly_temp}")

#list_name.remove(value) to remove the element 
weekly_temp.remove(2)
print(f"update 1 {weekly_temp}")

#list_name.append(value) to remove the element 
weekly_temp.append(2)
print(f"update 2 {weekly_temp}")

# for inserting at a specfic index we do tablename.insert(index,value)
weekly_temp.insert(0,0)
print(f"update 3 {weekly_temp}")

# tuple 


# dictionary
city_data = {
    "name" : "pune",
    "temperature" : 20,
    "humidity" : 80,
    "state" : "maharashtra",
    "country" : "india",
    "AQI" : 100
}

print(f"city data {city_data}")

# updating the value
#  dictionary_name["key"]=value 
city_data["AQI"] = 200
print(f"city data {city_data}")

# Adding the value in dictionary
#  dictionary_name["key"]=value
city_data["rainfall"] = 100
print(f"city data {city_data}")

# deleting the value in dictionary
#  del dictionary_name["key"]
del city_data["AQI"]
print(f"city data {city_data}")