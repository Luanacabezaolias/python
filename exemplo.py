
alunos = {}

with open('arquivos.csv','r') as aqruivo:
    cont = 1
    for linha in aqruivo:
        if cont > 1:
            lista = linha.split(',')
            print(lista)
            alunos[int(lista[0])] = lista[1].replace('\n','')
        cont += 1

print(alunos)