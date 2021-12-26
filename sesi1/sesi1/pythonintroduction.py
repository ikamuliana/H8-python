# Integers
print(123123123123123123123123123123123123123123123123 + 1)
# python interprets a sequence of decimal digitswithout any prefix
print(10)
print(type(10))

# Floating - point numbers
print(4.2)
print(type(4.2))
print(4.)
print(.2)
print(.4e7)
print(4.2e-4)

# String
print("Hactiv8")
print(type("Hactiv8"))
print("this string contains a single quote(') character.")
print('this string contains a double quote(") character.')

# Boolean
print (type(True))
print (type(False))
#when you compare two values, the expression is valuated and python returns the boolean answer:
print(100 > 200) # false
print(100 == 200) # false

# Variable Assignment
n = 300
print (n)
#python also allows chained assignment, which makes is possible to assign the value to several variables simultaneously:
a = b = c = 300
print(a, b, c)

# Variable name
name = "Hacktiv8"
Age = 54
has_laptops = True
print(name, Age, has_laptops)

age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_) #output: 1 2 3 4 5 6 7 8

# Operators and Expressions
#In Python, operators are special symbols that designate that some sort of computation should beperformed. The values that an operator acts on are called operands. Here is an example:
a = 10
b = 20
print(a + b)
print(a + b - 5)

# Arithmetic Operators
# Here are some examples of these operators in use:
a = 4
b = 3
print('a + b', a + b)
print('a - b', a - b)
print('a * b', a * b)
print('a / b', a / b)
print('a // b', a // b)
print('a % b', a % b)
print('a ** b', a ** b)

# Comparison Operators
# Here are examples of the comparison operators in use:
a = 10
b = 20
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

# String Manipulation
s = 'foo'
t = 'bar'
# + and * Operators
print(s + t)
print(s * 4)
#Case Conversion
#Capitalize
print(s.capitalize())
#Lower
print(s.lower())
#Swapcase
print(s.swapcase())
#Title
print(s.title())
#Uppercase
print(s.upper())

# Python Lists
# Lists are defined in Python by enclosing a comma-separated sequence of objects in square brackets ([]), asshown below:
a = ['foo', 'bar', 'baz', 'qux']
print(a)

# Modifying List Value
#A single value in a list can be replaced by indexing and simple assignment:
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2] = 10
a[-1] = 20
print(a)

a = 'aaaa'
i = 22
j = 122
print('Umur : {}{}'.format(i,j))
print('Umur : {nilai_i}{nilai_j}'.format(nilai_j = j, nilai_i = i))
print(f'Umur : {i}{j}')
print(f"Umur : {i}{j}")

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a [2:5]
#a[n:m] -> return from index m to n, but exclude n
#2 3 4
print (a) # output : ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a + ['grault', 'garply']) #['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'garply']
print(a * 2) #['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# len(), min(), max()
print(len(a)) #output: 6
print(min(a)) #output: bar
print(max(a)) #output: qux

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print(a[1:4]) #output: ['bar', 'baz', 'qux']
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a) #output: ['foo', 1.1, 2.2, 3.3, 4.4, 5.5, 'quux', 'corge']

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] 
#kosong di depan 
a[:5]
a[0:5]
# 0 1 2 3 4
# a b c d e

#kosong di belakang
a[3:]
a[3:7]
# 3 4 5 6 
# d e f g


# Python Tuples
#Tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([]). Tuples areimmutable. Here is a short example showing a tuple definition, indexing, and slicing:
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
print(t[0])
print(t[-1])
# packing and unpacking
(s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')
print(s1)

# Tuple
single_element_tuple = (22,)
print(type(tuple_element_tuple))
# output : <class 'tuple'>

# Defining and Accessing Dictionary
#You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}). Acolon (:) separates each key from its associated value.
MLB_team = {    
    'Colorado': 'Rockies',    
    'Boston': 'Red Sox',    
    'Minnesota': 'Twins'
    }
print(MLB_team['Minnesota'])
#Adding an entry to an existing dictionary
MLB_team['Kansas City'] = 'Royals'
MLB_team
# output: {'Colorado': 'Rockies','Boston': 'Red Sox','Minnesota': 'Twins','Milwaukee': 'Brewers','Seattle': 'Mariners','Kansas City': 'Royals'}

# accessing dictionary values
print(MLB_team['Minnesota']) #output: Twins
print(MLB_team['Colorado']) #output: Rockies

# If you want to update an entry, you can just assign a new value to an existing key:
MLB_team['Seattle'] = 'Seahawks'
MLB_team
#output : {'Colorado': 'Rockies','Boston': 'Red Sox','Minnesota': 'Twins','Milwaukee': 'Brewers','Seattle': 'Seahawks','Kansas City': 'Royals'}

# To delete an entry, use the del statement, specifying the key to delete:
del MLB_team['Seattle']
MLB_team
#output: {'Colorado': 'Rockies','Boston': 'Red Sox','Minnesota': 'Twins','Milwaukee': 'Brewers','Kansas City': 'Royals'}

#Building a Dictionary Incrementally
#You can start by creating an empty dictionary, which is specified by empty curly braces. Then you can addnew keys and values one at a time:
person = {}
person['fname'] = 'Hack'
person['lname'] = '8'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
print(person) #output: {'fname': 'Hack','lname': '8','age': 51,'spouse': 'Edna','children': ['Ralph', 'Betty', 'Joey'],'pets': {'dog': 'Fido', 'cat': 'Sox'}}
print(person['children'][1]) #output: Betty
print(person['pets']['cat']) #output: Sox

# Built-in Methods
d = {'a': 10, 'b': 20, 'c': 30} 

# items
print(d.items()) #output: dict_items([('a', 10), ('b', 20), ('c', 30)])

# keys
print(d.keys()) #output: dict_keys(['a', 'b', 'c'])

# values
print(d.values()) #output: dict_values([10, 20, 30])

# Python Statement
print('Hello, World!') #output: Hello, World!

x = [1, 2, 3]
print(x) # output: [1, 2, 3]

# Line Continuation
person1_age = 42
person2_age = 16
person3_age = 71

someone_is_of_working_age = (person1_age >= 18 and person1_age <= 65) or (person2_age >= 18 and person2_age <= 65) or (person3_age >= 18 and person3_age <= 65)
someone_is_of_working_age #output: True
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
someone_is_of_working_age = (
    (person1_age >= 18 and person1_age <= 65)
    or (person2_age >= 18 and person2_age <= 65)
    or (person3_age >= 18 and person3_age <= 65)
)

someone_is_of_working_age #output: True