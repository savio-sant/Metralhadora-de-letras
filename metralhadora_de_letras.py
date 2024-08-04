import time
import unicodedata


#Este script tem o objetivo de criar uma animação com as letras de uma string fornecida
#Chame a função metralhadora_de_letra() passando sua string como parâmetro e observe o output
#Coded by savio.dev.br


def remover_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    return ''.join([c for c in texto_normalizado if not unicodedata.combining(c)])


def metralhadora_de_letra(frase):


    caracteres = list(frase)
    
    print(f"Há {len(caracteres)} caracteres na lista. Que são: {frase} \n")

    alfabeto = [
    "a", "á", "à", "ã", "â", 
    "b", 
    "c", "ç", 
    "d", 
    "e", "é", "ê", 
    "f", 
    "g", 
    "h", 
    "i", "í", 
    "j", 
    "k", 
    "l", 
    "m", 
    "n", 
    "o", "ó", "õ", "ô", 
    "p", 
    "q", 
    "r", 
    "s", 
    "t", 
    "u", "ú", "ü", 
    "v", 
    "w", 
    "x", 
    "y", 
    "z",
    "?", "!", ",", ".",
    " "
]

    lista_string_saida = []

    for x in range(0, len(caracteres)):
        item_atual = caracteres[x]
        posicao_alfabeto = alfabeto.index(item_atual.lower())

        for y in range(0, posicao_alfabeto + 1):
            string_saida = ""
            string_saida = ''.join(lista_string_saida)
            print(f"{string_saida}{remover_acentos(alfabeto[y])}")
            time.sleep(0.01)
            
        lista_string_saida.append(item_atual)
        
        for i in range(0,5):
            print(f"{string_saida}{remover_acentos(alfabeto[y])}")
        

metralhadora_de_letra("Hello Fadminas!!!")