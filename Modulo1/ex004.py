import random

jogador = dict()
ganhadores = list()

for i in range(0,5):
    jogador['nome'] = 'jorge'
    jogador['dado'] = random.randint(1,6)
    ganhadores.append(jogador.copy())
    
for jogador in ganhadores:
    for k,v in jogador:




for jogador in ganhadores:
    for k,v in jogador:
        print(f'Nome: {k} Dado: {v}')