partidas = list()
jogador = dict()
jogador['nome'] = input(" - Nome do jogador: ")
partidas = int(input(f' - Quantas partidas o {jogador["nome"]} jogou?: '))
gols=[]
for i in range(0, partidas):
        gols.append(int(input(f' - Quantos gols na partida {i} o {jogador['nome']} jogou?: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for i, v in enumerate(jogador["gols"]):
    print(f'    => Na partida {i}, fez {v} gols. ')
print(f' Foi um total de {jogador["total"]} gols.')

print('-='* 40)