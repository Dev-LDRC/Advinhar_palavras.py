from palavras_jogo import palavras_do_jogo
import random

##################################

palavra = random.choice(palavras_do_jogo)
chances = 4
jogar_denovo = 1
palavras_ja_usadas = []
palavra_certa = []

for x in range(0, jogar_denovo):
    dashboard = ''

    while True:
        # FEEDBACK DO JOGO DO USUARIO
        dashboard = ''

        for letra in palavra:
            if letra in palavra_certa:
                dashboard += letra
            else:
                dashboard += '-'

        # AVISOS E INPUT DO USUARIO
        print(f'Você tem {chances} chances')
        print(dashboard)
        advinhar = input('Advinhe uma letra da palavra: ').lower()

        # CASO O USUARIO TENTE ADVINHAR A "PALAVRA TODA"
        if len(advinhar) > 1:
            if advinhar == palavra:
                dashboard = palavra
            else:
                chances -= 1
                print('Infelizmente você errou o chute, tente novamente.')

        if advinhar not in palavras_ja_usadas:
            # SE O USUARIO ACERTAR OU ERRAR A "LETRA"
            if len(advinhar) == 1:
                if advinhar in palavra:
                    print('Muito Bem!, está letra tem na Palavra secreta.')
                    palavras_ja_usadas.append(advinhar)
                    palavra_certa.append(advinhar)
                else:
                    print('Infelizmente você errou, tente novamente.')
                    palavras_ja_usadas.append(advinhar)
                    chances -= 1
        else:
            print(f'A letra "{advinhar}" ja foi usada, digite outro.')
            print()
            continue

        # CONDIÇÃO DE VITORIA E DERROTA
        # VITORIA
        if dashboard == palavra:
            print()
            print(f'A palavra é "{palavra}".\nVocê Ganhou, parabéns!!!')
            print()
            while True:
                jogar_novamente = input('Você deseja jogar de novo? (S/N) -> ').lower()
                if jogar_novamente == 's':
                    chances = 4
                    palavra_certa.clear()
                    palavras_ja_usadas.clear()
                    palavra = random.choice(palavras_do_jogo)
                    jogar_denovo += 1
                    break
                else:
                    exit()
            continue

        # DERROTA
        if chances == 0:
            print()
            print(f'Infelizmente você Perdeu, A palavra era "{palavra}".')
            print()
            while True:
                jogar_novamente = input('Você deseja jogar de novo? (S/N) -> ').lower()
                if jogar_novamente == 's':
                    chances = 4
                    palavra_certa.clear()
                    palavras_ja_usadas.clear()
                    palavra = random.choice(palavras_do_jogo)
                    jogar_denovo += 1
                    break
                else:
                    exit()
            continue

        print()