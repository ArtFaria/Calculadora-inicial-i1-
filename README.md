# Projetos Iniciais Simples em Python
Repositório criado para praticar conceitos básicos de Python. Contém scripts simples, pequenos exercícios e alguns notebooks de apoio. 


# "Mini Calculadora" feita em python utilizando o comando sympify da sympy library.
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

#Utilização do if, elif e else

nome = input("Qual é o seu nome?")
idade = int(input("Qual é a sua idade?"))
salario = float(input("Qual é o seu salário?"))

# Verificação de idade
if idade <= 18:
    print(f"{nome}, você NÃO PODE entrar!")
else:
    print(f"{nome}, você PODE entrar!")

# Verificação de salário
if salario < 1000:
    print(f"{nome}, você NÃO PODE ter acesso ao sistema!")
elif salario > 1000 and salario <=3000:
    print(f"{nome}, você PODE ter acesso ao sistema, mas com restrições!")
elif salario >3000 and salario <=5000:
    print(f"{nome}, você PODE ter acesso ao sistema completo")
else:
    print(f"{nome}, você PODE ter acesso ao sistema completo e ainda ganhar um bônus!")
