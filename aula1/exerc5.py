
# Numeros Pares em um Intervalo

""" 
Solicite dois números inteiros ao usuário
Representando o inicio e o fim de um intervalo
Mostre todos os numeros pares nesse intervalo
(incluindo limite inicial e final, se forem pares)
"""

n1 = int(input("Digite o numero 1"))
n2 = int(input("Digite o numero 2"))

for y in range(n1, n2 + 1):
    if y % 2 == 0: 
        print("o Numero é par: ", y)
