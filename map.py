def menu():
    menu = """
Seleccione el metodo de numeros aleatorios:

Metodo de los cuadrados medios
1) Algoritmo de cuadrados medios. DONE
2) Algoritmo de productos medios. DONE
3) Algoritmo de multiplicador constante. TODO

Algoritmos congruenciales
4) Algoritmo congruencial lineal. DONE
5) Algoritmo congruencial multiplicativo. DONE
6) Algoritmo congruencial aditivo. TODO

Algoritmos congurenciales no lineales
7) Algoritmo congruencial cuadratico. TODO
"""
    while(True):
        print(menu)
        i = input('> ')
        print(i)
        print(algorithm_selected(i)())


def cuadrados_medios():
    seed = int(input("Seed: "))
    N = int(input("N: "))
    yi = pow(seed, 2)
    xi = seed
    result = []
    for x in range(1, N):
        if(yi == 0):
            break
            return result
        elif(len(str(yi)) <= 4):
            xi = int(str(yi))
        elif(len(str(yi)) <= 6):
            xi = int(str(yi)[1:5])
        else:
            xi = int(str(yi)[2:6])

        random_value = xi / 10000
        result.append(random_value)

        yi = pow(xi, 2)
    return result


def productos_medios():
    x1 = 445
    x2 = 445
    N = 4
    yi = x1 * x2
    result = []

    for x in range(1, N):
        if(yi == 0):
            break
            return result
        elif(len(str(yi)) <= 4):
            xi = int(str(yi))
        elif(len(str(yi)) <= 6):
            xi = int(str(yi)[1:5])
        else:
            xi = int(str(yi)[2:6])

        random_value = xi / 10000
        result.append(random_value)

        yi = x2 * xi
        x1 = x2
        x2 = xi
    return result


def algorithm_selected(x):
    return {
        '1': cuadrados_medios,
        '2': productos_medios,
        '3': 2,
        '4': congruencial_lineal,
        '5': congruencial_multiplicativo,
        '6': 2,
        '7': 2,
    }.get(x, 9)


def congruencial_lineal():
    while(True):
        xo = float(input("xo: "))
        k = float(input("k: "))
        g = float(input("g: "))
        c = float(input("c: "))
        a = 1 + 4 * k
        m = pow(2, g)
        module = xo
        ls = []
        for x in range(1, 100):
            xi = (a * module) + c
            module = xi % m
            ls.append(module / (m - 1))
        return ls


def congruencial_multiplicativo():
    while(True):
        xo = float(input("xo: "))
        k = float(input("k: "))
        g = float(input("g: "))
        a = 3 + 8 * k
        m = pow(2, g)
        pv = pow(2, g - 2)
        module = xo
        result = []
        for x in range(1, 100):
            xi = (a * module)
            module = xi % m
            print(module / (m - 1))
        return result


def menu_comprobacion():
    menu = """Pruebas de estadistica
1) Pueba de medias
2) Prueba de varianza
Prueba de uniformidad
3) Prueba chi-cuadrada
4) Prueba de Kolmogorov
Pruebas de independencia
5) Pruebas de corridas arriba y abajo"""
    print(menu)


def main():
    menu()

if __name__ == "__main__":
    main()
