# # # raka = ["Raka Ardhi", 28, "CurDev", 2265]
# # # spock = ["Spock", 35, "Science Officer", 2254]
# # # mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

# # # 0                       1                               2                       3
# # # "Raka Ardhi",           28,                             "CurDev",               2265,
# # # "Spock",                35,                             "Science Officer",      2254,
# # # "Leonard McCoy",        "Chief Medical Officer",        2266,

# # # print("Daftar nama: ", raka[0], spock[0], mccoy[0])
# # # print("Daftar umur: ", raka[1], spock[1], mccoy[1])
# # # print("Daftar jabatan: ", raka[2], spock[2], mccoy[2])
# # # print("Daftar tahun mulai: ", raka[3], spock[2], mccoy[3])

# # class Dog:   
# #     # Class attribute
# #     species = "Canis familiaris"
# #     def __init__(self, name, age):        
# #         self.name = name        
# #         self.age = age

# #     # def __init__(self, input_name, input_age):        
# #     #     self.name = input_name        
# #     #     self.age = input_age

# #     # def __init__(self, name, age):
# #     #     self.info_name = name        
# #     #     self.info_age = age

# # # dog_1 = Dog('Miley', 7)
# # #     # __init__(dog_1, 'Miley', 7)
# # # dog_2 = Dog('Hike', 2)
# # #     # __init__(dog_2, 'Miley', 2)
# # # dog_3 = Dog('Vivi', 1)
# # # buddy = Dog("Buddy", 9)

# # # print("Dog 1 ::", dog_1.name, dog_1.age)
# # # print("Dog 2 ::", dog_2.name, dog_2.age)
# # # print("Dog 3 ::", dog_3.name, dog_3.age)
# # # print("Buddy ::", buddy.name, buddy.age)
# # # dog_3 = Dog()
# # # dog_3.name = 'Vivi'
# # # dog_3.age = 1

# # # print(dog_1.speak(''))


# # # print("Species")
# # # print("Dog 1", dog_1.species)
# # # print("Dog 2", dog_2.species)
# # # print("Dog 3", dog_3.species)
# # # print("Buddy", buddy.species)


# # # =========================================
# # # Keyword :
# # # class
# # # instance
# # # class attribute / class variable
# # # instance attribute / instance variable
# # # instance method
# # # =========================================


# # class Dog:
# #     species = "Canis familiaris"

# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# # # Instance Methods
# # def description(self):
# #     return f"{self.name} is {self.age} years old"

# # # Another instance method
# # def speak(self, sound):
# #     return f"{self.name} says {sound}"
# #     # {dog_1.name} {"Woof woof"}
# #     # {'Miley'}
# #     # {dog_1.name} {"Bow wow"}
# #     # {'Miley'}

# # dog_1 = Dog('Miley', 7)
# # buddy = Dog('Buddy', 1)

# # print (buddy.description () )
# # print (dog_1.description () )

# # print(dog_1.speak("Woof woof"))
# # print(dog_1.speak("Bow wow"))

# # Parent Class
# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"

# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")

# #subclass of dog
# class Bulldogs(Dog):
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#     #Another instance method
#     def speak(self):
#         return f"{self.name} says Woof Woof"

# class Dachshund(Dog):
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#     #Another instance method
#     def speak(self):
#         return f"{self.name} says Yap Yap"

# class Bulldogs(Dog):
#     def speak(self):
#         return f"{self.name} says Woof Woof"

# # Parent class
# class Dog:
#     species = "Canis familiaris"
 
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
 
#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"
 
#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"

#     # def __repr__(self):
#     #     return f"to create instance:: Dog(name={self.name}, age={self.age}, breed={self.breed} #REPR"

#     # def __str__(self):
#     #     return f"clean info:: {self.name} is {self.age} years old {self.breed}) #STR"

# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")

# print(miles)
# print(repr(miles))

# class JackRussellTerrier(Dog):
#     def speak(self, sound="Arf"):
#         return f"{self.name} says {sound}"

# hike = Bulldogs('Hike', 9, 'Bulldogs')
# miles = JackRussellTerrier('Miles', 9, 'Jack Russel Terier')
# dachs = Dachshund('Dachs', 9, 'Bulldogs')

# print(hike)
# print(miles)
# print(dachs)


# print(1 + 1)        #2, int + int
# print('1' + '1')    #11, str + str
# print(hike + miles) #??

# # __repr__() # provide unambiguous tentang suatu object -> ditujukan baca oleh developer: debugging, logging, etc etc "Dog(self, name, age, breed)"
# # __str__() # provide informasi yang lebih readabl -> tujuannya untuk disaksikan / ditujukan kepada end user => "Miley is 4 years old"

# # print(hike)
# #     cuma ada 1: __str__() => __str__()
# #     cuma ada 1: __repr__() => __repr__()
# #     kalau dua-duanya ada: prioritas 1 __str__() -- 2 __repr__()

# # __doc__() => docstring
# # __init__()
# # __str__()
# # __repr__()
# # __add__()

# class Dog:
#     species = "Canis familiaris"
 
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
 
#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"
 
#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"

#     def __repr__(self):
#         return f"to create instance:: Dog(name={self.name}, age={self.age}, breed={self.breed} #REPR"

#     def __str__(self):
#         return f"clean info:: {self.name} is {self.age} years old {self.breed}) #STR"

# miles = Dog("Miles", 4, "Jack Russell Terrier")
# # buddy = Dog("Buddy", 9, "Dachshund")
 
# # Sebelum __repr__ or __str__ ada
# print(miles) # akan return memory addres untuk object/instance miles, seperti : <__main__.JackRussellTerrier object at 0x000002806CAEABB0>
# #^ lihat ke catatan bagian prioritas
 
 
# #Setelah ada  dunder method __repr__() ATAU __str__()
# print(repr(miles))
# print(miles.__repr__())
 
# print(str(miles))
# print(miles.__str__())

class Dog:
    species = "Canis familiaris"
 
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
 
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
 
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
 
    def __repr__(self):
        return f"to create instance :: Dog( name={self.name}, age={self.age}, breed={self.breed} ) #REPR"
 
    def __str__(self):
        return f"clean info :: {self.name} is {self.age} years old {self.breed}  #STR"


class Bulldogs(Dog):
    def __init__(self, name, age, breed, weight_in_lbs):
        # self.name = name
        # self.age = age
        # self.breed = breed
        super().__init__(name, age, breed)
        self.weight_in_lbs = weight_in_lbs
    
    #Another instance method
    def speak(self):
        return f"{self.name} says Woof Woof"

    def __add__(self, other):
        return self.weight_in_lbs + other.weight_in_lbs

scooby = Bulldogs('Scooby', 2, 'Bulldogs', 15)
scooby_jr = Bulldogs('Scooby JR', 1, 'Bulldogs', 8)
print("Scooby : ", scooby.weight_in_lbs)
print("Scooby JR : ", scooby_jr.weight_in_lbs)