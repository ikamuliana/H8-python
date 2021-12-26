def penjumlahan (num1, num2, num3):
    return num1 + num2 + num3
def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)
    return p * l

# def printme( str_input ):
#    '''This prints a passed string into this function'''
#    print(str_input)

# my_function(9, 2)
# print(my_function.__doc__)

# printme(100)
# print(printme.__doc__)

# printme("I'm first call to user defined function!")
# printme("Again second call to the same function")


# luas = my_function(10, 3)
# print(f"Luas persegi panjang adalah {luas}")

# hasil_penjumlahan  = penjumlahan (50, 60)
# hasil_penjumlahan  = penjumlahan (50, 60, 4)
# # hasil_penjumlahan = num1 + num2 + num3
# #                   = 50   + 60   + 4
# #                   = 114
# print(f"hasil penjumlahan {hasil_penjumlahan}")

# def save_data(name, age):
#     print(f"Nama : {name}")
#     print(f"Age + 10 = {age + 10}")
#     # return None

# save_data('Adi', 20)
# # save_data(20, 'Adi')


# # Keyword Arguments
# save_data(age = 20, name = 'Adi')


#Default Arguments
# def printinfo( name, age = 26 ):
#    '''This prints a passed info into this function'''
#    print("Name : ", name)
#    print("Age  : ", age)
#    print("")
# # Now you can call printinfo function
# printinfo( age=50, name="hacktiv8" )
# printinfo( name="hacktiv" )


# Variable-length Arguments
# def printinfo( arg1, *vartuple ):
# # def printinfo(arg1, arg2, arg3, arg4):
#    '''This prints a variable passed arguments'''
#    print('arg1     : ', arg1)
#    print('vartuple : ', vartuple)
#    print('')
   
#    for var in vartuple:
#       print('isi vartuple : ', var) 

# # Now you can call printinfo function
# printinfo( 10 )
# printinfo( 70, 60, 50, "a" )
# printinfo( 70, 60, "a" )


# # The Anonymous Function
# penjumlahan = lambda num1, num2, num3 : num1 + num2 + num3
# print(penjumlahan(1, 2, 3))

# penjumlahan_copy = penjumlahan(1, 3, 2)
# print(f"copy of penjumlahan = {penjumlahan_copy}")


# # The return Statement
# def penjumlahan_pengurangan(num1, num2):
#     sum = num1 + num2
#     sub = num1 - num2

#     # print(f "sub = {sub}")
#     # print(f "num1 = {num1}")
#     # return num1 + num2, num1 - num2
#     return sum, sub
# print(penjumlahan_pengurangan(10, 1))


# Scope of variables

print
import brands
print(brands.brands)