km =float(input('qual a velocidade atual do carro?'))
if km > 80:
    print('parabens, voce foi multado e receberá R$7 por cada km acima da velocidade!')
    m = 7 * (km - 80)
    print('você deve pagar uma multa de R${:.2f}'.format(m))
print('tenha um bom dia! dirija com segurança')
