import random as r

lista = []
i = 1

while i <=20:
    lista.append(r.randrange(1, 198, 3))
    i = i+1

print(f'Essa foi a lista gerada aleatoriamente: {lista}')


def maior_valor(lista):
    return max(lista, key=int)
m = maior_valor(lista)
print(f'Maior valor é: {m}')