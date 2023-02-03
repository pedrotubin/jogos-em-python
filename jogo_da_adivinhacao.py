import random

def mensagem_inicial():
    print('-'*30)
    print('JOGO DA ADIVINHAÇÃO'.center(30))
    print('-'*30)

def obter_dificuldade():
    print('Qual o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')
    nivel = str(input('Defina o nível: ')).strip()
    while not (nivel.isnumeric() and nivel in '123'):
        print('Entrada inválida.')
        print()
        print('(1) Fácil (2) Médio (3) Difícil')
        nivel = str(input('Defina o nível: ')).strip()
    print()
    return nivel

def define_tentativas(nivel=1):
    match int(nivel):
        case 1:
            tentativas = 20
        case 2:
            tentativas = 10
        case 3:
            tentativas = 5
    return tentativas

def entra_numero():
    valido = False
    while not valido:
        tent = str(input('Digite: ')).strip()
        valido = (int(tent) in range(100)) if tent.isnumeric() else False
        if not valido:
            print('Entrada inválida. ', end='')
    tent = int(tent)

    return tent

def jogar():
    
    mensagem_inicial()
    nivel = obter_dificuldade()
    tentativas = define_tentativas(nivel)

    numero = random.randint(1,100)
    print('Pensei em um número de 1 a 100. Tente adivinhar!')

    rodada = 1
    venceu = False
    pontuacao = 1000

    while (not venceu) and (rodada != tentativas):
        print(f'Rodada {rodada} de {tentativas}.')
        tent = entra_numero()

        maior = tent > numero
        menor = tent < numero
        venceu = tent == numero

        if maior:
            print('O número que você digitou é MAIOR que o que eu pensei.')
        if menor:
            print('O numero que você digitou é MENOR que o que eu pensei.')

        pontuacao -=  abs(tent - numero)
        rodada +=1

    if venceu:
        print(f'Parabéns! Você ganhou! Eu realmente pensei no número {numero}.')
    else:
        print(f'Você perdeu! Eu pensei no número {numero}.')
        pontuacao = 0
    print(f'Sua pontuação: {pontuacao}')

if __name__ == '__main__':
    jogar()