import random
import math
def zad1():
    # zad 1
    A = [x for x in range(1,11)]
    print(A)
    B = [4**x for x in range(0,7) ]
    print(B)
    C = [x for x in B if x%2== 0]
    print(C)


def zad2():
    lista1 = random.sample(range(0,100),10)
    print(lista1)
    lista = [x for x in lista1 if x%2==0]
    print(lista)


def zad3():
    slownik = {"jablko": "sztuki", "ogurek": "kg", "kapusta": "paczki"}
    slownik1 ={key: value for (key, value) in slownik.items() if value == "sztuki"}
    print(slownik)
    print(slownik1)


def zad4():
    a = int(input("podaj dlugosc pierwszego boku trojkata"))
    b = int(input("podaj dlugosc drugiego boku trojkata"))
    c = int(input("podaj dlugosc trzeciego boku trojkata"))
    if a > b and a > c:
        if b**2 + c**2 == a**2:
            print("trojkat jest prostokatny")
        else:
            print("trojkat nie jest prostokatny")
    if b > a and b > c:
        if a**2 + c**2 == b**2:
            print("trojkat jest prostokatny")
        else:
            print("trojkat nie jest prostokatny")
    if c > a and c > b:
        if b**2 + a**2 == c**2:
            print("trojkat jest prostokatny")

        else:
            print("trojkat nie jest prostokatny")


def zad5(a=5, b=5, h=1):
    print(((a+b)*h)/2)


def zad6(a = 1, b = 4,ile = 10):
    lista = [1]
    w = a;
    for i in range(a,ile-1):
        lista.append(w*b)
        w *= b
    print(lista)


def zad7():
    # x = int(input("podaj x: "))
    # a = math.sqrt(x)
    try:
        x = int(input("podaj x: "))
        a = math.sqrt(x)
        print(a)

    except Exception:
        print("liczba nie moze byc ujemna")




def main():
    #zad1()
    #zad2()
    #zad3()
    #zad4()
    #zad5()
    #zad6()
    zad7()


main()
