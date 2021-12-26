# Python "while" loops
# while <expr>:
#     <statement(s)>

#while
n = 5               #output: 4      #5 4 3 2 1 0 xxx
while n > 0:                #3      #n = n - 1 #4 3 2 1 0
    n -= 1                  #2      #4 3 2 1 0
    print(n)                #1
                            #0

#while2
i = 1               #output: 1      #1 2 3 4 5 6xxx
while i < 6:                #2      #1 2 3 4 5
  print(i)                  #3      #2 3 4 5 6
  i += 1                    #4
                            #5

#break
i = -1                      
while i < 6:                #output: -1
    print(i)                        #0
    if i == 2:                      #1
        break                       #2
    i += 1                          #print yang di luar loop
print('print yang di luar loop')

# The python break and continue statements
n = 5
while n > 0:    #5 4 3 2 1 0                  #output: 3
    n -= 1      #4 3 2 1 0                           #4
    if n == 2:  #break                             #Loop ended
        break # Break Statement
    print(n)    #4 3
print('Loop ended.')

# Continue
n = 5
while n > 0:                #output: 4
    n -= 1                          #3
    if n == 2:                      #2
        continue                    #1
    print(n)                        #0
print('Loop ended.')                #Loop ended


# The else clause
# while <expr>:
#     <statement(s)>
# else:
#     <additional_statement(s)>
n = 5
while n > 0:                #output: 4
    n -= 1                          #3
    print(n)                        #2
    if n == 2:                      #1
        break                       #0
else:                               #Loop done
    print('Loop done.')

#clause 2
n = 5
while n > 0:               #output: 4
    n -= 1                         #3 
    print(n)                       #2
    if n == 2:
        break
else:
    print('Loop done.')

# Nested while loops
a = ['foo', 'bar']

while len(a):                   #output: foo
    print(a.pop(0))                     #> baz
                                        #> qux
    b = ['baz', 'qux']                  #bar
                                        #> baz
    while len(b):                       #> qux
        print('>', b.pop(0))

# One line while loops
n = 5
while n > 0: n -= 1; 
print(n) #0 1 2 3 4

# The Python for Loop
#example1
a = ['foo', 'bar', 'baz']   #output:foo
for i in a:                        #bar
    print(i)                       #baz
     
#example2
d = {'foo': 1, 'bar': 2, 'baz': 3} #output:foo
for k in d:                               #bar
    print(k)                              #baz

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k, v in d.items(): #(value1, value2)
    print(k, ":", v)   #('foo', 1)

# for k, v in d.items()
#for kunci, nilai d.items()

#The range () function
#x = range (5) => 1 2 3 4
# x = range(1,5)
x = range(0, 10, 4) #in java dan php for (i=0; i<10; i+4)
for n in x:
    print(n)


# The break and continue statement
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i) #foo

#continue
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i) #foo qux

#example
for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Will execute
    #output: foo bar baz qux done

#example
for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'bar':
    break
  print(i)
else:
  print('Done.') #foo


