from selectors import SelectSelector

n =input('digite um nome de cidade').strip()
comsantos =n.upper().startswith("SANTO")
if comsantos:
 print("a cidade comeca com 'santo'.")
else:
 print('A cidade nao comeca com "Santo".')