meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'OMG': 'Una palabra para decir que algo es asombroso',
            'CREEPY': 'Una palabra que se utiliza para decir que algo es aterrador',
            'GOD': 'Palabra para decir que algo es genial'
            }
word = input('Escribe cualquier palabra que quieras saber (con mayuscula)' )

if word in meme_dict.keys():
    print (meme_dict[word])
else:
    print ("esta palabra no esta registrada :( ")
