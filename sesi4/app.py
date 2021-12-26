# f = open("test.txt")
# f = open("test.txt", 'w') #write -> menulis dan menimpa(replace) exixting teksnya
# f = open("test.txt", 'a') #append -> manulis tapi di paling akhir(setelah)
# f = open("test.txt", 'r') #read -> membaca

# file = open('Hack8_Sample_Text.txt')
# print(file.read(4), "\n -- \n")
# print(file.read(6), "\n -- \n")
# print(file.tell())
# print(file.read(12), "\n -- \n")
# file.seek(25)
# print(file.tell())
# print(file.read(4), "\n -- \n")
# print(file.read(), "\n -- \n")

# try:
    # file = open('Hack8_Sample_Text_22.txt')
# logic jsdbjwdjw
# finally:
    # file.close()
# file.close()

# our_file = open('Hack8_Sample_Text.txt')
# our_file.seek(0)
# # for line in our_file:
# #     print(line, end = '')

# print(our_file.readline())
# # print(our_file.readlines())

# our_rows = our_file.readlines()
# print(our_rows[6], our_rows[4])

#Should be greater
# x = 10
# if x < 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))


#
# x = 22
# assert x == 20, "x harus 20"
# assert(x, 20, "berbeda")
# assert x == 20, "berbeda"

# import sys
# assert ('linux' in sys.platform), "This code runs on Linux only."
# assert ('windows' in sys.platform), "This code runs on Windows only."

# def perkalian_dengan_0(num1):
#     # return 0 * num1
#     return 0 * num1 + 1
# a = 0
# # sepuluh_kali_0 = perkalian_dengan_0(10)
# sepuluh_kali_0 = perkalian_dengan_0(10)
# assert sepuluh_kali_0 == 0, "fungsi masih salah"

# import sys
# print(sys.platform)
# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('windows' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')

#os_interaction()
# try:
#     os_interaction()
# except:
#     print('ewerwjnekrb Error')


# try:
#     os_interaction()
# except AssertionError as error:
#     print("##", error)
#     print('The os_interaction() function was not executed')

# with open('file.log') as file:
#     read_data = file.read()

# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except:
#     print('Could not open file.log')
#     print('file.log is not find in this directory')


# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)

import sys
print(sys.platform)
def os_interaction():
    # assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('win32' in sys.platform), "This code runs on Windows only."
    # file = open('file_baru.txt')
    print('Doing something.')
# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     print('Executing the else clause.')


# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)


try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')
    print('End')