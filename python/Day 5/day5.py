# loop
# for loop --> for item in list_of_item_name:
                    #write code
a=[1,2,3,4,5]
for i in a:
    print(i)
    print(f"{i} is a number")
    
# using for loop with range function --> for i in range(a,b): it will acess a to b-1.(b is not including)
# if i want print a to b then range funcition will be range(a,b+1)
# if we want to specify the step then --> range(a,b,c) where c is step
for i in range(1,11,2):
    print(i)
