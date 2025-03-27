
# Verificar se é impar ou par

""" 
Digite um numero inteiro
Verifique se o numero é impar ou par
Escreva a mensagem correspondente
"""

print("Seja bem vindo ao sistema imporpar")
print("Digite o numero correspondente")
numero = int(input())

resto = numero % 2 # 10 / 2 = 0

if resto != 0:
    print("e um numero impar")
else:
    print("e um numero par")

    