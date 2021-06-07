class Pessoa:
    def crescer(self):
        pessoa.altura = pessoa.altura + ((pessoa.idade / pessoa.idade) * float(0.5))
        print(format(pessoa.nome), ",a sua altura é: ",
              float(pessoa.altura), "cm", "e está com", pessoa.idade, "anos")

    def envelhecer(self):
        for i in range(pessoa.idade, 20):
            pessoa.idade = pessoa.idade + 1
            if pessoa.idade < 21:
                pessoa.crescer()

        if pessoa.idade >= 21:
            print(format(pessoa.nome), ", a fase de crescimento se encerra aos 21 anos")

    def emagrecer(self):
        if pessoa.peso / ((pessoa.altura/100) ** 2) > 25:
            print("Você precisa emagrecer,seu IMC está acima de 25!")



    def engordar(self):
        if pessoa.peso / ((pessoa.altura/100) ** 2) < 18.5:
            print("Você precisa engordar!, seu IMC está abaixo de 18.5")
        else:
            print("Você não precisa emagrecer")


pass

print("------", " Classes e métodos ", "------  \n")

pessoa = Pessoa()
pessoa.nome = input("Digite o seu nome: ")
pessoa.idade = int(input("Qual a sua idade? : "))
pessoa.peso = float(input("Qual o seu peso? : "))
pessoa.altura = int(input("Qual a sua altura? : "))
pessoa.envelhecer()
pessoa.engordar()
pessoa.emagrecer()
