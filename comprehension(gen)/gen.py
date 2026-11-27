#generation expression(não é tupla)
from tornado import gen

gen = (x ** 2 for x in range(6))
print('='* 30)
print(f'1- definição de generator: {gen}')

print(tuple(gen))
print('='*30)

print(f'2- definição de lista em generator: {list(gen)}')
print('='*30)
print(f'3- definição de tupla em generator: {(tuple(gen))}')
print('='*30)
print(dict(gen))
quadrados = tuple (x ** 2 for x in range(6))
print(quadrados)
