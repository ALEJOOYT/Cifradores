import os
import string
import math

alfabeto = list(string.ascii_uppercase)
N = len(alfabeto)

def ModInvertido(a, m):
    a = a % m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def cifrar(palabra, A, B):
    cifrado = ""
    for letra in palabra:
        if letra in alfabeto:
            x = alfabeto.index(letra)
            nuevoIndice = (A * x + B) % N
            cifrado += alfabeto[nuevoIndice]
        else:
            cifrado += letra
    return cifrado

def descifrar(palabra, A, B):
    invA = ModInvertido(A, N)
    descifrado = ""
    for letra in palabra:
        if letra in alfabeto:
            y = alfabeto.index(letra)
            x = (invA * (y - B)) % N
            descifrado += alfabeto[x]
        else:
            descifrado += letra
    return descifrado

def DecifrarFuerzaBruta(palabra, rango):
    print("Iniciando descifrado por fuerza bruta...\n")
    with open("posiblesDecifrados.txt", "w") as archivo:
        for A in range(1, rango + 1):
            if ModInvertido(A, N):
                for B in range(rango + 1):
                    resultado = descifrar(palabra, A, B)
                    linea = f"A = {A}, B = {B}, descifrado = {resultado}\n"
                    archivo.write(linea)
                    print(linea, end="")

def ObtenerCoeficientes():
    while True:
        try:
            A = int(input("Ingrese el coeficiente A: "))
            if math.gcd(A, N) != 1:
                print(f"El coeficiente A ({A}) no es coprimo con {N}. Intente nuevamente.")
                continue
            B = int(input("Ingrese el coeficiente B: "))
            return A, B
        except ValueError:
            print("Error: Los coeficientes deben ser números enteros. Intente nuevamente.")

def MostrarMenu():
    # os.system("cls" if os.name == "nt" else "clear")
    print("=" * 40)
    print("  BIENVENIDO AL SISTEMA DE CIFRADO AFIN")
    print("=" * 40)
    print("1. Cifrar palabra")
    print("2. Descifrar palabra")
    print("3. Descifrar por fuerza bruta")
    print("4. Salir")
    print("=" * 40)

def main():
    while True:
        MostrarMenu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            palabra = input("Ingrese la palabra a cifrar: ").upper()
            A, B = ObtenerCoeficientes()
            resultado = cifrar(palabra, A, B)
            print("Palabra cifrada:", resultado)

        elif opcion == "2":
            palabra = input("Ingrese la palabra a descifrar: ").upper()
            A, B = ObtenerCoeficientes()
            resultado = descifrar(palabra, A, B)
            print("Palabra descifrada:", resultado)

        elif opcion == "3":
            palabra = input("Ingrese la palabra a descifrar: ").upper()
            rango = int(input("Ingrese el rango de búsqueda: "))
            DecifrarFuerzaBruta(palabra, rango)
            print("Los posibles descifrados se han guardado en 'posiblesDecifrados.txt'.")

        elif opcion == "4":
            print("Saliendo del programa...\n")
            break

        else:
            print("Opción inválida, intente nuevamente.")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
