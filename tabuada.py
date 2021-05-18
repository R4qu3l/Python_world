print("----------------------Tabuada---------------------")
numero=int(input("Desejo ver a tabuada do número... "))
print("Tabuada do número {}".format(numero))

for i in range(1, 11):
    print(i, "x", numero,"=", numero*i)