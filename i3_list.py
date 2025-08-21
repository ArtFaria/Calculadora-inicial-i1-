notas = []

for x in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota: "))
    resultado = [nome, nota]
    notas.append(resultado)
    print("Quantidade de notas:", len(notas))
#Recebe os nomes e notas

for n in notas:
    nome = n[0]
    nota = n[1] 
    print("Nome:", nome, "tirou a nota:", nota)
#Exibie os nomes e suas notas
