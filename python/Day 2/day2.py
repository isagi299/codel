 # data type
 
 # String
 # we can access any char from a string using --> string[index]
print("hello")
a="helloworld"
print(a[2]) 
 
 # Integer 
a1=234
print(a1+666)
print(1_23_50_325) # 1,23,50,325

#float
a2=3.1413
print(a2+4.212)

#Boolean --> True or Flase

a3= False
print(a3)

# to know the type your data --> type(data)
print(type(a3))
print(type(a))

#type conversion --> convert any type of data ot another
# type conversion --> data_type(data)
# data_type --> str(),int(),float(),bool()

print("he has " + str(6)+" cats")

# operation --> + - * / **
# / always return float number
# ** is a^b
# priority list of operator --> () ** * / + -
# * / are equal important . the calculation goes from left ot right
# + - are equal important . the calculation goes from left ot right
# to make a number to round/whole --> round(number)
# round a number into specific position --> round(number,position)

print(round(3/8,2))

# floor division --> // . remove the float part and return the interger part.
# // return int 
# / return float
print(20//3)

# we can write += -= *= /=

#f-String --> f"string_data {other data type}"

age = 18
score = 77.32
Is_80 = False

print(f"your age is {age}\nyour score is {score}\nis 80 = {Is_80}")

# {:.nf}.format(x) --> show decimal to n point in float number
