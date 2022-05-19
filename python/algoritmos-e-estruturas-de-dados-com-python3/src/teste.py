nome = "daniel de lima"

print(len(nome))

lista = [1, 2, 3, 4]

print(len(lista))

dic = {"daniel": 47, "lucas": 21, "carla": 35}

#usando um laço for
for chave in dic:
    print(dic[chave])

#numero par
numero = 10

# condicional
if (numero % 2 == 0):
    print("par")
else:
    print("impar")

#laço while
num = 0
while (num < 11):
    print(num)
    num = num + 1

def eh_par(numero):
    if (numero % 2 == 0):
        return True
    return False

print(eh_par(100))