nome = 'Marlon Bartz'
altura = 1.83
peso = 76
# imc = peso em kg / (altura em metros ** 2)
imc = peso / (altura ** 2)

print(f'{nome} tem de {altura:,.2f}m de altura,\n'
      f'pesa {peso:.1f} kg e seu IMC é\n{imc:.1f}')
