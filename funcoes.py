def verificasetriangulo(numero1, numero2, numero3):
    if (numero1 + numero3) >= numero2 and (numero2 + numero1) >= numero3 and (numero3 + numero2) >= numero1:
        return 1
    return 0


if verificasetriangulo(1, 1, 1) == 1:
    print("É triângulo")

else:
    print("Não é triângulo")


def tipotriangulo(numero1, numero2, numero3):
    if verificasetriangulo(numero1, numero2, numero3) == 1:

        if numero1 == numero2 and numero2 == numero3:
            print("É equilátero")
        else:
            if numero1 != numero2 and numero2 != numero3 and numero1 != numero3:
                print("É escaleno")
            else:
                print("É isósceles")

    else:
        print("Não é triângulo")

lado1 = int(input("Insira o valo do lado 1 "))
lado2 = int(input("Insira o valo do lado 2 "))
lado3 = int(input("Insira o valo do lado 3 "))

tipotriangulo(lado1,lado2,lado3)