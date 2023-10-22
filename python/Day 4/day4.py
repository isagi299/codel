# random module --> to creater random number . we have to import random. 
import random
# import my_module

# to use the module after import --> module_name.function()
# to create random interger --> random.randint(a,b) where a>b; it will give random number between a and b including.
random_int = random.randint(1,15) 
print(random_int)

# to create our own module. first create a file and import it in this code . and use it.
# print(my_module.pi)

# we can chage the random number by adding , multiply, division , substraction
# to create random float --> random.random(a,b) where a>b; it will give random number between a and b where b is not including.

random_float=random.random()*5 # it will create float random number
print(random_float)

# charge the order of a list randomly or shuffle : random.shuffle(list_name)
# random item from a list --> random.choice(list_name)
# add a item in a list --> list_name+=item or list_name.append(item)