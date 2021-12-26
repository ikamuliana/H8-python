# Function Creation
def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)

#example 2
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)


# Calling a Function
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)
# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")


# Pass by reference vs value
def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = mylist+[1,2,3,4]
   print("\nValues inside the function : ", mylist)         #Values inside the function :  [10, 20, 30, 1, 2, 3, 4]
   return mylist
# Now you can call changeme function
mylist = [10,20,30]
print("\nValues outside the function - before : ", mylist)  #Values outside the function - before :  [10, 20, 30]
mylist = changeme( mylist )
print("\nValues outside the function - after  : ", mylist)  #Values outside the function - after  :  [10, 20, 30, 1, 2, 3, 4]

# example 2
def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = [1, 2, 3, 4] # This would assign new reference in mylist
   print("Values inside the function  : ", mylist)  #Values inside the function  :  [1, 2, 3, 4]
# Now you can call changeme function
mylist = [10, 20, 30]
changeme( mylist )
print("Values outside the function : ", mylist)     #Values outside the function :  [10, 20, 30]


# Required Arguments
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)
printme("Hello")    #Hello

#example 2
def calculate_rect(length, width):
  '''This function is used to calculate area of rectangle'''
  print('Area : ', length*width)    #Area: 2000
length = 100
width = 20
calculate_rect(length, width)


# Keyword Arguments
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)
printme(str_input = "Hacktiv8")     #Hacktiv8

#example 2
def printinfo( name, age ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age. : ", age)
printinfo( age=4, name="a" )


# Default Arguments
def printinfo( name, age = 26 ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age  : ", age)
   print("")
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )

#example 2
def printinfo( name, age = 26 ):
   '''This prints a passed info into this function'''
   print("Name : ", name)       #Name: Hacktiv8
   print("Age  : ", age)        #Age : 50
   print("")
printinfo( age=50, name="hacktiv8" )


#Variable-length Arguments
def printinfo( arg1, *vartuple ):
# def printinfo(arg1, arg2, arg3, arg4):
   '''This prints a variable passed arguments'''
   print('arg1     : ', arg1)           #arg1   :10
   print('vartuple : ', vartuple)       #vartuple:()
   print('')
   for var in vartuple:                 #arg1   :70
      print('isi vartuple : ', var)     #vartuple:(60, 50, 'a')
printinfo( 10 )
printinfo( 70, 60, 50, "a" )            #isivartuple: 60, 50, a


# Variable-length argument have two types
    # All nonkeyword varibales will be saved in a tuple
        # def functionname(args, *var_args_tuple ):
        #     '''function_docstring'''
        #     function_suite
        #     return [expression]

    # All nonkeyword variables will be saved in a dict
        # def functionname(args, **var_args_dict ):
        #     '''function_docstring'''
        #     function_suite
        #     return [expression]


# Create a function with nonkeyword variables
def person_car(total_data, **kwargs):
  '''Create a function to print who owns what car'''
  print('Total Data : ', total_data)
  for key, value in kwargs.items():
    print('Person : ', key)
    print('Car    : ', value)
    print('')
person_car(3, jimmy='chevrolet', frank='ford', tina='honda')
person_car(3)

# Parameters (jimmy='chevrolet', frank='ford', tina='honda') will be equal to
# kwargs = {
#     'jimmy': 'chevrolet',
#     'frank': 'ford',
#     'tina': 'honda'
# }


# The Anonymous Functions
sum = lambda arg1, arg2: arg1 + arg2
# That lambda function will be equal to :
# def sum(arg1, arg2):
#     return arg1+arg2
print("Value of total : ", sum( 10, 20 ))   #Value of total: 30
print("Value of total : ", sum( 20, 20 ))   #Value of total: 40


# The return statement
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    return total
total = sum(10, 20)
print("Result function : ", total)  #result function: 30


#Scope of variables
# Declare a global variable
total = 0
# Create sum function
def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total : ", total) #Inside the function local total: 30
# Call a function
sum( 10, 20 )
print("Outside the function global total : ", total)    #Outside the function global total: 0

#example 2
# Declare a global variable
total = 0
# Create sum function
def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total : ", total)           #Inside the function local total: 30
   return total
# Call a function
print("Outside the function global total - before : ", total)   #Outside the function global total - before: 0
total = sum( 10, 20 )
print("Outside the function global total - after : ", total)    #Outside the function global total - after : 30


# Docstring
# Example of docstring in a function
def sum_number(num1, num2):
  '''
  This function is used to sum of 2 variables.
  :param num1: Input number 1 | int or float
  :param num2: Input number 2 | int or float
  
  :return: num3: Sum of number | int or float
  '''
  num3 = num1 + num2
  return num3
# Syntax to get explanation/docstring from a particular module/function/class
print(sum_number.__doc__)