from re import T
#enconding: utf-8

edad = 60
m_edad = 18

if edad >= m_edad:
    print("Mayor de Edad")
    if True:
        print ('Se valido que es mayor')
    else:
        print ('se valido ')
else:
    print("Es menor de edad")
print("Termine")

#################################################
if edad >= 0 and edad < 18:
    print ('Es un niño')
elif edad >= 18 and edad < 27:
    print('Sos un joven')
elif edad >= 27 and edad < 60:
    print ('Sos Adulo')
else:
    print('Sos de la 3ra edad')