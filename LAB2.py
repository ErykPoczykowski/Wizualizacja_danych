import sys
#lista =[1,2,4,5.6,'a',[12,11],3+2j]
#print(lista)
#lista.append(8)
#print(lista)
#lista.insert(3,7)
#print(lista)
#lista.pop()
#print(lista)
#lista.pop(1)
#print(lista)
#lista.remove(7)
#print(lista)
#lista.reverse()
#print(lista)
#lista2=[6,4,8.5,3.12,5,8,10]
#print(lista2)
#lista2.sort()
#print(lista2)
#del lista[3]
#print(lista)

#znaki ='abcde'
#print(znaki[0])

#slownik ={'a':1,'b':2,'c':3,'d':4,'e':5}
#print(slownik)
#print(slownik['a'])
#slownik.pop('e')
#print(slownik)
#print(slownik.keys())
#print(slownik.values())

# liczba = input('wprowadz liczbe: ')
# print(f'{liczba} to wczytana liczba')

# sys.stdout.write("wprowadz liczbe: ")
# liczba = sys.stdin.readline()
# print(type(liczba))
# liczba = int(liczba)
# print(type(liczba))
# print(f'{liczba} to wczytana liczba')

#a = int(input())
#b = int(input())
#if a > b:
#    print(a)
#else:
#    print(b)

#if a ==b:
#    print(a+b)
#else:
#    print("liczby nierowne")

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (a>b) & (c>d):
#     print(a+c)
# else:
#     print(b+d)

# for i in range(0,6,1):
#     print(i)
#
# for item in lista2:
#     print(item)
# else:
#     print('')
#     print(len(lista2))

# licznik = 0
# while licznik <10:
#     print(licznik)
#     licznik +=1

# zad 0.1
# lista3 = [1,4,2,8,16,5,13]
# a = int(input("podaj liczbe: "))
# licznik = 0
# while licznik < len(lista3):
#     if a*a == lista3[licznik]:
#         print("znajduje sie")
#         break
#     licznik +=1
# else:
#     print("nie znajduje sie")

def zad_1():
    slowo = input("podaj zdanie: ")
    licznik = 0
    ilosc = 1
    while licznik < len(slowo):
        if slowo[licznik] == " ":
            ilosc +=1
        licznik +=1
    print(ilosc)

def zad_2():
    sys.stdout.write("wprowadz 1 liczbe: ")
    a = sys.stdin.readline()
    a = int(a)
    sys.stdout.write("wprowadz 2 liczbe: ")
    b = sys.stdin.readline()
    b = int(b)
    sys.stdout.write("wprowadz 3 liczbe: ")
    c = sys.stdin.readline()
    c = int(c)
    print(a**b+c)


def zad_3_1():
    napis = input("podaj slowo: ")
    licznik = int(0)
    dlugosc = int(len(napis))
    while licznik < dlugosc:
        if napis[licznik] != napis[dlugosc-1-licznik]:
            print(f"{napis} nie jest palindromem")
            break
        licznik +=1
    else:
        print(f"{napis} jest palindromem")

def zad_3_2_n():
    napis = input("podaj slowo: ")
    lista = []
    licznik = int(0)
    while licznik < len(napis):
        lista[licznik] = napis[licznik]
        licznik +=1
    print(lista)


def zad_4():
    liczba = int(input("wszytaj liczbe: "))
    licznik1 = 2
    while licznik1 < liczba:
        if liczba % licznik1 == 0:
            print(f"{liczba} nie jest pierwsza")
            break
        licznik1 +=1
    else:
        print(f"{liczba} jest pierwsza")


# def zad_5_n():
#     licznik1 = 1
#     licznik2 = 1
#     while licznik1 <=1000:
#         while licznik2 < licznik1:
#             if licznik


def zad_6():
    lista = [1,2,3,4,5.5,6.6,7.7,8]
    l = 0
    for i in lista:
        lista[l] = i**2
        l +=1
    print(lista)


def zad_7():
    licznik = 0
    lista = []
    while licznik < 10:
        a = int(input(f"podaj {licznik+1} liczbe: "))
        if a % 2 ==0:
            lista.append(a)
        licznik +=1
    else:
        print(lista)


def zad_8():
    lista = ["a","a","a",1,2,2,2,2,3,3,4.5,"ala"]
    slownik = {"a": 0, 1: 0, 2: 0, 3: 0, 4.5: 0, "ala": 0}
    print(slownik)
    licznik = 1
    dlugosc = int(len(lista))
    zapis = 0
    while licznik < dlugosc:
        zapis = lista[licznik-1]
        if lista[licznik] == zapis:
            slownik[zapis] +=1
        else:





# zad_1()
# zad_2()
# zad_3_1()
# zad_3_2_n()
# zad_4()
# zad_5_n()
# zad_6()
# zad_7()
zad_8()