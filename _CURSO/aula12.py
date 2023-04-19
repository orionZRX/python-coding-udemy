nome = 'Marlon Bartz'
altura = 1.83
peso = 76
# imc = peso em kg / (altura em metros ** 2)
imc = round(peso / (altura ** 2))

print(f'{nome} tem de {altura},\n'
      f'pesa {peso} kg e seu IMC é\n{imc}')
