import matplotlib.pyplot as plt
import math


def a(n: int) -> float:
    '''сюда надо ручками вписать полученную интегрированием an функцию от n'''
    return 4/((math.pi * n) ** 2)  
def b(n: int) -> float:
    '''#сюда надо ручками вписать полученную интегрированием bn функцию от n'''
    return -4 / (math.pi * n) + 2 / (math.pi * n) ** 3 

def get_points(a0: float, x1: int, x2: int, n: int) -> list[float]:
    X = []
    Y = []
    x = x1
    l =  ((x2 - x1) / 2)
    while x <= x2:
        y = a0 / 2
        for n in range(1,n+1):
            y += a(n) * math.cos(math.pi * n * x / l) + b(n) * math.sin(math.pi * n * x / l)
        X.append(x)
        Y.append(y)
        x += 0.01
    return X, Y  
def draw(X: list[float], Y: list[float]):  
    plt.grid() 
    ax = plt.gca()
    ax.set_aspect("equal")   
    plt.plot(X, Y)
    plt.title(f'n = {n}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
if __name__ == "__main__":
    x1 = 0 #левая граница
    x2 = 2 #нижняя граница
    n = 100         
    a0 = 8/3     
    X,Y = get_points(a0, x1, x2, n)
    draw(X,Y)
