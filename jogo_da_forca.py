import random

def apresentar():
    print('-'*30)
    print('JOGO DA FORCA'.center(30))
    print('-'*30)
    print()

def definir_palavra():
    with open('palavras.txt','r',encoding='utf-8') as arquivo:
        palavras = [line.strip() for line in arquivo]
    palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()
    return palavra_secreta

   
def jogar(): 

    apresentar()
    palavra_secreta = definir_palavra()
    linhas = ['_' for x in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    tentativas = []

    while not enforcou and not acertou:
        mostrarLinhas = ' '.join(linhas)
        print(mostrarLinhas.center(30),'\n')

        tentativa = input(str("QUAL LETRA? ")).upper().strip()

        if tentativa.isalpha():
            if tentativa not in tentativas:
                tentativas.append(tentativa)
            else:
                print(f'A letra {tentativa} já foi!')
                continue
        else:
            print("Digite uma letra.")
            continue

        if tentativa not in palavra_secreta:
            erros += 1
            print(f"Você errou! A letra {tentativa} não existe na palavra.")
            print(f'Tentativas restantes: {6-erros}')
        else:
            for i,x in enumerate(palavra_secreta):
                if tentativa == x:
                    linhas[i] = x

        enforcou = erros == 6
        acertou = '_' not in linhas

        if acertou:
            print(palavra_secreta.center(30))
            print('PARABÉNS! VOCÊ GANHOU!'.center(30))
        elif enforcou:
            print(palavra_secreta.center(30))
            print('POXA, VOCÊ PERDEU!'.center(30))


if __name__ == '__main__':
    jogar()