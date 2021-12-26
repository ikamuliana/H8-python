# List
a = ['foo', 'bar', 'baz', 'qux']
print(a) #['foo', 'bar', 'baz', 'qux']

#List are Ordered
a = ['foo', 'bar', 'baz', 'qux']
b = ['baz', 'qux', 'bar', 'foo']
a == b #False

#Lists can contain arbitrary
a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
print(a) #[21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

#List elements can be accessed by index
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[0]) #foo
print(a[5]) #corge
print(a[-1]) #corge
print(a[-6]) #foo

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2:5] #['baz', 'qux', 'quux']

# The concatenation (+) and replication (*) operators:
print(a) #['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a + ['grault', 'garply']) #['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'garply']
print(a * 2) #['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'foo', 'bar', 'baz', 'qux', 'quux', 'corge']

# len(), min(), max()
print(a) #['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(len(a)) #6
print(min(a)) #bar
print(max(a)) #qux

#Modifying a single list value
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a) #['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

a[2] = 10
a[-1] = 20
print(a) #['foo', 'bar', 10, 'qux', 'quux', 20]

# A list item can be deleted with the del command:
del a[3]
print(a) #['foo', 'bar', 10, 'quux', 20]