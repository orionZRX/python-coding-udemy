# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  M a r l o n
# -6-5-4-3-2-1
# nome = 'Marlon'
# print(nome[2])
# print(nome[-4])
# print('l' in nome)
# print('-' * 10)
# print('ar' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
