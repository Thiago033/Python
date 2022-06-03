aluno = dict()
classe = list()

for i in range(0,3):
    aluno['nome'] = str(input('Digite o nome: '))
    aluno['media'] = str(input('Digite a media do aluno: '))
    classe.append(aluno.copy())

for alu in classe:  
    for k, v in alu.items():
        print(f'{k} do aluno eh: {v}.')