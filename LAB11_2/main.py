import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def zad2():
    x = np.arange(1,20)
    y=1/x

    plt.plot(x,y, 'g:>',label="f(x) = 1/x")
    plt.ylabel("f(x)")
    plt.xlabel("x")
    plt.legend()
    plt.title('Wykres funkcji f(x) dla x [1,20]')
    plt.show()


def zad3():
    x = np.arange(0,30,0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, 'g', label="f(x) = sin(x0")
    plt.plot(x, y2, 'r', label="f(x) = cos(x)")
    plt.ylabel("f(x)")
    plt.xlabel("x")
    plt.legend()
    plt.title('Wykres funkcji f(x) dla x [1,30]')
    plt.show()


def zad4():
    csv = pd.read_csv("iris.csv", sep=",", header=None, names=["sepal_length","sepal_width","petal_length","petal_width","class"])
    x = csv["sepal_length"]
    y = csv["sepal_width"]
    # plt.plot(x, y, 'g.',label="dziwne")
    plt.scatter(x, y, c='c',s=abs(x-y), label="wykres")
    plt.ylabel("sepal_width")
    plt.xlabel("sepal_length")
    plt.legend()
    plt.title('zad 4')
    plt.show()


def zad5():
    csv = pd.read_excel("imiona.xlsx")
    print(csv)
    # fig, axs =plt.sublots(1,3, )
    # x = csv["sepal_length"]
    # y = csv["sepal_width"]
    # # plt.plot(x, y, 'g.',label="dziwne")
    # plt.scatter(x, y, c='c',s=abs(x-y), label="wykres")
    # plt.ylabel("sepal_width")
    # plt.xlabel("sepal_length")
    # plt.legend()
    # plt.title('zad 4')
    # plt.show()
# zad2()
# zad3()
# zad4()
zad5()
