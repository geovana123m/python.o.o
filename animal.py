class Animal():
    quantidade_patas = 4
    tem_rabo = False
    tem_pelo = True
    especie = ''

class Cachorro(Animal):
    tem_rabo = True
    especie = 'Canis lupus familiaris'
    raca = 'shitzu'
    nome = 'sergio'
    porte = 'pequeno'

def latir():
    return 'auauauauauau'

def comer():
    return 'nhami'

def dormir():
    return 'ZZZZZZZZZZZ'

