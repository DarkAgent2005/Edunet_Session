# # # # # # # print ("Enter the age of the person:")
# # # # # # # age = input()
# # # # # # # print ("The age of the person is:", age)

# # # # # # # if int(age) >18 and int(age) < 24:
# # # # # # #     print("The person is eligible to vote")
# # # # # # # else :
# # # # # # #     print("The person is not eligible to vote")
# # # # # # # # logical operators
# # # # # # # print(not 4<3)
# # # # # # # print(4<3 or 4>3)
# # # # # # # print(4<3 and 4>3)

# # # # # # # # identity operator
# # # # # # # a="a"
# # # # # # # print(4 is 4)
# # # # # # # print(4 is not 4)
# # # # # # # x=4
# # # # # # # print(type(x))
# # # # # # # str(x) # converted to string
# # # # # # # print(type(str(x)))
# # # # # # # print(str(x).isdigit())

# # # # # # # #membership operator
# # # # # # # print("a" in "prashant")
# # # # # # # print("a" not in "prashant")

# # # # # # # # bitwise operator 
# # # # # # # print(4 & 5)
# # # # # # # print(4 | 5)
# # # # # # # print(4 ^ 5)
# # # # # # # print(~4)
# # # # # # # print(4<<3) # 4* 2^3
# # # # # # # print(32>>4) # 32/2^4

# # # # # # # # Taking specific type of input 

# # # # # # # x = int(input("Enter the value of x:"))
# # # # # # # y = float(input("Enter the value of y:"))
# # # # # # # z = complex(input("Enter the value of z:"))
# # # # # # # print(x)
# # # # # # # print(y)
# # # # # # # print(z)

# # # # # # # Conditional Statements
# # # # # # # x=10
# # # # # # # if x>10 :
# # # # # # #     print(x)
# # # # # # # elif x<10 :
# # # # # # #     print("not worthy")
# # # # # # # else : 
# # # # # # #     print("quit")

# # # # # # print("Enter the nos : ")

# # # # # a = int (input("Enter the value of a:"))
# # # # # b = int (input("Enter the value of b:"))
# # # # # # ans = 'yes'
# # # # # # while (ans=='yes'):
# # # # # #     operation = input("Enter operator (+, -, *): ")

# # # # # #     if operation == '+':
# # # # # #         result = a + b
# # # # # #     elif operation == '-':
# # # # # #         result = a - b
# # # # # #     elif operation == '*':
# # # # # #         result = a * b
# # # # # #     else:
# # # # # #         result = "Invalid operator"

# # # # # #     print("Result:", result)
# # # # # #     ans = input("Do you want to continue? (yes/no): ")
# # # # # #     if ans != 'yes':
# # # # # #         break

# # # # # x = int (input("Enter the required table :"))

# # # # # for i in range(x,(x*10)+1,x):
# # # # #     print(i)

# # # # # accessing the list elements through for loop
# # # # # list_01=[1,2,3,4,5]
# # # # # sum=0
# # # # # for i in list_01:
# # # # #     sum+=i
# # # # #     print(i)
# # # # # print(sum)

# # # # # while loop 
# # # # c=0
# # # # while(c<10):
# # # #     print(c)
# # # #     c+=1
# # # # else:
# # # #     print("Done")

# # # # Transfer Statement Pass Break Continue




# # # for i in range(1,11):
# # #     if(i==3):
# # #         continue # to skip the particular element
# # #     if(i==9):
# # #         break # to break the loop
# # #     print(i)

# # # for i in range (1,11):
# # #     pass

# # # > Function 

# # # Inbuilt functions in python print 
# # # explicit

# # # SYNTAX    
# # # name= input("Enter the name : ")
# # # def greeting(name):
# # #     print("Hello",name)

# # # return gives only last thing 

# # weekly_temp = [25,27,28,26,24,30,29]

# # def avg_temp(weekly_temp):
# #     sum=0
# #     for i in weekly_temp:
# #         sum+=i
# #     print("Total sum is : ",sum)
# #     print("Total length is : ",len(weekly_temp))
# #     return sum/len(weekly_temp)

# # print(avg_temp(weekly_temp))

# climate_data = [
#     {"city": "City A", "temperature": 25, "carbon_footprint": 500},
#     {"city": "City B", "temperature": 30, "carbon_footprint": 350},
#     {"city": "City C", "temperature": 22, "carbon_footprint": 600},
#     {"city": "City D", "temperature": 15, "carbon_footprint": 200},
#     {"city": "City E", "temperature": 28, "carbon_footprint": 450},
# ]

# def temperature_data(climate_data):
#         for i in climate_data:
#             if i["temperature"] > 26:
#                   print(i["city"],"is hot")
    
# temperature_data(climate_data)

# def average_carbon_footprint(climate_data):
#     total_footprint = 0
#     for i in climate_data:
#         total_footprint += i["carbon_footprint"]
#     return total_footprint / len(climate_data)

# print(average_carbon_footprint(climate_data)) 

# def sustainable_city(climate_data):
#     for i in climate_data:
#         if i["carbon_footprint"] < average_carbon_footprint(climate_data):
#            print(i["city"],"is sustainable")
#         else : 
#             print(i["city"],"is not sustainable")
# sustainable_city(climate_data)

# def highest_carbon_footprint(climate_data):
#      for i in climate_data:
#           if i["carbon_footprint"] == max(climate_data,key=lambda x:x["carbon_footprint"]):
#                print(i["city"],"has highest carbon footprint")
# highest_carbon_footprint(climate_data)


# def calculate_carbon_footprint(energy_consumption, emission_factor,total_waste,of_w):
#     ec_cf=energy_consumption * emission_factor
#     tw_cf = total_waste * of_w
#     return ec_cf + tw_cf                    
#     return energy_consumpton * emission_factor

# print(calculate_carbon_footprint(1000,0.475,6800,0.92))

# leap year using the lambda funtion 

is_leap_year = lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap_year(2025))
