# Python Dictionary
MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

#Accessing Dictionary
print(MLB_team['Minnesota']) #Twins
print(MLB_team['Colorado']) #Rockies
# error
# MLB_team['Toronto']

#Adding an entry to an existing dictionary is simply a matter of assigning a new key and value:
MLB_team['Kansas City'] = 'Royals' 
MLB_team
# output: {'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins', 'Milwaukee': 'Brewers', 'Seattle': 'Mariners', 'Kansas City': 'Royals'}

# If you want to update an entry, you can just assign a new value to an existing key:
MLB_team['Seattle'] = 'Seahawks'
MLB_team
#output: {'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins', 'Milwaukee': 'Brewers', 'Seattle': 'Seahawks', 'Kansas City': 'Royals'}

# To delete an entry, use the del statement, specifying the key to delete:
del MLB_team['Seattle']
MLB_team
#output: {'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins', 'Milwaukee': 'Brewers', 'Kansas City': 'Royals'}

# Building a dictionary incrementally
person = {}
type(person)
 
person['fname'] = 'Hack'
person['lname'] = 'Inalum'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}

print (person) #output: {'fname': 'Hack', 'lname': 'Inalum', 'age': 51, 'spouse': 'Edna', 'children': ['Ralph', 'Betty', 'Joey'], 'pets': {'dog': 'Fido', 'cat': 'Sox'}}
print(person['fname']) #Hack
print(person['lname']) #Inalum
print(person['children']) #['Ralph', 'Betty', 'Joey']
print(person['children'][1]) #Betty
print(person['pets']) #{'dog': 'Fido', 'cat': 'Sox'}
print(person['pets']['cat']) #Sox

# Built-in Methods
d = {'a': 10, 'b': 20, 'c': 30}
# items
print(d.items()) #dict_items([('a', 10), ('b', 20), ('c', 30)])
# keys
print(d.keys()) #dict_keys(['a', 'b', 'c'])
# values
print(d.values()) #dict_keys([10, 20, 30])

#Modifying multiple list values
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[1:4]) #['bar', 'baz', 'qux']
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a) #['foo', 1.1, 2.2, 3.3, 4.4, 5.5, 'quux', 'corge']