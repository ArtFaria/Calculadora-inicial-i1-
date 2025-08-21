
from sympy import sympify
#importei especificamente a função sympify

#recebe as expressões digitadas pelo usuário
soma = input("Coloque aqui seus valores de soma (Ex: 1+1):")
multiplicacao = input("Coloque aqui seus valores de multiplicação (Ex: 4*4):")  
divisao = input("Coloque aqui seus valores de divisão (Ex: 30/3):")
potencia = input("Coloque aqui seus valores de potência (Ex: 7**2):")

#usa o sympy para calcular as expressões
print("Soma:", sympify(soma))
print("Multiplicação:", sympify(multiplicacao))
print("Divisão:", sympify(divisao))
print("Potência:", sympify(potencia))