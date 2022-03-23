# http://www.math.umbc.edu/~campbell/Computers/Python/linalg.html
age = 40
teskt = "Pan Jan jadł 2kg jogurtu"

heh = '43'
hehe = heh
print(f'{type(heh)}, {type(hehe)}')
print("Giga vortex")
print(f'Is it {age} years old')
cash = input("How much? ")
print(f'I have {cash} money')

print(' '.join(teskt))
print(teskt.split(" "))
twierdzenie = "Metody Inżynierii Wiedzy są najlepsze"
print(falsz.capitalize())
print(f'dlugość {twierdzenie} to {len(twierdzenie)}')
liteki = {"ą": "a", "ę": "e"}
twierdzenie = twierdzenie.replace("ą", "a")
twierdzenie = twierdzenie.replace("ż", "z")
twierdzenie = twierdzenie.replace(" ", "")
print(f'dlugość {twierdzenie} to {len(twierdzenie)}')

twierdzenie_set = set(twierdzenie)
print(f'dlugość {twierdzenie_set} to {len(twierdzenie_set)}')

x = "xcv"
y = 312
z = (x, y)
print(z)
print(type(z))

list1 = [1, 2, 34, 6]
list2 = ["a", "be", "zww"]
list3 = (list1, list2)
list4 = list1 + list2
print(list3)
print(type(list3))
print(list4)
print(type(list4))
print(type(list4[3:4]))
print(list4.index((2)))  # index of number in question

list5 = [23, 6, 2]
list6 = [433, 6, 2]
list5.extend(list6)
print(list5)

dicta = {"Polska": ["Deutschland", "Russia"], "Czechy": "Czechoslowacja"}
print(dicta["Polska"])
sur = dicta.keys()

print(sur)

# TODO: Sort dict by keys or values