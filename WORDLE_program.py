from funcao_wordle import *
import random
reiniciar = True
while reiniciar: #boas vindas do jogo
    print_slow_asc('''
    ██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ███████╗
    ██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝
    ██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     █████╗  
    ██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██╔══╝  
    ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗███████╗
    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝
    ''')
    print_slow('\nBem vind@ ao jogo WORDLE.')
    print()
    print_slow('\nVoce precisa acertar a palavra em 6 tentativas.')
    print()
    print_slow('\nPara te ajudar vamos te dar algumas dicas.')
    print()
    print_slow('\nA palavra sorteada e a palavra a ser digitada devem ser palavras de 5 letras.')
    print()
    print_slow('\nO símbolo 🟩  indicará que a letra pertence a palavra e está na posição correta.')
    print()
    print_slow('\nO símbolo 🟨  indicará que a letra pertence a palavra mas nao está na posição correta.')
    print()
    print_slow('\nO símbolo ⬜  indicará que a letra não pertence a palavra .')
    print()
    time.sleep(1)
    teclado = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    teclado_novo = dict()
    for teclas in teclado:
        teclado_novo[teclas] = '⬜ '
    continuar = True
    tentativas = 1
    chute = True
    palavra_secreta = random.choice(lista_filtrada)
    print(palavra_secreta)
    palavra_secreta2 = remove_acentos(palavra_secreta)
    while continuar:
        while chute:#loop para o usuario digitar uma palavra,e caso ele digite uma palavra invalida,ele possa digitar uma nova .
            print()
            palavra_chute = input('Faça o seu chute:').lower() #comando para o usuario digitar uma palavra-chute.
            print()
            if len(palavra_chute) != 5: #condição para o usuario digitar somente palavras que contem 5 letras.
                print_slow('\nVoce precisa digitar uma palavra com 5 letras.')
                print()
                chute = True
            else:
                if palavra_chute not in lista_filtrada: #condiçao que diz que o usuario so pode digitar palavras que sao validas,ou seja, estao na lista de palavras passadas pelo handout.
                    print_slow('\nVoce digitou uma palavra inválida.')
                    print()
                    chute = True
                else:
                    chute = False
        if palavra_chute == palavra_secreta: #condicao caso o usuario acerte a palavra-chave.
            print_slow(f'\nParabens!! Voce acertou a palavra ({palavra_secreta}) em {tentativas} tentativas')
            print()
            continuar = input('Voce deseja jogar novamente?(s) sim - (n) nao')# comando para o usuario escolher se ele quer jogar novamente ou não.
            if continuar == 's':
                tentativas = 1
                reiniciar = True
                continuar = False
                chute = False
            elif continuar == 'n':
                print_slow('\nObrigado por ter jogado!! FIM')
                print()
                continuar = False
                chute = False
                reiniciar = False
        elif tentativas == 6: #condicao caso o usuario ultrapasse a quantidade maxima de tentativas, e entao ele pode escolher jogar novamente ou não.
            print()
            print(compara_palavras(palavra_chute,palavra_secreta2))
            print()
            print(atualiza_teclado(palavra_chute,palavra_secreta2,teclado))
            print()
            print_slow(f'\nInfelizmente acabaram suas tentativas campeão :( , a palavra era ({palavra_secreta})')
            print()
            continuar = input('Voce deseja jogar novamente? (s) sim - (n) nao')
            if continuar == 's':
                tentativas = 1
                reiniciar = True
                continuar = False
                chute = False
            elif continuar == 'n':
                print_slow('\nObrigado por ter jogado!! FIM')
                print()
                continuar = False
                chute = False
                reiniciar = False
        else: # condicao para o programa executar a funcao que compara a palavra digitada pelo usuario e a palavra escolhida aleatoriamente pelo programa.
            print()
            print(compara_palavras(palavra_chute,palavra_secreta2))
            print()
            print(atualiza_teclado(palavra_chute,palavra_secreta2,teclado_novo))
            print()
            tentativas += 1 
            continuar = True
            chute = True
            reiniciar = False
