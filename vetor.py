print("***Localizar o maior número do vetor e seu índice ***")

numeros= list(range(10))

for n in range(0,10):
    numeros[n] = int(input("Digite um número: "))

for n in range(0, 10):
    print(numeros[n])

maior=max(numeros)
print("O maior número é: ", maior ," e seu índice é: ", numeros.index(maior))
