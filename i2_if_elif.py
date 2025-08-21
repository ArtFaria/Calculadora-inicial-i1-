
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