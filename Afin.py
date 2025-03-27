alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def ModInvertido(a, m):
    a = a % m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def Cifrar(palabra, A, B):
    cifrado = ""
    for letra in palabra:
        if letra in alfabeto:
            x = alfabeto.index(letra)
            # segun mi formula c = (A * x + B) mod 26
            nuevoIndice = (A * x + B) % 26
            cifrado += alfabeto[nuevoIndice]
        else:
            cifrado += letra
    return cifrado

def Descifrar(palabra, A, B):
    descifrado = ""
    invA = ModInvertido(A, 26)
    if invA is None:
        print("El coeficiente A no tiene inverso módulo 26. No se puede descifrar.")
        return ""
    for letra in palabra:
        if letra in alfabeto:
            y = alfabeto.index(letra)
            # segun mi formula x = invA * (y - B) mod 26
            x = (invA * ((y - B) % 26)) % 26
            descifrado += alfabeto[x]
        else:
            descifrado += letra
    return descifrado

def DescifrarFuerzaBruta(palabra):
    print("Iniciando descifrado por fuerza bruta...\n")
    for A in range(1, 26):
        invA = ModInvertido(A, 26)
        if invA is not None:
            for B in range(26):
                descifrado = Descifrar(palabra, A, B)
                print("A = " + str(A) + ", B = " + str(B) + " descifrado = " + descifrado)

def main():
    while True:
        accion = input("Ingrese 'cifrar' para cifrar, 'descifrar' para descifrar o cualquier otra tecla para salir: ").strip().lower()
        if accion == "cifrar":
            palabra = input("Ingrese la palabra: ").upper()
            try:
                coeficiente_a = int(input("Ingrese el coeficiente A: "))
                coeficiente_b = int(input("Ingrese el coeficiente B: "))
                resultado = Cifrar(palabra, coeficiente_a, coeficiente_b)
                print("Palabra cifrada:", resultado)
            except ValueError:
                print("Error: Los coeficientes deben ser números enteros.")
        elif accion == "descifrar":
            descifrar_fuerza_bruta = input("¿Desea descifrar por fuerza bruta? (s/n): ").strip().lower()
            palabra = input("Ingrese la palabra: ").upper()

            if descifrar_fuerza_bruta == "s":
                DescifrarFuerzaBruta(palabra)
            else:
                try:
                    coeficiente_a = int(input("Ingrese el coeficiente A: "))
                    coeficiente_b = int(input("Ingrese el coeficiente B: "))
                    resultado = Descifrar(palabra, coeficiente_a, coeficiente_b)
                    print("Palabra descifrada:", resultado)
                except ValueError:
                    print("Error: Los coeficientes deben ser números enteros.")
        else:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()