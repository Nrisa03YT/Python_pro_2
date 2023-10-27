meme_dict = {
    'CRINGE': 'Pena Ajena',
    'LOL': 'Una respuesta común a algo gracioso',
    'ROFL':  'una respuesta a una broma',
    'SHEESH': 'Ligera desaprobación',
    'CREEPY': 'aterrador, siniestro',
    'AGGRO': 'ponerse agresivo/enojado'
    }

word = input("escribe la palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])

else:
    # ¿Qué debemos hacer si no se encuentra la palabra?
    print('Tu palabra no está, lo siento')