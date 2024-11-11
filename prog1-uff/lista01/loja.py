import math as m

largura = float(input('Digite a largura do local: '))
comprimento = float(input('Digite o comprimento do local: '))
altura = float(input('Digite a altura do local: '))

areaPiso = largura*comprimento
areaTotal = (2*altura*largura)+(2*altura*comprimento)+(2*largura*comprimento)-areaPiso 
latasTinta = m.ceil(areaTotal/54)
custoTinta = latasTinta*215
horasPintor = m.ceil(areaTotal/8)
custoPintor = horasPintor*60
rolosDeTinta = horasPintor*2
custoRolos = rolosDeTinta*12

print('Área total da loja: ', (areaTotal), 'm²')
print('Tempo de duração da reforma:', (horasPintor), 'horas')
print('Quantidade de latas de tinta:', (latasTinta))
print('Quantidade de rolos utilizados:', (rolosDeTinta))
print('Valor do material:', (custoTinta+custoRolos), 'reais')
print('Valor da mão de obra:', (custoPintor), 'reais')
print('Valor total da reforma: ', (custoTinta+custoRolos+custoPintor), 'reais')