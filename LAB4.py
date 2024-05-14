import math
import random


def zad1():
    a = ((math.e)**4 - math.log(34,2)) ** (1 / 3)
    print(round(a,2))
    b = (math.log(20) + math.cos(45) + math.e) ** (1 / 3)
    print(round(b,2))
    c = ((math.log(20,3)+  math.sin(45) * (5/8))) ** (1 / 4)
    print(round(c,2))
    d = math.log(23,3)+(math.sin(34)+5) ** (1 / 3)
    print(round(d,2))
    e = (math.log(32,2) + math.pi + math.sin(56)) ** (1 / 4)
    print(round(e,2))


def zad2():
    a = 1;
    n = int(input("podaj wysokosc wiezy: "))
    if n < 0:
        print("podano ujemna wartosc")
    elif n > 10:
        print("podano wartosc wieksza od 10")
    else:
        for i in range(1,n+1):
            print("A"*i)


def zad3():
    n = int(input("wpisz wysokosc piramidy: "))
    if n > 10:
        print("liczba wieksza od 10")
    elif n < 0:
        print("liczba ujemna")
    else:
        for i in range(1, n + 1):
            print(" " * (n - i) + "A" * i + "A"*(i-1))


def zad5():
    n = int(input("wpisz ilosc wierszy: "))
    matrix = []
    for i in range(n):
        wiersz = [random.randint(1,10) for i in range(n)]
        matrix.append(wiersz)
    suma_wierszy = [sum(wiersz) for wiersz in matrix]

    print(f"{suma_wierszy} - suma poszczegolnych wierszy")
    print(f"{matrix} - cala macierz")


def zad6():
    a = int(input("liczba do podniesienia: "))
    b = int(input("liczba podnosząca: "))
    print(a**b)
    print(len(str(a**b)))
    napis = str(a**b)
    print(napis[-1])


def main():
    #zad1()
    #zad2()
    #zad3()
    #zad5()
    zad6()



main()
