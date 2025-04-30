from dataclasses import replace

nome =str(input('digite o nome completo')).strip()
print('nome em maiusculas:', nome.upper())
print('nome em minusculas:', nome.lower())
total =(len(nome) - nome.count(' '))
print('total de letras:',total)
prim =nome.split()[0]
print('primeiro nome',len(prim))
