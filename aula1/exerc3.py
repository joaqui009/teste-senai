# Calculadora de IMC

""" 
Solicite o peso em kg e altura do usuario em metros
calcule o IMC ( Indice de Massa Corporal )
peso / (altura * altura)

exibir o IMC
"""

print("Seja bem vindo a calculadora de IMC")
print("Digite o seu peso em KG")
peso = float(input())

print("Digite sua altura em Metros")
altura = float(input())

imc = peso / (altura * altura)

print("O seu IMC é ", imc)