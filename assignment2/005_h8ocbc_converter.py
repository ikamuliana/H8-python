convert = u"\N{Degree Sign}"
text = int(input('Masukkan temperature: '))

def kelvin_celcius(degree):
    print('Kelvin to Celcius and Celcius to Kelvin: ')

    '''Kelvin to Celcius'''
    print(degree, convert, "Kelvin is ", degree - 273, convert, "Celcius")
    '''Celcius to Kelvin'''
    print(degree, convert, "Celcius is ", degree + 273, convert, "Kelvin")


def to_fahrenheit(degree, tmp):
    if(tmp == 'Celcius'):
        print('Celcius to Fahrenheit:')
        '''Celcius to Fahrenheit'''
        print(degree, convert, "Celcius is ", ((9 / 5) * (degree + 32)), convert, "Fahrenheit")
    elif(tmp == 'Kelvin'):
        print('Kelvin to Fahrenheit:')
        '''Kelvin to Fahrenheit'''
        print(degree, convert, "Kelvin is ", ((9 / 5) * (degree - 273) + 32) , convert, "Fahrenheit")
    else:
        print('Input invalid')


def from_fahrenheit(degree):
    print('Fahrenheit to Kelvin and Fahrenheit to Celcius')
    '''Fahrenheit to Kelvin'''
    print(degree, convert, "Fahrenheit is ", ((5 / 9) * (degree - 32) + 273), convert, "Kelvin")
    '''Fahrenheit to Celcius'''
    print(degree, convert, "Fahrenheit is ", ((5 / 9) * (degree - 32)), convert, "Celcius")
    

print('\n')
kelvin_celcius(text)
print('\n')
text1 = input('Convert [kelvin/celcius] to fahrenheit: ')
to_fahrenheit(text, text1)
print('\n')
from_fahrenheit(text)
