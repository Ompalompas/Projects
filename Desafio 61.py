print('GERADOR DE P.A.')
print(10*'=-')

primeiro=int(input('Primeiro termo: '))

razão=int(input('Razão: '))

termo=primeiro

c=1
while c <= 10:

    print('{} '.format(termo), end=' ')
    termo+=razão
    c+=1

print('ACABOU')