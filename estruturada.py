nomes = []
notas1 = []
notas2 = []

def cadastrar():
    nome = input("nome do estudante: ")
    nota1 = float(input("nota 1:")) # casting (to cast)
    nota2 = float(input("nota 2:"))

    nomes.append(nome)
    notas1.append(nota1)
    notas2.append(nota2)
    print("estudante  cadastrado")

def calcular_media(indice):
    return ((notas1 [indice] + notas2 [indice]) /2 )

def situacao(indice):
    media = calcular_media(indice)
    if media >= 6:s
        return "aprovado"
    elif media >= 4:
        return "reuperação"
    return "reprovado"

def listar():
    if len(nomes == 0):
        print("nehum estudante cadastrado")
        return

    print(f"\n{'nome':<16}{'n1':<7}{'n2':<7}{'media':<8}{'situação':<8}")

    for i in range(len(nomes)):
        print(f"{nomes[i]:<16:}{notas1[i]:<7}{notas2[i]:<7}"f"{calcular_media(i):<8.1f}{situacao(i):<14}")

def media_da_turma():
    if len(nomes) ==0:
        print("nenhum estudante cadastrado")
        return

    soma = 0
    for i in range(len(nomes)):
        soma = soma + calcular_media(i)
        print(f"\nmédia da turma: {soma / len(nomes):.2f}")

def menu():
    while True:
        print("\n1 - cadastrar estudante")
        print("2 - listar estudante")
        print("3 - média da turma")
        print("0 - sair")

        opcao = input("opção: ")


        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            media_da_turma()
        elif opcao == "0":
            break
        else:
            print("opção invalida. ")

menu()
