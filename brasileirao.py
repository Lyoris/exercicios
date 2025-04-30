tabela =['internacional', 'corinthians','ceará', 'fortaleza',
         'botafogo', 'flamengo', 'palmeiras', 'juventude', 'fluminense',
         'gremio', 'vasco', 'cruzeiro', 'bahia','sao paulo','bragantino',
         'santos', 'mirassol', 'sport recife', 'atletico mg', 'vitoria'.strip()]
print('-='*20)
print(f'listas de times do brasileirão {tabela}')
print('-='*20)
print('os 5 primeiros da tabela:', end="")
print(tabela[0:5])
print('-='*20)
print('os 5 ultimos da tabela são:', end="")
print(tabela[-5:])
print('-='*20)
print('em ordem alfabetica: ', end="")
tabela.sort()
print(tabela)