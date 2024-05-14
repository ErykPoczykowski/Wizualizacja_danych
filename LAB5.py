import numpy as np

def main():
    # a = np.arange(2)
    # a = np.array([0,1]) # inicializacja tablicy
    # print(a)
    # print(type(a))
    # print(a.dtype)
    # a = np.arange(2, dtype ='int64')
    # print(a.dtype)
    # b = a.astype('float')
    # print(b)
    # print(b.dtype)
    # print(b.shape)
    # print(a.ndim)
    # m = np.array([np.arange(2), np.arange(2)])
    # print(m.shape)
    # print(type(m))
    # zera = np.zeros((5,5))
    # jedynki = np.ones((5, 5))
    # print(zera)
    # print(jedynki)
    # print(zera.dtype)
    # print(jedynki.dtype)
    # pusta = np.empty((2,2))
    # print(pusta)
    # poz_1 = pusta[1,1]
    # poz_2 = pusta[0, 1]
    # print(poz_1)
    # print(poz_2)
    # # macierz = np.array([[]])
    # zad1()
    # zad2()
    # zad3(10)
    # zad4(2,4)
    # zad5(5)
    # zad6()
    # zad7(18)
    # zad8(a,0)
    zad9()



def zad1():
    a = np.arange(1,43,3)
    print(a)


def zad2():
    b = np.array([1.5,2.3,5.7,9.1,8.7])
    c = b.astype('int64')
    print(b)
    print(c)


def zad3(n):
    d = np.ones((n,n))
    x = 1
    for i in range(0,n):
        for j in range(0,n):
            d[i][j]= x
            x +=1
    print(d)


def zad4(n,m):
    a = np.logspace(1, m, num=m, base = n,)
    print(a)


def zad5(n):
    l = np.linspace(n,1,n)
    x = np.diag(l)
    print(x)


def zad7(n):
    x = np.diag(np.ones((n))*2)
    for i in range(1,n+1):
        x += np.diag(np.ones((n - i)) * 2 * i, -i)
        x += np.diag(np.ones((n - i)) * 2 * i, i)
    print(x)


#def zad8():
def zad9():
    def fibonacci(n):
        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib
    def macierz_fib(n):
        fib_sequence = fibonacci(n ** 2)
        macierz = np.array(fib_sequence[:n ** 2]).reshape((n, n))
        return macierz
    print(macierz_fib(5))






main()

