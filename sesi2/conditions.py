# Conditinal
x = 0
y = 5

if x < y:                            # Truthy
    print('yes')
if y < x:                            # Falsy
    print('yes')
if x:                                # Falsy
    print('yes')
if y:                                # Truthy
    print('yes')
if 'aul' in 'grault':                # Truthy
    print('yes')
if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes')
# output: yes
        # yes
        # yes

# Grouping Statements: Identation adn Blocks
# if <expr>:
#     <statement>
#     <statement>
#     ...
#     <statement>
# <following_statement>

if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional') #After conditional

# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x
#output: Outer condition is true
        #Between inner conditions
        #Inner condition 2
        #End of outer condition
        #After outer condition

# x = 10 - 15 -> tampil
x = 13
# sunny = True
sunny = False
# if x >= 10 and x <= 15 and sunny == False:
# if x >= 10 and x <= 15 and not sunny:

# if x >= 10 and x <= 15 and sunny == True:
if x >= 10 and x <= 15 and sunny:
    print(x)

# The else and elif clauses
# if <expr>:
#     <statement(s)>
# else:
#     <statement(s)>

x = 20
if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')
#output: (first suite)
        # x is small

x = 120
if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')
#output: (first suite)
        # x is large

hargaBuku = 20000
hargaMajalah = 5000
# uang = 2000   => uang tidak cukup
# uang = 30000  => beli buku
uang = 7000     # uang tidak cukup
if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup") 

hargaBuku = 20000
hargaMajalah = 5000
# uang = 2000
# uang = 7000 => beli majalah
uang = 27000 # beli buku (karena transaksi pertama beli buku)
if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")
print ('transaction done')

name = 'Hacktiv8'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!") #Hello Hacktiv8

total_purchase = 1000
# if 'a' in 'bar':
if 'aa' in 'bar':
    print('foo')
elif total_purchase >= 850:
    print('discount 30%')
elif 1/0:
    print("This won't happen")
elif var:
    print("This won't either") #foo

# One line if statement
if 'foo' in ['foo', 'bar', 'baz']:
    print('yes foo'); print('lalalala')

if 'f' in 'foo': print('1'); print('2'); print('3') 
# output: 1
        # 2
        # 3

if 'z' in 'foo': print('1'); print('2'); print('3')

# Multiple statements may be specified on the same line as an elif or else clause as well:
x = 2
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')
#output: qux
        #quux

x = 3
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')
#output: corge
        #grault

x = 3
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')  #output: corge
    print('grault')         #grault

# Conditional Expressions (Python's Ternary Operator)
#Ternary if 1
#rainung = false => 'beach'
#rainung = true => 'library'
raining = False
print("Let's go to the", 'beach' if not raining else 'library')
#output: Let's go to the beach

if not raining:
    print("Let's go to the beach")
else: 
    print("Let's go to the library")

# 'beach' if not raining else 'library'
# <expr1> if <conditional_expr> else <expr2>

# raining = True
# print("Let's go to the", 'beach' if not raining else 'library')
#output: Let's go to the library

# Tenary if 2
age = 12
s = 'teen' if age < 21 else 'adult'
# if age < 21:
#     s = 'teen'
# else:
#     s = 'adult'
print(s) #output: teen

# Ternary if 3
'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'
#output: no

# Standard statement
m = if a > b else b
m = b
if a > b :
    m = a
else:
    m = b

# The python pass statement
if True:
    pass
print('foo') #foo