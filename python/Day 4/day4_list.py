# list is like array 
# notation --> list_name = [data1, data2, data3]
# access the list data --> list_name[index]
# change the list data --> list_name[index] = change_data
# index start with 0,1,2. the last elements of list can access by -1,-2,-3.
# to print the whole list --> print(list_name)
# length of a list --> len(list_name)
number = [1,2,3,4,5,6]
print(number)
print(number[3]) 
number[3]=99
print(number[3]) 
print(number[-2])

# nested list --> list_name = [list1,list2,...]
even = [2,4,6,8]
odd = [1,3,5,7]
x=[9,9,9]
number1=[odd,even,x]
print(number1)

# access member in nested list --> list_name[[index][index]]
print(number1[2][2])
