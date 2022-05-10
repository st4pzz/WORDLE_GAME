import unicodedata
import sys
import time
from texto import string_palavras #importanto o texto de todas as palavras fornecidas pelo handout para a realização do exercício.
lista_palavras = string_palavras.split()
lista_filtrada = list()
for palavras in lista_palavras: # filtrando todas as palavras que contem 5 letras para uma nova lista
    if len(palavras) == 5:
        lista_filtrada.append(palavras)

def print_slow(str): # funçao que pega uma frase e imprime ela de pouco em pouco e nao de uma vez só.
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

def print_slow_asc(str): # funçao que pega a arte que fiz pelo ASCII e imprime ela de pouco em pouco e nao de uma vez só.
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.001)

def remove_acentos(s): #funcao utilizada de outro exercicio para remover os acentos de uma palavra.
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def compara_palavras(palavra_chute,palavra_secreta): #funcao para substituir os elementos de uma lista ja criada e adicionar outros elementos de acordo com as regras do jogo.
    lista_troca = list()
    lista_compara = list()
    for letra_chute,letra_secreta in zip(palavra_chute,palavra_secreta):
        if letra_chute in lista_compara:
            lista_troca.append('⬜ ')
        elif letra_chute == letra_secreta:
            
            lista_troca.append('🟩 ')
            
        elif letra_chute != letra_secreta and letra_chute in palavra_secreta:
            lista_troca.append('🟨 ')
        else:
            lista_troca.append('⬜ ')
        lista_compara.append(letra_chute)
        
    return ' '.join(lista_troca)

def atualiza_teclado(palavra_chute,palavra_secreta,teclado_novo):#deleta as letras do teclado caso o usuario acerte a letra na posicao correta.
    for letra_chute,letra_secreta in zip(palavra_chute,palavra_secreta):
        
        if letra_chute == letra_secreta:
            teclado_novo.pop(letra_chute)
            teclado_novo[letra_chute] = '🟩 '
        elif letra_chute != letra_secreta and letra_chute in palavra_secreta:
            teclado_novo.pop(letra_chute)
            teclado_novo[letra_chute] = '🟨 '
        else:
            pass
    return teclado_novo
