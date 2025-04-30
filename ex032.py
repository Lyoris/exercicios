ano =int(input('digite um ano qualquer ou o atual'))
if (ano % 4 ==0 and ano % 100 !=0) or (ano % 400 ==0):
    print(f'o ano {ano} é um ano bissexto!')
else:
    print(f'o ano {ano} não é um ano bissexto!')
