frase =input('digite uma frase').strip().upper()
q = frase.count("A")
p =frase.find("A")+1
u =frase.rfind("A")-1 
print('a letra A aparece {} vez(es).\n a letra A aparece na primeira posicao  na {}° posição\n a letra A aparece na ultima posicao na {}° posição'.format(q, p,u))
