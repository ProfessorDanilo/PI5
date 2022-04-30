''' Marcela na 1º tentativa de colocar o fluxograma em python
Programa para sortear perguntas de uma lista, receber resposta e validar resposta.
Joguinho para aprendizado de verdadeiro, falso, E, Ou
'''

import random

#lista com sentenças verdadeiras
lista_true = ['Peixes vivem na água.',
    'Borboletas voam.',
    'Dinossauros foram extintos.',
    'Pássaros botam ovos. ',
    'Coruja são aves.',
    'Abelhas produzem mel.',
    'Cachorros latem.']

#lista com sentenças verdadeiras
lista_false=['Cachorros têm asas.',
    'Cachorros têm penas.',
    'Borboletas comem peixes.',
    'Arvores correm.',
    'Sapos voam.',
    'Corujas são mamíferos.',
    'Formigas produzem mel.',]

lista_dicas=['A frase é verdadeira ou falsa?',
    'Ambas as frases precisam ser verdadeiras.',
    'Pelo menos uma frase precisa ser verdadeira.',
    'E: ambas as frses precisam ser verdeiras.  OU: pelo menos uma frase precisa ser verdadeira']



#função GERAR PERGUNTAS: sorteia perguntas das listas e retorna resposta correta.
def perguntas():
    fraseTrue = random.choice(lista_true) #sorteia um item aleatorio da lista
    fraseFalse = random.choice(lista_false) #sorteia um item aleatorio da lista
    trueOrFalse = random.randint(0,1)   #sorteia qual das duas listas será usada: 1->fraseTrue 0->fraseFalse
    fraseNao = random.randint(0,1)   #sorteia se a sentança terá o NÃO 1->frase com NÃO 0->frase da lista sem modificação
    respostaCorreta = 0

    if fraseNao == 0:
        if trueOrFalse == 1:
            print (fraseTrue)
            respostaCorreta = 1
            return respostaCorreta
        else:
            print(fraseFalse)
            return respostaCorreta
    else:
        if trueOrFalse == 1:
            posicaoPalavra = fraseTrue.find(' ') #retorna onde termina a primeira palavra da string
            fraseTrue = list(fraseTrue) #transforma string em lista para poder adicionar o não
            fraseTrue.insert(posicaoPalavra,' não') # insere o termo 'nao' na frase
            print(''.join(fraseTrue)) #imprime a lista em forma de string
            return respostaCorreta
        else:
            posicaoPalavra = fraseFalse.find(' ')  # retorna onde termina a primeira palavra da string
            fraseFalse = list(fraseFalse)  # transforma string em lista para poder adicionar o não
            fraseFalse.insert(posicaoPalavra, ' não')  # insere o termo 'nao' na frase
            print(''.join(fraseFalse))  # imprime a lista em forma de string
            respostaCorreta = 1
            return respostaCorreta

def conferirResposta(respostaDada, respostaCorreta, nivel1, pontos1):
    global nivel
    global pontos
    nivel = nivel1
    pontos = pontos1

    if respostaDada == str(respostaCorreta):
        pontos += 10
        print('---------------------------------------------------------------------------')
        print('RESPOSTA CORRETA!!!     VOCE GANHOU 10 PONTOS       Continua...')
        if pontos >= nivel*mudancaNivel:
            nivel += 1
            print('      Parabéns! você conseguiu mudar de nível!!    ')
            print('      Nível: ', nivel)
        print('---------------------------------------------------------------------------')
        continua = input()
    else:
        pontos = (nivel-1)*mudancaNivel
        print()
        print('---------------------------------------------------------------------------')
        print('RESPOSTA INCORRETA!!! VOLTA PARA O INICIO DO NÍVEL')
        print(" DICA: \n     " + lista_dicas[nivel-1] + '   Continua...')
        print('---------------------------------------------------------------------------')
        continua = input()
    return nivel, pontos,


def funcaoE(respostaCorreta1):
    print('E')
    respostaCorreta2 = perguntas()  # sorteia, imprime a pergunta e retorna a resposta correta para ela.
    if respostaCorreta1 and respostaCorreta2 == 1:
        respostaCorreta = 1
    else:
        respostaCorreta = 0
    return respostaCorreta

def funcaoOU(respostaCorreta1):
    print('OU')
    respostaCorreta2 = perguntas()  # sorteia, imprime a pergunta e retorna a resposta correta para ela.
    if respostaCorreta1 or respostaCorreta2 == 1:
        respostaCorreta = 1
    else:
        respostaCorreta = 0
    return respostaCorreta


#variáveis
nivel = 1
pontos = 0
mudancaNivel = 50

print(" ")
while nivel <= 4:
    print('---------------------------- Jogo O ou 1 -----------------------------------')
    print('   Nivel:', nivel,'      Pontos:', pontos, '           FALSO=0  VERDADEIRO=1')
    print('----------------------------------------------------------------------------')
    print()

    respostaCorreta = perguntas()  # sorteia, imprime a pergunta e retorna a resposta correta para ela.

    if nivel == 2:
        respostaCorreta = funcaoE(respostaCorreta)
    elif nivel == 3:
        respostaCorreta = funcaoOU(respostaCorreta)
    elif nivel == 4:
        misturadoEOU = random.randint(0,1)
        if misturadoEOU == 0:
            respostaCorreta = funcaoE(respostaCorreta)
        else:
            respostaCorreta = funcaoOU(respostaCorreta)
    elif nivel >= 5:
        print('PARABÉNS')

    print()

    respostaDada = input("Digite 0 ou 1: ")

    conferirResposta(respostaDada, respostaCorreta, nivel, pontos)
    print()
    print()

print("FIM DO JOGO.")