# dataframe = lista
# numerical = dane liczbowe bez decyzji (i kategorii)
# categorical = dane kategoryczne
# decision = decyzje bez danych

dataframe = []
with open("australian.dat", "r") as file:
    for line in file:
        kolekcja = line.replace("\n","").split()
        kolekcja = list(map(lambda e: float(e), kolekcja)) #Using map is enough
        dataframe.append(kolekcja)

numerical = [item[:-1] for item in dataframe]
decision = [item[-1] for item in dataframe]
decision_keys = []

def euklides(numerical):
    dimensions = len(numerical)
    distance = 0
    arg_a = 0
    arg_b = 0
    for d in range(0,dimensions-1):
        arg_a = sum(numerical[d])# dodaje wszystko , nmie wiem od czego mam odejmowac
        arg_b = sum(numerical[d+1])
        distance += (arg_a-arg_b)** 2
        distance = distance ** (1/2)
        print(distance)
        distance = 0
        # zrob podwojnego loops i zrobisz 1vsall w ten sposob

    #     distance += (numerical[d] - b[d] ** 2)
    # distance = distance ** (1/2)
    # return distance
    return distance
euklides(numerical)

# print(dataframe)
# print(dataframe[0])
# print(type(dataframe[0]))
# print(dataframe[:5])
# print(kolekcja)


# dzisiejszy kod
#import numpy as np
#v1 = np.array(lista1)
#v2 = np.array(lista2)
#c = v1-v2
##np.dot(,) #iloczyn skalarny
#mamy odejmowac od siebie odległosci wektow (nie robilismy tego wczesniej?)

list1 = []
inputted = input("Enter the first list : ")
inputted = inputted.split()
for i in inputted:
    list1.append(int(i))

#Iloczyn kazrtezjanski
list1 = [int(i) for i in input("Enter the first list : ").split()]
list2 = [int(i) for i in input("Enter the second list : ").split()]
cartesianProduct = []
# cartesian product is simply the product of each element of list with every other element of second list
for i in list1:
    for j in list2:
        result = (i , j)
        cartesianProduct.append(result)
print("cartesianProduct = ")
print(cartesianProduct)

#koniec kodu

# def eukldes(element1, element2):
#     mean_square = sum(sqrt(([for i in element1]+[for i in element2])**2))
#TODO: nie działa
#TODO: Praca domowa: Pierwszy element listy to y = dataframe[0]
# odległość d(y,x), gdzie x nalezy naszej listy ale nie jest dataframe[0]
# w słowniku pogrupowac odległóści
#klasa decyzyjna x to ostatni element
# wartosc to dataframe odległości
# dodatkowo napisac funkcje ktora liczy wyznacznik macierzy kwadratowej

#nowe do domu
#Lista wektorow odleglosci do klasy decyzyjnej?
#wyznaczyc klase decyzyjna bez korzystania z poczatkowo przypisanych las decyzyjnych (random color decisions)
# najblizszy ma najmniejsza sume odleglosci od reszty
# praca domowa:
# calkowanie numeryczne - Monte Carlo (calkowanie I)
# calkowanie II - Nie jasne narysowany jakis trojkat i masz dwie czesci  
# jedna to to co chcemy , druga trzeba scalkowac zeby wiedziec ile wynosi (im wiecej ciec tym lepszy wynik)
# metoda prostokatow/trapezow i monte carlo
# 28 luty 1h10min - mowi podobno o tym