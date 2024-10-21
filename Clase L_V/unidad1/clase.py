#print('py','52','48', sep=',')

dat = 'celular'
if dat.find ('celular')>=0:
    print('encontrado')
else:
    print('nada')

men = 'manjios manning'
ej = men[0:6]
print(ej)

i = 0

while i < 5:

    i += 1

    if i == 4:

        continue

    print("contador: ", i)
print('---------------------------')
i = 0

while i < 5:

    i += 1

    if i == 4:

        break

    print("contador: ", i)