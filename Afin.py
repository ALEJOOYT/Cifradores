import os
import string
import math

alfabeto = list(string.ascii_uppercase)  # Alfabeto dinámico
N = len(alfabeto)  # Tamaño del alfabeto

def mod_invertido(a, m):
    """ Calcula el inverso modular de a módulo m si existe. """
    a = a % m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def cifrar(palabra, A, B):
    if math.gcd(A, N) != 1:
        print(f"El coeficiente A ({A}) no es coprimo con {N}. No se puede cifrar.")
        return ""
    cifrado = ""
    for letra in palabra:
        if letra in alfabeto:
            x = alfabeto.index(letra)
            nuevo_indice = (A * x + B) % N
            cifrado += alfabeto[nuevo_indice]
        else:
            cifrado += letra
    return cifrado

def descifrar(palabra, A, B):
    invA = mod_invertido(A, N)
    if invA is None:
        print(f"El coeficiente A ({A}) no tiene inverso módulo {N}. No se puede descifrar.")
        return ""
    descifrado = ""
    for letra in palabra:
        if letra in alfabeto:
            y = alfabeto.index(letra)
            x = (invA * (y - B)) % N
            descifrado += alfabeto[x]
        else:
            descifrado += letra
    return descifrado

def descifrar_fuerza_bruta(palabra):
    print("Iniciando descifrado por fuerza bruta...\n")
    for A in range(1, N):
        if mod_invertido(A, N):
            for B in range(N):
                print(f"A = {A}, B = {B}, descifrado = {descifrar(palabra, A, B)}")

def mostrar_menu():
    os.system("cls" if os.name == "nt" else "clear")
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
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            palabra = input("Ingrese la palabra a cifrar: ").upper()
            try:
                A = int(input("Ingrese el coeficiente A: "))
                B = int(input("Ingrese el coeficiente B: "))
                resultado = cifrar(palabra, A, B)
                print("Palabra cifrada:", resultado)
            except ValueError:
                print("Error: Los coeficientes deben ser números enteros.")

        elif opcion == "2":
            palabra = input("Ingrese la palabra a descifrar: ").upper()
            try:
                A = int(input("Ingrese el coeficiente A: "))
                B = int(input("Ingrese el coeficiente B: "))
                resultado = descifrar(palabra, A, B)
                print("Palabra descifrada:", resultado)
            except ValueError:
                print("Error: Los coeficientes deben ser números enteros.")

        elif opcion == "3":
            palabra = input("Ingrese la palabra a descifrar: ").upper()
            descifrar_fuerza_bruta(palabra)

        elif opcion == "4":
            print("Saliendo del programa...\n")
            break

        else:
            print("Opción inválida, intente nuevamente.")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()