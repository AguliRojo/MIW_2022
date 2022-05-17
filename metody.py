# dataframe = lista
# numerical = dane liczbowe bez decyzji (i kategorii)
# categorical = dane kategoryczne
# decision = decyzje bez danych
import pandas as pd

# otwieranie pliku
dataframe = []
with open("australian.dat", "r") as file:
    for line in file:
        kolekcja = line.replace("\n","").split()
        kolekcja = list(map(lambda e: float(e), kolekcja)) # Using map is enough
        dataframe.append(kolekcja)

# grupowanie kolumn bazy
numerical = [item[:-1] for item in dataframe] # dane numeryczne
decision = [item[-1] for item in dataframe] # dane kategoryczne
decision_keys = []

# zasieg zmiennych
# def value_range(dataframe): # problem: how to return both min and max
                                # answer: by making map/dict of values.

# zip() function takes iterables, aggregates them in a tuple and returns it.
smallest = [min(index) for index in zip(*dataframe)]
biggest = [max(index) for index in zip(*dataframe)]
values = list(zip(smallest, biggest))
print(values)
# for i, x in enumerate(values):
#     print(x[0])         # min in tuple
#     print(x[1])         # max in tuple
# value_range = dict((x,y) for x,y in values) # dobra proba ale tylo dziala do 3-go?
                                            # innny sposob tradycyjnie zmienic, bo wymagany dict
# print(value_range)


print("\n Czy to jest dobrze \n")
# dataframe[y][x]
# normalizacja
df = dataframe # data normalised
for j,y in enumerate(df):
    for i,x in enumerate(values):
        df[j][i] = (df[j][i] - x[0])/(x[1]-x[0])
        #(liczba -min)/max-min
for i, x in enumerate(df):
    print(f'{df[i]}\n')


# grupowanie decyzji
decision1 = [] # klasa decyzyjna 1
decision0 = [] # klasa decyzyjna 0
for item in dataframe:
    if item[-1] == 1:
        decision1.append(item)
    elif item[-1] == 0:
        decision0.append(item)

# euklides, dystans(znormalizowany)
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return distance**(1/2)

#dystans kazdy do kazdego
distance_grid = []
distance_to = []
for i,x in enumerate(df):
    row0 = df[i]
    for row in df:
        distance = euclidean_distance(row0, row)
        distance_to.append(distance)
    distance_grid.append(distance_to)
data = pd.DataFrame(distance_grid)
data.to_csv(set.file_name + ".csv", index=False)

#problem: Porobnujemy do wiersza 0 (to tez zaleta)^ druga petla
# jak zrobic to wszystko na macierzy z rozroznieniem klas/ heatmapa


#TODO: kod poniżej nie dziala
input()
def carthesian_product(list1,list2):
    # Iloczyn kazrtezjanski
    cartesianProduct = []
    for i in list1:
        for j in list2:
            result = (i, j)
            cartesianProduct.append(result)
    print("cartesianProduct = ")
    print(cartesianProduct)
print("\nAAA\n")
carthesian_product(df,df)
input()
def record_value(numerical):
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
    return distance

def real_euklidean(distance1, distance2):
    pass
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
#odjac od siebie odległosci wektow

#Iloczyn kazrtezjanski
list1 = [int(i) for i in input("Enter the first list : ").split()]
list2 = [int(i) for i in input("Enter the second list : ").split()]
carthesian_product(list1,list2)


