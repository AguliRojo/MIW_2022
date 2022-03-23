word = 'pizza'
if 'a' in word:
    print(word)
print(*range(0,21))
for i in range(0,21):
    print(i)

slowa = "Jan szedl przez wies"
split_val = []
split_emulator = ''
splitter = ' '
for c in slowa:
    if c == splitter:
        split_val.append(split_emulator)
        split_emulator = ''
    else:
        split_emulator += c
if split_emulator:
    split_val.append(split_emulator)
print(split_val)


# password validator
# 10 znaków , posiada caps
password = "ab34S56dqwdq!s"
maly = False
duzy = False
for i in range(len(password)):
    if password[i] >= "A" and password[i] <= "Z":
        duzy = True
    if password[i] >= "a" and password[i] <= "z":
        maly = True
print(bool("a"<"b"))
if '!' in password and len(password) >=10 and maly and duzy:
    print("Nice")

# dataframe 5 element 5liczb , 1 z nich 79
# za pomowa for wypisz w kazdej lini wartosc bez 79
lista_5 = [1,79,2,5,7]
for i in range(len(lista_5)):
    if lista_5[i] == 79:
        continue
    print(lista_5[i])

#czy nalezy przez while
while lista_5 is not None:
    if 5 in lista_5:
        print("True")
        break
    print("False")
    break

#TODO: przygotuj plik np. data.txt
# w pliku w odzielnich lnijkach wczytaj Metody Inżynierii Wiedzy. Kazde słowko wydrukuj linijka po linijce
