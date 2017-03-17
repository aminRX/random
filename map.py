def menu():
    menu = """
Seleccione el metodo de numeros aleatorios:

Metodo de los cuadrados medios
1) Algoritmo de cuadrados medios.
2) Algoritmo de productos medios.
3) Algoritmo de multiplicador constante.

Algoritmos congruenciales
4) Algoritmo congruencial lineal.
5) Algoritmo congruencial multiplicativo.
6) Algoritmo congruencial aditivo.

Algoritmos congurenciales no lineales
7) Algoritmo congruencial cuadratico."""
    while(True):
        print(menu)
        i = input('> ')
        print(algorithm_selected(i))


def algorithm_selected(x):
    return {
        '1': 1,
        '2': 2,
        '3': 2,
        '4': congruencial_lineal(),
        '5': 2,
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
        break


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
