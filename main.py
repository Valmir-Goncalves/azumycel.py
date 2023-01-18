from time import sleep

sleep(0.1)
print('                                              ')
print('+\033[m\033[34m=======\033[m========(\033[36m Machine\033[m )========\033[34m======\033[m+')
print('\033[36m=\033[m' * 42)
print("|                                        |")
sleep(0.1)
print('|               Developed                |')
print('|                                        |')
print('\033[36m=\033[m' * 42)
sleep(0.1)
print('+===============(\033[35m AZUMY\033[m )================+')
print("|                                        |")
print('|oi meu nome e \033[35mAzumy\033[m                     |')
sleep(0.1)
# while True:
sleep(0.1)
print('|Seja bem \033[34mVindo\033[m:                         |')
print("+========================================+")
sleep(0.1)
while True:
    res = str(input('Qual trabalho ira \033[34mrealizar\033[m: ')).strip().lower()
    print("|                                        |")
    if res == 'cintas de amarração' or res == 'cinta' or res == 'cintas' or res == 'magro':
        sleep(0.1)
        print("+========================================+")
        sleep(0.1)
        print(f'|\033[34mconcreto\033[m para (\033[34m{res}\033[m) adicionado        |')
        print('|com\033[32m sucesso\033[m!                            |')
        sleep(0.1)
        print(
            f'|           Para \033[32m(\033[m\033[36m{res}\033[m\033[32m)\033[m                 |')
        print('|usaremos (c\033[35m15\033[m Fck  \033[35m15\033[m \033[32m MPA\033[m)             |')
        print('|de resistência                          |')
        print("+========================================+")
        print('                     ')
        alt = float(input('altura\033[36m:\033[m '))
        lar = float(input('largura\033[36m:\033[m '))
        comp = float(input('comprimento\033[36m:\033[m '))
        quantidade = float(input('\033[34mquantas vezes será essa concretagem\033[m: '))
        skg = float(input('Saca de quantos kilos você usará Kg\033[36m:\033[m '))
        print('=' * 42)
        print("   ")
        print(
            '+\033[34m==============\033[m( \033[37mCIMENTO\033[m )\033[34m===============\033[m+')
        print('=' * 42)
        tipo = '\033[32mCP2-E-32\033[m'
        print(f'|Então usaremos o cimento (\033[32m{tipo}\033[m)     |')
        print(f'|de (\033[32m{skg}\033[m) kg                            |')
        m3 = comp * lar * alt * quantidade
        print('|   O volume total e  de (\033[34m{:.2f}\033[m) M³       |'.format(m3))
        print('|                                        |')
        cimento = 0.239
        cimentos = 239
        areia = 0.634
        areias = 634
        brita = 0.550
        britas = 550
        agua = 0.203
        aguas = 203
        aditivo = 0.003
        c1 = (cimento / skg) * skg * m3
        c2 = (cimentos / skg) * m3
        c3 = (cimentos / skg)
        a1 = (areia / 18) * 18 * m3
        a2 = (areias / 18) * m3
        b1 = (brita / 18) * 18 * m3
        b2 = (britas / 18) * m3
        ag1 = (agua / 18) * 18 * m3
        ag2 = (aguas / 18) * m3
        ad1 = (aditivo / 10) * m3
        print('=' * 42)
        sleep(0.1)
        print(
            '+\033[34m=========\033[m(\033[36m TOTAL DE MATERIAL\033[m )\033[34m==========\033[m+')
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) kg de cimento          |'.format(c1))
        print(
            "|         (\033[34m{:.2f}\033[m) sacas de (\033[32m{}\033[m) kg      |".format(c2, skg))

        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³  de areia           |'.format(a1))
        print('|         (\033[34m{:.2f}\033[m) latas de(\033[32m18\033[m) litros     |'.format(a2))
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³ de brita            |'.format(b1))
        print('|         (\033[34m{:.2f}\033[m) latas de (\033[32m18\033[m) litros    |'.format(b2))
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³ de água             |'.format(ag1))
        print('|         (\033[34m{:.3f}\033[m) latas de (\033[32m18\033[m) litros   |'.format(ag2))
        print('=' * 42)
        print('|(\033[34m{:.4f}\033[m) litros de aditivo plástificante|'.format(ad1))
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+=========\033[m( \033[37m TRAÇO DE CONCRETO\033[m )\033[34m=========+\033[m')
        print('=' * 42)
        print('|                                        |')
        print('|Será feito (\033[34m{:.2f}\033[m) traços                |'.format(c2))
        print('|Para cada traço                         |')
        print('|\033[34m 1 \033[msaca de cimento de (\033[32m{}\033[m)            |'.format(skg))
        s1areia = (areias / 18) / c3
        s2brita = (britas / 18) / c3
        s3agua = (aguas / 18) / c3
        s4aditivo = (aditivo * 10 * 10 / 10) / c3
        print('\033[36m=\033[m' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de areia de (\033[32m18\033[m) litros    |'.format(
            s1areia))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de brita de (\033[32m18\033[m) litros    |'.format(
            s2brita))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de água de (\033[32m18\033[m) litros     |'.format(
            s3agua))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.4f}\033[m) ml de aditivo plástificante    |'.format(s4aditivo))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|para cimento de (\033[32m42.5\033[m) kg usar:         |')
        print('|padiola  de (\033[35m36.33\033[m) litros              |')
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+===============\033[m(\033[32m MEDIDAS\033[m )\033[34m==============+\033[m')
        print('=' * 42)
        print('|                                        |')
        print(
            '|\033[34mAREIA\033[m ( 20 \033[35mx\033[m 37 \033[35mx\033[m 49 )                  |')
        print('|                                        |')

        print(
            '|\033[34mSEIXO\033[m ( 21\033[35m x\033[m 37\033[35m x\033[m 49 )                  |')
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|Na compra de material                   |')
        print('|você deve acrecentar                    |')
        print('|desperdicio na ordem de (\033[32m10%\033[m)           |')
        print('|slump de(\033[32mabatimento\033[m) (\033[32m08\033[m)cm             |')
        print('|                                        |')
        print('\033[34m=\033[m' * 42)
        print('|                                        |')
        print(
            '|seu calculo foi realizado com \033[35m(\033[m\033[36msucesso\033[m\033[35m)\033[m |')
        print('|                                        |')
        print('=' * 42)
        print('+========================================+')
        print('\033[36m=\033[m' * 42)
        print('                  ')


        # 20 MPA
    elif res == 'fundação' or res == 'fundações' or res == 'sapata' or res == 'sapatas':
        sleep(0.1)
        print("+========================================+")
        sleep(0.1)
        print(f'|\033[34mconcreto\033[m para (\033[34m{res}\033[m) adicionado       |')
        print('|com\033[32m sucesso\033[m!                            |')
        sleep(0.1)
        print(
            f'|           Para \033[32m(\033[m\033[36m{res}\033[m\033[32m)\033[m                |')
        print('|usaremos (c\033[35m15\033[m Fck  \033[35m15\033[m \033[32m MPA\033[m)             |')
        print('|de resistência                          |')
        print("+========================================+")
        print('                     ')
        alt = float(input('altura\033[36m:\033[m '))
        lar = float(input('largura\033[36m:\033[m '))
        comp = float(input('comprimento\033[36m:\033[m '))
        quantidade = float(input('\033[34mquantas vezes será essa concretagem\033[m: '))
        skg = float(input('Saca de quantos kilos você usará Kg\033[36m:\033[m '))
        print('=' * 42)
        print("   ")
        print(
            '+\033[34m==============\033[m( \033[37mCIMENTO\033[m )\033[34m===============\033[m+')
        print('=' * 42)
        tipo = '\033[32mCP2-E-32\033[m'
        print(f'|Então usaremos o cimento (\033[32m{tipo}\033[m)     |')
        print(f'|de (\033[32m{skg}\033[m) kg                            |')
        m3 = comp * lar * alt * quantidade
        print('|   O volume total e  de (\033[34m{:.2f}\033[m) M³       |'.format(m3))
        print('|                                        |')
        cimento = 0.269
        cimentos = 269
        areia = 0.629
        areias = 629
        brita = 0.560
        britas = 560
        agua = 0.196
        aguas = 196
        aditivo = 0.0034
        c1 = (cimento / skg * skg) * m3
        c2 = (cimentos / skg) * m3
        c3 = (cimentos / skg)
        a1 = (areia / 18) * 18 * m3
        a2 = (areias / 18) * m3
        b1 = (brita / 18) * 18 * m3
        b2 = (britas / 18) * m3
        ag1 = (agua / 18) * 18 * m3
        ag2 = (aguas / 18) * m3
        ad1 = (aditivo / 10) * m3
        print('\033[32m=\033[m' * 41)
        sleep(0.1)
        print(
            '+\033[34m=========\033[m(\033[36m TOTAL DE MATERIAL\033[m )\033[34m==========\033[m+')
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) kg de cimento          |'.format(c1))
        print(
            "|         (\033[34m{:.2f}\033[m) sacas de (\033[32m{}\033[m) kg     |".format(c2, skg))

        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³  de areia           |'.format(a1))
        print('|         (\033[34m{:.2f}\033[m) latas de(\033[32m18\033[m) litros   |'.format(a2))
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³ de brita            |'.format(b1))
        print('|         (\033[34m{:.2f}\033[m) latas de (\033[32m18\033[m) litros  |'.format(b2))
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³ de água             |'.format(ag1))
        print('|         (\033[34m{:.3f}\033[m) latas de (\033[32m18\033[m) litros  |'.format(ag2))
        print('=' * 42)
        print('|(\033[34m{:.4f}\033[m) litros de aditivo plástificante|'.format(ad1))
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+=========\033[m( \033[37m TRAÇO DE CONCRETO\033[m )\033[34m=========+\033[m')
        print('=' * 42)
        print('|                                        |')
        print('|Será feito (\033[34m{:.2f}\033[m) traços               |'.format(c2))
        print('|Para cada traço                         |')
        print('|\033[34m 1 \033[msaca de cimento de (\033[32m{}\033[m)            |'.format(skg))
        s1areia = (areias / 18) / c3
        s2brita = (britas / 18) / c3
        s3agua = (aguas / 18) / c3
        s4aditivo = (aditivo * 10 * 10 / 10) / c3
        print('\033[36m=\033[m' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de areia de (\033[32m18\033[m) litros    |'.format(
            s1areia))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de brita de (\033[32m18\033[m) litros    |'.format(
            s2brita))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de água de (\033[32m18\033[m) litros     |'.format(
            s3agua))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.4f}\033[m) ml de aditivo plástificante    |'.format(s4aditivo))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|para cimento de (\033[32m42.5\033[m) kg usar:         |')
        print('|padiola  de (\033[35m36.33\033[m) litros              |')
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+===============\033[m(\033[32m MEDIDAS\033[m )\033[34m==============+\033[m')
        print('=' * 42)
        print('|                                        |')
        print(
            '|\033[34mAREIA\033[m ( 20 \033[35mx\033[m 37 \033[35mx\033[m 49 )                  |')
        print('|                                        |')

        print(
            '|\033[34mSEIXO\033[m ( 21\033[35m x\033[m 37\033[35m x\033[m 49 )                  |')
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|Na compra de material                   |')
        print('|você deve acrecentar                    |')
        print('|desperdicio na ordem de (\033[32m10%\033[m)           |')
        print('|slump de(\033[32mabatimento\033[m) (\033[32m08\033[m)cm             |')
        print('|                                        |')
        print('\033[34m=\033[m' * 42)
        print('|                                        |')
        print(
            '|seu calculo foi realizado com \033[35m(\033[m\033[36msucesso\033[m\033[35m)\033[m |')
        print('|                                        |')
        print('=' * 42)
        print('+========================================+')
        print('\033[36m=\033[m' * 42)
        print('                  ')
        # 25 MPA
    elif res == 'pilar' or res == 'pilares' or res == 'viga' or res == 'vigas' or res == 'laje' or res == 'piso':
        sleep(0.1)
        print("+========================================+")
        sleep(0.1)
        print(f'|\033[34mconcreto\033[m para (\033[34m{res}\033[m) adicionado         |')
        print('|com\033[32m sucesso\033[m!                            |')
        sleep(0.1)
        print(
            f'|           Para \033[32m(\033[m\033[36m{res}\033[m\033[32m)\033[m                  |')
        print('|usaremos (c\033[35m15\033[m Fck  \033[35m15\033[m \033[32m MPA\033[m)             |')
        print('|de resistência                          |')
        print("+========================================+")
        print('                     ')
        alt = float(input('altura\033[36m:\033[m '))
        lar = float(input('largura\033[36m:\033[m '))
        comp = float(input('comprimento\033[36m:\033[m '))
        quantidade = float(input('\033[34mquantas vezes será essa concretagem\033[m: '))
        skg = float(input('Saca de quantos kilos você usará Kg\033[36m:\033[m '))
        print('=' * 42)
        print("   ")
        print(
            '+\033[34m==============\033[m( \033[37mCIMENTO\033[m )\033[34m===============\033[m+')
        print('=' * 42)
        tipo = '\033[32mCP2-E-32\033[m'
        print(f'|Então usaremos o cimento (\033[32m{tipo}\033[m)     |')
        print(f'|de (\033[32m{skg}\033[m) kg                            |')
        m3 = comp * lar * alt * quantidade
        print('|   O volume total e  de (\033[34m{:.2f}\033[m) M³       |'.format(m3))
        print('|                                        |')
        cimento = 0.344
        cimentos = 344
        areia = 0.486
        areias = 486
        brita = 0.364
        britas = 364
        agua = 0.210
        aguas = 210
        aditivo = 0.0037
        c1 = (cimento / skg) * skg * m3
        c2 = (cimentos / skg) * m3
        c3 = (cimentos / skg)

        a1 = (areia / 18) * 18 * m3
        a2 = (areias / 18) * m3
        b1 = (brita / 18) * 18 * m3
        b2 = (britas / 18) * m3
        ag1 = (agua / 18) * 18 * m3
        ag2 = (aguas / 18) * m3
        ad1 = (aditivo / 10) * m3
        print('=' * 42)
        sleep(0.1)
        print(
            '+\033[34m=========\033[m(\033[36m TOTAL DE MATERIAL\033[m )\033[34m==========\033[m+')
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) kg de cimento          |'.format(c1))
        print(
            "|         (\033[34m{:.2f}\033[m) sacas de (\033[32m{}\033[m) kg      |".format(c2, skg))

        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³  de areia           |'.format(a1))
        print('|         (\033[34m{:.2f}\033[m) latas de(\033[32m18\033[m) litros     |'.format(a2))
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³ de brita            |'.format(b1))
        print('|         (\033[34m{:.2f}\033[m) latas de (\033[32m18\033[m) litros    |'.format(b2))
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³ de água             |'.format(ag1))
        print('|         (\033[34m{:.3f}\033[m) latas de (\033[32m18\033[m) litros   |'.format(ag2))
        print('=' * 42)
        print('|(\033[34m{:.4f}\033[m) litros de aditivo plástificante|'.format(ad1))
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+=========\033[m( \033[37m TRAÇO DE CONCRETO\033[m )\033[34m=========+\033[m')
        print('=' * 42)
        print('|                                        |')
        print('|Será feito (\033[34m{:.2f}\033[m) traços                |'.format(c2))
        print('|Para cada traço                         |')
        print('|\033[34m 1 \033[msaca de cimento de (\033[32m{}\033[m)            |'.format(skg))
        s1areia = (areias / 18) / c3
        s2brita = (britas / 18) / c3
        s3agua = (aguas / 18) / c3
        s4aditivo = (aditivo * 10 * 10 / 10) / c3
        print('\033[36m=\033[m' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de areia de (\033[32m18\033[m) litros    |'.format(
            s1areia))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de brita de (\033[32m18\033[m) litros    |'.format(
            s2brita))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de água de (\033[32m18\033[m) litros     |'.format(
            s3agua))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.4f}\033[m) ml de aditivo plástificante    |'.format(s4aditivo))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|para cimento de (\033[32m42.5\033[m) kg usar:         |')
        print('|padiola  de (\033[35m36.33\033[m) litros              |')
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+===============\033[m(\033[34m MEDIDAS\033[m )\033[34m==============+\033[m')
        print('=' * 42)
        print('|                                        |')
        print(
            '|\033[34mAREIA\033[m ( 20 \033[35mx\033[m 37 \033[35mx\033[m 49 )                  |')
        print('|                                        |')

        print(
            '|\033[34mSEIXO\033[m ( 21\033[35m x\033[m 37\033[35m x\033[m 49 )                  |')
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|Na compra de material                   |')
        print('|você deve acrecentar                    |')
        print('|desperdicio na ordem de (\033[32m10%\033[m)           |')
        print('|slump de(\033[32mabatimento\033[m) (\033[32m08\033[m)cm             |')
        print('|                                        |')
        print('\033[34m=\033[m' * 42)
        print('|                                        |')
        print(
            '|seu calculo foi realizado com \033[35m(\033[m\033[36msucesso\033[m\033[35m)\033[m |')
        print('|                                        |')
        print('=' * 42)
        print('+========================================+')
        print('\033[36m=\033[m' * 42)
        print('                  ')
    elif res == 'obra 3':
        sleep(0.1)
        print("+========================================+")
        sleep(0.1)
        print(f'|\033[34mconcreto\033[m para (\033[34m{res}\033[m) adicionado       |')
        print('|com\033[32m sucesso\033[m!                             |')
        sleep(0.1)
        print(
            f'|           Para \033[32m(\033[m\033[36m{res}\033[m\033[32m)\033[m                |')
        print('|usaremos (c\033[35m15\033[m Fck  \033[35m15\033[m \033[32m MPA\033[m)             |')
        print('|de resistência                          |')
        print("+========================================+")
        print('                     ')
        alt = float(input('altura\033[36m:\033[m '))
        lar = float(input('largura\033[36m:\033[m '))
        comp = float(input('comprimento\033[36m:\033[m '))
        quantidade = float(input('\033[34mquantas vezes será essa concretagem\033[m: '))
        skg = float(input('Saca de quantos kilos você usará Kg\033[36m:\033[m '))
        print('=' * 42)
        print("   ")
        print(
            '+\033[34m==============\033[m( \033[37mCIMENTO\033[m )\033[34m===============\033[m+')
        print('=' * 42)
        tipo = '\033[32mCP2-E-32\033[m'
        print(f'|Então usaremos o cimento (\033[32m{tipo}\033[m)     |')
        print(f'|de (\033[32m{skg}\033[m) kg                            |')
        m3 = comp * lar * alt * quantidade
        print('|   O volume total e  de (\033[34m{:.2f}\033[m) M³       |'.format(m3))
        print('|                                        |')

        cimento = 0.317
        cimentos = 317
        areia = 0.623
        areias = 623
        brita = 0.579
        britas = 579
        agua = 0.184
        aguas = 184
        aditivo = 0.004
        c1 = (cimento / skg) * skg * m3  # kg
        c2 = (cimentos / skg) * m3  # sacas
        c3 = (cimentos / skg)
        a1 = (areia / 18) * 18 * m3  # metro cubico ok
        a2 = (areias / 18) * m3  # latas ok
        b1 = (brita / 18) * 18 * m3  # metro cubico
        b2 = (britas / 18) * m3  # latas
        ag1 = (agua / 18) * 18 * m3  # metro cubico
        ag2 = (aguas / 18) * m3  # latas
        ad1 = (aditivo / 10) * m3
        print('\033[32m=\033[m' * 55)
        sleep(0.1)
        print(
            '+\033[34m=========\033[m(\033[36m TOTAL DE MATERIAL\033[m )\033[34m==========\033[m+')
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) kg de cimento          |'.format(c1))
        print(
            "|         (\033[34m{:.2f}\033[m) sacas de (\033[32m{}\033[m) kg      |".format(c2, skg))

        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³  de areia           |'.format(a1))
        print('|         (\033[34m{:.2f}\033[m) latas de(\033[32m18\033[m) litros    |'.format(a2))
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³ de brita            |'.format(b1))
        print('|         (\033[34m{:.2f}\033[m) latas de (\033[32m18\033[m) litros   |'.format(b2))
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³ de água             |'.format(ag1))
        print('|         (\033[34m{:.3f}\033[m) latas de (\033[32m18\033[m) litros  |'.format(ag2))
        print('=' * 42)
        print('|(\033[34m{:.4f}\033[m) litros de aditivo plástificante|'.format(ad1))
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+=========\033[m( \033[37m TRAÇO DE CONCRETO\033[m )\033[34m=========+\033[m')
        print('=' * 42)
        print('|                                        |')
        print('|Será feito (\033[34m{:.2f}\033[m) traços                |'.format(c2))
        print('|Para cada traço                         |')
        print('|\033[34m 1 \033[msaca de cimento de (\033[32m{}\033[m)            |'.format(skg))
        s1areia = (areias / 18) / c3
        s2brita = (britas / 18) / c3
        s3agua = (aguas / 18) / c3
        s4aditivo = (aditivo * 10 * 10 / 10) / c3
        print('\033[36m=\033[m' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de areia de (\033[32m18\033[m) litros    |'.format(
            s1areia))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de brita de (\033[32m18\033[m) litros    |'.format(
            s2brita))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de água de (\033[32m18\033[m) litros     |'.format(
            s3agua))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.4f}\033[m) ml de aditivo plástificante    |'.format(s4aditivo))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|para cimento de (\033[32m42.5\033[m) kg usar:         |')
        print('|padiola  de (\033[35m36.33\033[m) litros              |')
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+===============\033[m(\033[32m MEDIDAS\033[m )\033[34m==============+\033[m')
        print('=' * 42)
        print('|                                        |')
        print(
            '|\033[34mAREIA\033[m ( 20 \033[35mx\033[m 37 \033[35mx\033[m 49 )                  |')
        print('|                                        |')

        print(
            '|\033[34mSEIXO\033[m ( 21\033[35m x\033[m 37\033[35m x\033[m 49 )                  |')
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|Na compra de material                   |')
        print('|você deve acrecentar                    |')
        print('|desperdicio na ordem de (\033[32m10%\033[m)           |')
        print('|slump de(\033[32mabatimento\033[m) (\033[32m08\033[m)cm             |')
        print('|                                        |')
        print('\033[34m=\033[m' * 42)
        print('|                                        |')
        print(
            '|seu calculo foi realizado com \033[35m(\033[m\033[36msucesso\033[m\033[35m)\033[m |')
        print('|                                        |')
        print('=' * 42)
        print('+========================================+')
        print('\033[36m=\033[m' * 42)
        print('                  ')

    if res == 'obra 3.5':
        sleep(0.1)
        print("+========================================+")
        sleep(0.1)
        print(f'|\033[34mconcreto\033[m para (\033[34m{res}\033[m) adicionado     |')
        print('|com\033[32m sucesso\033[m!                            |')
        sleep(0.1)
        print(
            f'|           Para \033[32m(\033[m\033[36m{res}\033[m\033[32m)\033[m              |')
        print('|usaremos (c\033[35m15\033[m Fck  \033[35m15\033[m \033[32m MPA\033[m)             |')
        print('|de resistência                          |')
        print("+========================================+")
        print('                     ')
        alt = float(input('altura\033[36m:\033[m '))
        lar = float(input('largura\033[36m:\033[m '))
        comp = float(input('comprimento\033[36m:\033[m '))
        quantidade = float(input('\033[34mquantas vezes será essa concretagem\033[m: '))
        skg = float(input('Saca de quantos kilos você usará Kg\033[36m:\033[m '))
        print('=' * 42)
        print("   ")
        print(
            '+\033[34m==============\033[m( \033[37mCIMENTO\033[m )\033[34m===============\033[m+')
        print('=' * 42)
        tipo = '\033[32mCP2-E-32\033[m'
        print(f'|Então usaremos o cimento (\033[32m{tipo}\033[m)     |')
        print(f'|de (\033[32m{skg}\033[m) kg                            |')
        m3 = comp * lar * alt * quantidade
        print('|   O volume total e  de (\033[34m{:.2f}\033[m) M³       |'.format(m3))
        print('|                                        |')
        cimento = 0.344
        cimentos = 344
        areia = 0.614
        areias = 614
        brita = 0.586
        britas = 586
        agua = 0.186
        aguas = 186
        aditivo = 0.0044
        c1 = (cimento / skg) * skg * m3  # kg
        c2 = (cimentos / skg) * m3  # sacas
        c3 = (cimentos / skg)
        a1 = (areia / 18) * 18 * m3  # metro cubico ok
        a2 = (areias / 18) * m3  # latas ok
        b1 = (brita / 18) * 18 * m3  # metro cubico
        b2 = (britas / 18) * m3  # latas
        ag1 = (agua / 18) * 18 * m3  # metro cubico
        ag2 = (aguas / 18) * m3  # latas
        ad1 = (aditivo / 10) * m3
        print('\033[32m=\033[m' * 42)
        sleep(0.1)
        print(
            '+\033[34m=========\033[m(\033[36m TOTAL DE MATERIAL\033[m )\033[34m==========\033[m+')
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) kg de cimento          |'.format(c1))
        print(
            "|         (\033[34m{:.2f}\033[m) sacas de (\033[32m{}\033[m) kg      |".format(c2, skg))

        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³  de areia           |'.format(a1))
        print('|         (\033[34m{:.2f}\033[m) latas de(\033[32m18\033[m) litros    |'.format(a2))
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³ de brita            |'.format(b1))
        print('|         (\033[34m{:.2f}\033[m) latas de (\033[32m18\033[m) litros   |'.format(b2))
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³ de água             |'.format(ag1))
        print('|         (\033[34m{:.3f}\033[m) latas de (\033[32m18\033[m) litros  |'.format(ag2))
        print('=' * 42)
        print('|(\033[34m{:.4f}\033[m) litros de aditivo plástificante|'.format(ad1))
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+=========\033[m( \033[37m TRAÇO DE CONCRETO\033[m )\033[34m=========+\033[m')
        print('=' * 42)
        print('|                                        |')
        print('|Será feito (\033[34m{:.2f}\033[m) traços                |'.format(c2))
        print('|Para cada traço                         |')
        print('|\033[34m 1 \033[msaca de cimento de (\033[32m{}\033[m)            |'.format(skg))
        s1areia = (areias / 18) / c3
        s2brita = (britas / 18) / c3
        s3agua = (aguas / 18) / c3
        s4aditivo = (aditivo * 10 * 10 / 10) / c3
        print('\033[36m=\033[m' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de areia de (\033[32m18\033[m) litros    |'.format(
            s1areia))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de brita de (\033[32m18\033[m) litros    |'.format(
            s2brita))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de água de (\033[32m18\033[m) litros     |'.format(
            s3agua))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.4f}\033[m) ml de aditivo plástificante    |'.format(s4aditivo))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|para cimento de (\033[32m42.5\033[m) kg usar:         |')
        print('|padiola  de (\033[35m36.33\033[m) litros              |')
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+===============\033[m(\033[32m MEDIDAS\033[m )\033[34m==============+\033[m')
        print('=' * 42)
        print('|                                        |')
        print(
            '|\033[34mAREIA\033[m ( 20 \033[35mx\033[m 37 \033[35mx\033[m 49 )                  |')
        print('|                                        |')

        print(
            '|\033[34mSEIXO\033[m ( 21\033[35m x\033[m 37\033[35m x\033[m 49 )                  |')
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|Na compra de material                   |')
        print('|você deve acrecentar                    |')
        print('|desperdicio na ordem de (\033[32m10%\033[m)           |')
        print('|slump de(\033[32mabatimento\033[m) (\033[32m08\033[m)cm             |')
        print('|                                        |')
        print('\033[34m=\033[m' * 42)
        print('|                                        |')
        print(
            '|seu calculo foi realizado com \033[35m(\033[m\033[36msucesso\033[m\033[35m)\033[m |')
        print('|                                        |')
        print('=' * 42)
        print('+========================================+')
        print('\033[36m=\033[m' * 42)
        print('                  ')

        # 40 MPA
    elif res == 'obra 4':

        sleep(0.1)
        print("+========================================+")
        sleep(0.1)
        print(f'|\033[34mconcreto\033[m para (\033[34m{res}\033[m) adicionado       |')
        print('|com\033[32m sucesso\033[m!                            |')
        sleep(0.1)
        print(
            f'|           Para (\033[36m{res}\033[m)                |')
        print('|usaremos (c\033[35m15\033[m Fck  \033[35m15\033[m \033[32m MPA\033[m)             |')
        print('|de resistência                          |')
        print("+========================================+")
        print('                     ')
        alt = float(input('altura\033[36m:\033[m '))
        lar = float(input('largura\033[36m:\033[m '))
        comp = float(input('comprimento\033[36m:\033[m '))
        quantidade = float(input('\033[34mquantas vezes será essa concretagem\033[m: '))
        skg = float(input('Saca de quantos kilos você usará Kg\033[36m:\033[m '))
        print('=' * 42)
        print("   ")
        print(
            '+\033[34m==============\033[m( \033[37mCIMENTO\033[m )\033[34m===============\033[m+')
        print('=' * 42)
        tipo = '\033[32mCP2-E-32\033[m'
        print(f'|Então usaremos o cimento (\033[32m{tipo}\033[m)     |')
        print(f'|de (\033[32m{skg}\033[m) kg                            |')
        m3 = comp * lar * alt * quantidade
        print('|   O volume total e  de (\033[34m{:.2f}\033[m) M³       |'.format(m3))
        print('|                                        |')
        cimento = 0.365
        cimentos = 365
        areia = 0.609
        areias = 609
        brita = 0.592
        britas = 592
        agua = 0.186
        aguas = 186
        aditivo = 0.0046
        c1 = (cimento / skg) * skg * m3  # kg
        c2 = (cimentos / skg) * m3  # sacas
        c3 = (cimentos / skg)
        a1 = (areia / 18) * 18 * m3  # metro cubico ok
        a2 = (areias / 18) * m3  # latas ok
        b1 = (brita / 18) * 18 * m3  # metro cubico
        b2 = (britas / 18) * m3  # latas
        ag1 = (agua / 18) * 18 * m3  # metro cubico
        ag2 = (aguas / 18) * m3  # latas
        ad1 = (aditivo / 10) * m3
        print('=' * 42)
        sleep(0.1)
        print(
            '+\033[34m=========\033[m(\033[36m TOTAL DE MATERIAL\033[m )\033[34m==========\033[m+')
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) kg de cimento          |'.format(c1))
        print(
            "|         (\033[34m{:.2f}\033[m) sacas de (\033[32m{}\033[m) kg     |".format(c2, skg))

        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³  de areia           |'.format(a1))
        print('|         (\033[34m{:.2f}\033[m) latas de(\033[32m18\033[m) litros   |'.format(a2))
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³ de brita            |'.format(b1))
        print('|         (\033[34m{:.2f}\033[m) latas de (\033[32m18\033[m) litros  |'.format(b2))
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³ de água             |'.format(ag1))
        print('|         (\033[34m{:.3f}\033[m) latas de (\033[32m18\033[m) litros  |'.format(ag2))
        print('=' * 42)
        print('|(\033[34m{:.4f}\033[m) litros de aditivo plástificante|'.format(ad1))
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+=========\033[m( \033[37m TRAÇO DE CONCRETO\033[m )\033[34m=========+\033[m')
        print('=' * 42)
        print('|                                        |')
        print('|Será feito (\033[34m{:.2f}\033[m) traços               |'.format(c2))
        print('|Para cada traço                         |')
        print('|\033[34m 1 \033[msaca de cimento de (\033[32m{}\033[m)            |'.format(skg))
        s1areia = (areias / 18) / c3
        s2brita = (britas / 18) / c3
        s3agua = (aguas / 18) / c3
        s4aditivo = (aditivo * 10 * 10 / 10) / c3
        print('\033[36m=\033[m' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de areia de (\033[32m18\033[m) litros    |'.format(
            s1areia))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de brita de (\033[32m18\033[m) litros    |'.format(
            s2brita))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de água de (\033[32m18\033[m) litros     |'.format(
            s3agua))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.4f}\033[m) ml de aditivo plástificante    |'.format(s4aditivo))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|para cimento de (\033[32m42.5\033[m) kg usar:         |')
        print('|padiola  de (\033[35m36.33\033[m) litros              |')
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+===============\033[m(\033[32m MEDIDAS\033[m )\033[34m==============+\033[m')
        print('=' * 42)
        print('|                                        |')
        print(
            '|\033[34mAREIA\033[m ( 20 \033[35mx\033[m 37 \033[35mx\033[m 49 )                  |')
        print('|                                        |')

        print(
            '|\033[34mSEIXO\033[m ( 21\033[35m x\033[m 37\033[35m x\033[m 49 )                  |')
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|Na compra de material                   |')
        print('|você deve acrecentar                    |')
        print('|desperdicio na ordem de (\033[32m10%\033[m)           |')
        print('|slump de(\033[32mabatimento\033[m) (\033[32m08\033[m)cm             |')
        print('|                                        |')
        print('\033[34m=\033[m' * 42)
        print('|                                        |')
        print(
            '|seu calculo foi realizado com \033[35m(\033[m\033[36msucesso\033[m\033[35m)\033[m |')
        print('|                                        |')
        print('=' * 42)
        print('+========================================+')
        print('\033[36m=\033[m' * 42)
        print('                  ')

        # 45 MPA
    elif res == 'obra 4.5':
        sleep(0.1)
        print("+========================================+")
        sleep(0.1)
        print(f'|\033[34mconcreto\033[m para (\033[34m{res}\033[m) adicionado     |')
        print('|com\033[32m sucesso\033[m!                            |')
        sleep(0.1)
        print(
            f'|           Para \033[32m(\033[m\033[36m{res}\033[m\033[32m)\033[m              |')
        print('|usaremos (c\033[35m15\033[m Fck  \033[35m15\033[m \033[32m MPA\033[m)             |')
        print('|de resistência                          |')
        print("+========================================+")
        print('                     ')
        alt = float(input('altura\033[36m:\033[m '))
        lar = float(input('largura\033[36m:\033[m '))
        comp = float(input('comprimento\033[36m:\033[m '))
        quantidade = float(input('\033[34mquantas vezes será essa concretagem\033[m: '))
        skg = float(input('Saca de quantos kilos você usará Kg\033[36m:\033[m '))
        print('=' * 42)
        print("   ")
        print(
            '+\033[34m==============\033[m( \033[37mCIMENTO\033[m )\033[34m===============\033[m+')
        print('=' * 42)
        tipo = '\033[32mCP2-E-32\033[m'
        print(f'|Então usaremos o cimento (\033[32m{tipo}\033[m)     |')
        print(f'|de (\033[32m{skg}\033[m) kg                            |')
        m3 = comp * lar * alt * quantidade
        print('|   O volume total e  de (\033[34m{:.2f}\033[m) M³       |'.format(m3))
        print('|                                        |')
        cimento = 0.387
        cimentos = 387
        areia = 0.600
        areias = 600
        brita = 0.597
        britas = 597
        agua = 0.186
        aguas = 186
        aditivo = 0.0049
        c1 = (cimento / skg) * skg * m3  # kg
        c2 = (cimentos / skg) * m3  # sacas
        c3 = (cimento / skg)
        a1 = (areia / 18) * 18 * m3  # metro cubico ok
        a2 = (areias / 18) * m3  # latas ok
        b1 = (brita / 18) * 18 * m3  # metro cubico
        b2 = (britas / 18) * m3  # latas
        ag1 = (agua / 18) * 18 * m3  # metro cubico
        ag2 = (aguas / 18) * m3  # latas
        ad1 = (aditivo / 10) * m3
        print('\033[32m=\033[m' * 55)
        sleep(0.1)
        print(
            '+\033[34m=========\033[m(\033[36m TOTAL DE MATERIAL\033[m )\033[34m==========\033[m+')
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) kg de cimento          |'.format(c1))
        print(
            "|         (\033[34m{:.2f}\033[m) sacas de (\033[32m{}\033[m) kg      |".format(c2, skg))

        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³  de areia           |'.format(a1))
        print('|         (\033[34m{:.2f}\033[m) latas de(\033[32m18\033[m) litros    |'.format(a2))
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³ de brita            |'.format(b1))
        print('|         (\033[34m{:.2f}\033[m) latas de (\033[32m18\033[m) litros   |'.format(b2))
        print('=' * 42)
        print('|         (\033[34m{:.3f}\033[m) M³ de água             |'.format(ag1))
        print('|         (\033[34m{:.3f}\033[m) latas de (\033[32m18\033[m) litros  |'.format(ag2))
        print('=' * 42)
        print('|(\033[34m{:.4f}\033[m) litros de aditivo plástificante|'.format(ad1))
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+=========\033[m( \033[37m TRAÇO DE CONCRETO\033[m )\033[34m=========+\033[m')
        print('=' * 42)
        print('|                                        |')
        print('|Será feito (\033[34m{:.2f}\033[m) traços                |'.format(c2))
        print('|Para cada traço                         |')
        print('|\033[34m 1 \033[msaca de cimento de (\033[32m{}\033[m)            |'.format(skg))
        s1areia = (areias / 18) / c3
        s2brita = (britas / 18) / c3
        s3agua = (aguas / 18) / c3
        s4aditivo = (aditivo * 10 * 10 / 10) / c3
        print('\033[36m=\033[m' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de areia de (\033[32m18\033[m) litros    |'.format(
            s1areia))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de brita de (\033[32m18\033[m) litros    |'.format(
            s2brita))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de água de (\033[32m18\033[m) litros     |'.format(
            s3agua))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.4f}\033[m) ml de aditivo plástificante    |'.format(s4aditivo))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|para cimento de (\033[32m42.5\033[m) kg usar:         |')
        print('|padiola  de (\033[35m36.33\033[m) litros              |')
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+===============\033[m(\033[32m MEDIDAS\033[m )\033[34m==============+\033[m')
        print('=' * 42)
        print('|                                        |')
        print(
            '|\033[34mAREIA\033[m ( 20 \033[35mx\033[m 37 \033[35mx\033[m 49 )                  |')
        print('|                                        |')

        print(
            '|\033[34mSEIXO\033[m ( 21\033[35m x\033[m 37\033[35m x\033[m 49 )                  |')
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|Na compra de material                   |')
        print('|você deve acrecentar                    |')
        print('|desperdicio na ordem de (\033[32m10%\033[m)           |')
        print('|slump de(\033[32mabatimento\033[m) (\033[32m08\033[m)cm             |')
        print('|                                        |')
        print('\033[34m=\033[m' * 42)
        print('|                                        |')
        print(
            '|seu calculo foi realizado com \033[35m(\033[m\033[36msucesso\033[m\033[35m)\033[m |')
        print('|                                        |')
        print('=' * 42)
        print('+========================================+')
        print('\033[36m=\033[m' * 42)
        print('                  ')
    if res == 'escada' or res == 'rampa':
        sleep(0.1)
        print("+========================================+")
        sleep(0.1)
        print(f'|\033[34mconcreto\033[m para (\033[36m{res}\033[m)                  |')
        print(f'|adicionado com\033[32m sucesso\033[m!                 |')
        sleep(0.1)
        print(
            f'|             Para \033[32m(\033[m\033[36m{res}\033[m\033[32m)\033[m              |')
        sleep(0.1)
        print(
            '|usaremos o (c\033[35m30\033[m Fck  \033[35m30\033[m \033[32m MPA\033[m)           |')
        print('|de resistência                          |')
        sleep(0.1)
        print("+========================================+")
        comp = float(input('qual o comprimento\033[36m:\033[m '))
        fd = float(input('qual a altura do fundo\033[36m:\033[m '))
        lar = float(input('qual a largura da escada\033[36m:\033[m '))
        qt = float(input('qual e o numero de degraus\033[36m:\033[m '))
        esp = float(input('qual e a altura do espelho\033[36m:\033[m '))
        deg = float(input('qual o comprimento do degrau\033[36m:\033[m '))
        quantidade = float(input('vezes que será feita essa concretagem\033[32m?\033[m '))
        skg = float(input('Saca de quantos kilos você usará kg: '))
        print('           ')
        sleep(0.1)
        print('=' * 42)
        print(
            '\033[34m+===============\033[m( \033[32mCIMENTO\033[m )\033[34m==============+\033[m')
        print('=' * 42)
        tipo = '\033[32mCP2-E-32\033[m'
        print('|                                        |')
        print('|Então usaremos o cimento                |')
        print(f'(\033[36m{tipo}\033[m) de (\033[32m{skg}\033[m) kg                  |')
        print('|                                        |')
        smf = comp * fd * lar * quantidade
        smd = (qt / 2) * deg * esp * lar * quantidade
        m3 = smf + smd
        print('|O volume total e  de (\033[34m{:.2f}\033[m) M³          |'.format(m3))
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        smf = comp * fd * lar * quantidade
        smd = (qt / 2) * deg * esp * lar * quantidade
        m3 = smf + smd
        cimento = 0.365
        cimentos = 365
        areia = 0.609
        areias = 609
        brita = 0.592
        britas = 592
        agua = 0.186
        aguas = 186
        aditivo = 0.0046
        c1 = (cimento / skg) * skg * m3  # kg
        c2 = (cimentos / skg) * m3  # sacas
        c3 = (cimentos / skg)
        a1 = (areia / 18) * 18 * m3  # metro cubico ok
        a2 = (areias / 18) * m3  # latas ok
        b1 = (brita / 18) * 18 * m3  # metro cubico
        b2 = (britas / 18) * m3  # latas
        ag1 = (agua / 18) * 18 * m3  # metro cubico
        ag2 = (aguas / 18) * m3  # latas
        ad1 = (aditivo / 10) * m3
        print(
            '\033[34m+=========\033[m(\033[32m TOTAL DE MATERIAL\033[m )\033[34m==========+\033[m')
        print('=' * 42)
        print('|       (\033[34m{:.3f}\033[m) kg de cimento            |'.format(c1))
        print(
            "|       (\033[34m{:.2f}\033[m) sacas de (\033[32m{}\033[m) kg        |".format(c2, skg))
        print('\033[36m=\033[m' * 42)
        print('|       (\033[34m{:.3f}\033[m) M³  de areia             |'.format(a1))
        print('|      (\033[34m{:.2f}\033[m) latas de(\033[32m18\033[m) litros       |'.format(a2))

        print('\033[36m=\033[m' * 42)
        print('|                (\033[34m{:.3f}\033[m) M³ de brita     |'.format(b1))
        print('|     (\033[34m{:.2f}\033[m) latas de (\033[32m18\033[m) litros       |'.format(b2))
        print('\033[35m=\033[m' * 42)
        print('|      (\033[34m{:.3f}\033[m) M³ de água                |'.format(ag1))
        print('|(\033[34m{:.3f}\033[m) latas de (\033[32m18\033[m) litros            |'.format(ag2))
        print('\033[35m=\033[m' * 42)
        print('|(\033[34m{:.4f}\033[m) litros de aditivo plástificante|'.format(ad1))
        print('|                                        |')
        print('\033[32m=\033[m' * 42)
        sleep(0.1)
        print(
            '\033[34m+=========\033[m( \033[32m TRAÇO DE CONCRETO\033[m )\033[34m==========+\033[m')
        print('\033[32m=\033[m' * 42)
        print('|                                        |')
        print('|Será feito (\033[34m{:.2f}\033[m) traços                |'.format(c2))
        print('|                                        |')
        print('|Para cada traço                                 |')
        print('1 saca de cimento de (\033[32m{}\033[m)              |'.format(skg))
        print('|                                        |')
        s1areia = (areias / 18) / c3
        s2brita = (britas / 18) / c3
        s3agua = (aguas / 18) / c3
        s4aditivo = (aditivo * 10 * 10 / 10) / c3
        print('\033[36m=\033[m' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de areia de (\033[32m18\033[m) litros    |'.format(
            s1areia))
        print('|                                        |')
        print('\033[35m=\033[m' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de brita de (\033[32m18\033[m) litros    |'.format(
            s2brita))
        print('|                                        |')
        print('\033[35m=\033[m' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de água de (\033[32m18\033[m) litros     |'.format(
            s3agua))
        print('|                                        |')
        print('\033[36m=\033[m' * 42)
        print('|                                        |')
        print('|(\033[34m{:.4f}\033[m) ml de aditivo plástificante    |'.format(s4aditivo))
        print('|                                        |')
        print('\033[35m=\033[m' * 42)
        print('|                                        |')
        print('|para cimento de (\033[32m42.5\033[m) kg usar:         |')
        print('|padiola  de (\033[35m36.33\033[m) litros              |')
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print('\033[34m+==============\033[m(\033[32m MEDIDAS\033[m )\033[34m===============+\033[m')
        print('=' * 42)
        print('|                                        |')
        print(
            '|\033[34mAREIA\033[m ( 20 \033[35mx\033[m 37 \033[35mx\033[m 49 )                  |')
        print('|                                        |')
        print(
            '|\033[34mSEIXO\033[m ( 21\033[35m x\033[m 37\033[35m x\033[m 49 )                  |')
        print('|                                        |')

        print('=' * 42)
        print('|                                        |')
        print('|Na compra de material                   |')
        print('|você deve acrecentar                    |')
        print('|desperdicio na ordem de (\033[32m10%\033[m)           |')
        print('|slump de(\033[32mabatimento\033[m) (\033[32m08\033[m)cm             |')
        print('|                                        |')
        print('\033[34m=\033[m' * 42)
        print('|                                        |')
        print(
            '|seu calculo foi realizado com \033[35m(\033[m\033[32msucesso\033[m\033[35m)\033[m |')
        print('|                                        |')
        print('\033[35m=\033[m' * 42)
        print('+========================================+')
        print('|\033[36mDeseja fazer outro calculo...\033[m           |')
        print('+========================================+')
        print('=' * 42)
        print('                  ')

    elif res == 'tubulão' or res == 'broca':
        sleep(0.1)
        print("+========================================+")
        sleep(0.1)
        print(f'|\033[34mConcreto\033[m para (\033[36m{res}\033[m)                   |')
        print('|adicionado com\033[32m sucesso\033[m!                 |')
        sleep(0.1)
        print(
            f'|Para \033[32m(\033[m\033[36m{res}\033[m\033[32m)\033[m                            |')
        print(
            '|Usaremos o (c\033[35m25\033[m Fck  \033[35m25\033[m \033[32m MPA\033[m)           |')
        print("+========================================+")

        print('ok então vamos lá')
        print('               ')
        sleep(0.1)
        r = float(input('Qual a medida do raio: '))
        al = float(input('Qual a medida da altura: '))
        quantidade = float(input('Quantas vezes será essa concretagem: '))
        skg = float(input('Saca de quantos kilos você usará kg: '))
        sleep(0.1)
        print('=' * 42)

        print(
            '\033[34m+===============\033[m( \033[37mCIMENTO\033[m )\033[34m==============+\033[m')
        print('=' * 42)
        tipo = '\033[37mCP2-E-32\033[m'
        print('|                                        |')
        print('|Então usaremos o cimento                |')
        print('(\033[32m{}\033[m) de (\033[32m{}\033[m) kg                  |'.format(tipo, skg))
        print('|                                        |')
        m3 = r * al * quantidade
        print('|O volume total e  de (\033[34m{:.3f}\033[m) M³         |'.format(m3))
        print('|                                        |')
        py = 3.1416
        raio = r * r
        area = py * raio
        x = py * raio * al
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+===========\033[m( \033[32mCIRCUNFERÊNCIA\033[m )\033[34m===========+\033[m')

        print('=' * 42)
        print('| A área total desta circunferência é    |')
        print('|\033[m(\033[36m {:.3f} \033[m)                               |'.format(area))
        sleep(0.1)
        cimento = 0.317
        cimentos = 317
        areia = 0.623
        areias = 623
        brita = 0.579
        britas = 579
        agua = 0.184
        aguas = 186
        aditivo = 0.004
        c1 = (cimento / skg) * skg * x  # kg
        c2 = (cimentos / skg) * x  # sacas
        c3 = (cimentos / skg)
        a1 = (areia / 18) * 18 * x  # metro cubico ok
        a2 = (areias / 18) * x  # latas ok
        b1 = (brita / 18) * 18 * x  # metro cubico
        b2 = (britas / 18) * x  # latas
        ag1 = (agua / 18) * 18 * x  # metro cubico
        ag2 = (aguas / 18) * x  # latas
        ad1 = (aditivo / 10) * x
        sleep(0.1)
        print('=' * 42)

        print('\033[34m+==========\033[m(\033[32m TOTAL DE MATERIAL\033[m )\033[34m=========+\033[m')
        print('=' * 42)
        print('|       (\033[34m{:.3f}\033[m) kg de cimento             |'.format(c1))
        print(
            "|       (\033[34m{:.2f}\033[m) sacas de (\033[32m{}\033[m) kg        |".format(c2, skg))
        print('\033[36m=\033[m' * 42)
        print('|       (\033[34m{:.3f}\033[m) M³  de areia              |'.format(a1))
        print('|       (\033[34m{:.2f}\033[m) latas de(\033[32m18\033[m) litros      |'.format(a2))
        print('\033[36m=\033[m' * 42)
        print('|       (\033[34m{:.3f}\033[m) M³ de brita               |'.format(b1))
        print('|       (\033[34m{:.2f}\033[m) latas de (\033[32m18\033[m) litros     |'.format(b2))
        print('=' * 42)
        print('|       (\033[34m{:.3f}\033[m) M³ de água                |'.format(ag1))
        print('|       (\033[34m{:.3f}\033[m) latas de (\033[32m18\033[m) litros       |'.format(ag2))
        print('=' * 42)
        print('|(\033[34m{:.4f}\033[m) litros de aditivo plástificante|'.format(ad1))
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+=========\033[m( \033[32m TRAÇO DE CONCRETO\033[m )\033[34m=========+\033[m')
        print('=' * 42)
        print('|                                        |')
        print('|Será feito (\033[34m{:.2f}\033[m) traços                |'.format(c2))
        print('|                                        |')
        print('|Para cada traço                         |')
        print('|\033[34m 1 \033[msaca de cimento de (\033[32m{}\033[m) |'.format(skg))
        print('|                                        |')
        s1areia = (areias / 18) / c3
        s2brita = (britas / 18) / c3
        s3agua = (aguas / 18) / c3
        s4aditivo = (aditivo * 10 * 10 / 10) / c3
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de areia de (\033[32m18\033[m) litros     |'.format(
            s1areia))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de brita de (\033[32m18\033[m) litros    |'.format(
            s2brita))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de água de (\033[32m18\033[m) litros      |'.format(s3agua))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.4f}\033[m) ml de aditivo plástificante      |'.format(s4aditivo))

        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|para cimento de (\033[32m42.5\033[m) kg usar:         |')
        print('|padiola  de (\033[35m36.33\033[m) litros              |')
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)

        print(
            '\033[34m+===============\033[m(\033[37m MEDIDAS\033[m )\033[34m==============+\033[m')
        print('=' * 42)
        print('|                                        |')
        print(
            '|\033[34mAREIA\033[m ( 20 \033[35mx\033[m 37 \033[35mx\033[m 49 )                  |')
        print('|                                        |')
        print(
            '|\033[34mSEIXO\033[m ( 21\033[35m x\033[m 37\033[35m x\033[m 49 )                  |')
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|Na compra de material                   |')
        print('|você deve acrecentar                    |')
        print('|desperdicio na ordem de (\033[32m10%\033[m)           |')
        print('|slump de(\033[32mabatimento\033[m) (\033[32m08\033[m)cm             |')
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print(
            '|Seu calculo foi realizado com \033[35m(\033[m\033[32msucesso\033[m\033[35m)\033[m |')
        print('|                                        |')
        print("+========================================+")
    if res == 'alvenaria':
        sleep(0.1)
        print("+========================================+")
        sleep(0.1)
        print("|\033[34mAlvenaria\033[m                               |")
        print(
            '|(\033[36m{}\033[m) adicionado com\033[32m sucesso\033[m!     |'.format(
                res))
        sleep(0.1)
        print(f'|Para \033[32m(\033[m\033[36m{res}\033[m\033[32m)\033[m usaremos               |')
        print('|O (c\033[35m15\033[m Fck  \033[35m15\033[m \033[32m MPA\033[m) de resistência     |')
        print("+========================================+")
        print('                     ')
        alt = float(input('altura\033[36m:\033[m '))
        lar = float(input('largura do tijolo\033[36m:\033[m '))
        comp = float(input('comprimento\033[36m:\033[m '))
        quantidade = float(input('quantas vezes será feita essa parede: '))
        skg = float(input('Saca de quantos kilos você usará Kg\033[36m:\033[m '))

        print('                 ')
        sleep(1)
        print('=' * 42)
        print(
            '\033[34m+===============\033[m( \033[37mCIMENTO\033[m )\033[34m==============+\033[m')
        print('=' * 42)
        tipo = '\033[32mCP2-E-32\033[m'
        print('|                                        |')
        print('|Então usaremos o cimento                |')
        print('|\033[m (\033[37m{}\033[m) de (\033[32m{}\033[m) kg                |'.format(tipo, skg))
        junta = 0.025
        m3 = (comp * alt) * 10 * lar * junta * quantidade  # metro cubico
        m2 = comp * alt * quantidade  # tijolo
        m1 = comp * alt
        print('|O volume total e  de (\033[34m{:.2f}\033[m) M³          |'.format(m3))
        print(f"|            Área total {m1:.2f}  M²        |")
        print('|                                        |')
        tijolo = 25.5
        cimento = 0.240
        cimentos = 240
        areia = 0.720
        areias = 720
        agua = 0.186
        aguas = 186
        aditivo = 0.050
        t1 = tijolo * m2
        c1 = (cimento / skg) * skg * m3  # kg
        c2 = (cimentos / skg) * m3  # sacas
        c3 = (cimento / skg)
        a1 = (areia / 18) * 18 * m3  # metro cubico ok
        a2 = (areias / 18) * m3  # latas ok
        ag1 = (agua / 18) * 18 * m3  # metro cubico
        ag2 = (aguas / 18) * m3  # latas
        ad1 = (aditivo / 18) * m3
        # s4aditivo = (aditivo * 10 * 10 / 10) / c3
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+==========\033[m(\033[37m TOTAL DE MATERIAL\033[m )\033[34m=========+\033[m')
        print('=' * 42)
        print('|       (\033[34m{:.3f}\033[m) kg de cimento            |'.format(c1))
        print(
            "|       (\033[34m{:.2f}\033[m) sacas de (\033[32m{}\033[m) kg        |".format(c2, skg))
        print('=' * 42)
        print('|       (\033[34m{:.3f}\033[m) M³  de areia             |'.format(a1))
        print('|       (\033[34m{:.2f}\033[m) latas de(\033[32m18\033[m) litros      |'.format(a2))
        print('=' * 42)
        print('|                (\033[34m{:.3f}\033[m) tijolos       |'.format(t1))
        print('=' * 42)
        print('|       (\033[34m{:.3f}\033[m) M³ de água               |'.format(ag1))
        print('|       (\033[34m{:.3f}\033[m) latas de (\033[32m18\033[m) litros    |'.format(ag2))
        print('=' * 42)
        print('|(\033[34m{:.2f}\033[m) litros de aditivo plástificante  |'.format(ad1))
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+=========\033[m( \033[37m TRAÇO DE ARGAMASSA\033[m )\033[34m========+\033[m')
        print('=' * 42)
        print('|                                        |')
        print('|Será feito (\033[34m{:.2f}\033[m) traços                |'.format(c2))
        print('|                                        |')
        print('|Para cada traço                         |')
        print('|\033[34m 1 \033[msaca de cimento de (\033[32m{}\033[m)            |'.format(skg))
        print('|                                        |')
        s1areia = (areias / 18) / c3
        s3agua = (aguas / 18) / c3
        s4aditivo = (aditivo * 10 * 10 / 10) / c3
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de areia de (\033[32m18\033[m) litros   |'.format(
            s1areia))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de água de (\033[32m18\033[m) litros     |'.format(
            ag2))
        print('|                                        |')
        print('=' * 42)

        print('|                                        |')
        print('|(\033[34m{:.3f}\033[m) ml de aditivo plástificante    |'.format(s4aditivo))
        print('|                                        |')
        print('\033[35m=\033[m' * 42)
        print('|                                        |')
        print('|para cimento de (\033[32m42.5\033[m) kg usar:         |')
        print('|padiola  de (\033[35m36.33\033[m) litros              |')
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+===============\033[m(\033[37m MEDIDAS\033[m )\033[34m==============+\033[m')
        print('=' * 42)
        print('|                                        |')
        print(
            '|\033[34mAREIA\033[m ( 20 \033[35mx\033[m 37 \033[35mx\033[m 49 )                  |')
        print(
            '|\033[34mSEIXO\033[m ( 21\033[35m x\033[m 37\033[35m x\033[m 49 )                  |')
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|Na compra de material                   |')
        print('|Você deve acrecentar                    |')
        print('|desperdicio na ordem de (\033[37m10%\033[m)           |')
        print('|slump de(\033[37mabatimento\033[m) (\033[32m08\033[m)cm             |')
        print('|                                        |')
        print('\033[37m=\033[m' * 42)
        print('|                                        |')
        print(
            '|Seu calculo foi realizado com \033[35m(\033[mmsucesso\033[35m)\033[m |')
        print('|                                        |')
        print('=' * 42)
        print('=' * 42)
        print('                  ')
    if res == 'reboco':
        sleep(0.1)
        print("+========================================+")
        sleep(0.1)
        print("|                 \033[34mReboco\033[m                 |")
        print(
            '|(\033[36m{}\033[m) adicionado com\033[32m sucesso\033[m!        |'.format(
                res))
        sleep(0.1)
        print(
            f'|               Para \033[32m(\033[m\033[36m{res}\033[m\033[32m)\033[m            |')
        print(
            '|usaremos o (c\033[35m20\033[m Fck  \033[35m20\033[m \033[32m MPA\033[m)          |')
        print("+========================================+")
        print('                     ')
        alt = float(input('altura\033[36m:\033[m '))
        lar = float(input('largura do reboco\033[36m:\033[m '))
        comp = float(input('comprimento\033[36m:\033[m '))
        quantidade = float(input('quantas vezes será feita essa parede: '))
        skg = float(input('Saca de quantos kilos você usará Kg\033[36m:\033[m '))

        print('                 ')
        sleep(1)
        print('=' * 42)
        print(
            '\033[34m+===============\033[m( \033[37mCIMENTO\033[m )\033[34m==============+\033[m')
        print('=' * 42)
        tipo = '\033[37mCP2-E-32\033[m'
        print('|                                        |')

        print('|Então usaremos o cimento')
        print('(\033[37m{}\033[m) de (\033[37m{}\033[m) kg     |'.format(tipo,
                                                                                                                 skg))
        print('|                                        |')

        m3 = (comp * alt) * lar * quantidade  # metro cubico
        m1 = comp * alt
        print('|O volume total e  de (\033[34m{:.2f}\033[m) M³          |'.format(m3))
        print(f"|Área total {m1:.2f}  M²                     |")
        print('|                                        |')
        cimento = 0.240
        cimentos = 240
        areia = 0.720
        areias = 720

        agua = 0.186
        aguas = 186
        aditivo = 0.050
        c1 = (cimento / skg) * skg * m3  # kg
        c2 = (cimentos / skg) * m3  # sacas
        c3 = (cimento / skg)
        a1 = (areia / 18) * 18 * m3  # metro cubico ok
        a2 = (areias / 18) * m3  # latas ok
        ag1 = (agua / 18) * 18 * m3  # metro cubico
        ag2 = (aguas / 18) * m3  # latas
        ad1 = (aditivo / 18) * m3
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+==========\033[m(\033[37m TOTAL DE MATERIAL\033[m )\033[34m=========+\033[m')
        print('=' * 42)
        print('|       (\033[34m{:.3f}\033[m) kg de cimento            |'.format(c1))
        print(
            "|       (\033[34m{:.2f}\033[m) sacas de (\033[32m{}\033[m) kg           |".format(c2, skg))
        print('=' * 42)
        print('|       (\033[34m{:.3f}\033[m) M³  de areia             |'.format(a1))
        print('|       (\033[34m{:.2f}\033[m) latas de(\033[32m18\033[m) litros      |'.format(a2))
        print('\033[36m=\033[m' * 42)
        print('\033[35m=\033[m' * 42)
        print('|       (\033[34m{:.3f}\033[m) M³ de água               |'.format(ag1))
        print('|       (\033[34m{:.3f}\033[m) latas de (\033[32m18\033[m) litros     |'.format(ag2))
        print('\033[35m=\033[m' * 42)
        print('|(\033[34m{:.2f}\033[m) litros de aditivo plástificante |'.format(ad1))
        print('|                                                     |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+========\033[m( \033[37m TRAÇO DE ARGAMASSA\033[m )\033[34m=========+\033[m')
        print('=' * 42)
        print('|                                        |')
        print('|Será feito (\033[34m{:.2f}\033[m) traços                |'.format(c2))
        print('|Para cada traço                         |')
        print('|1 saca de cimento de (\033[32m{}\033[m)|'.format(skg))
        print('|                                        |')
        s1areia = (areias / 18) / c3
        s3agua = (aguas / 18) / c3
        s4aditivo = (aditivo * 10 * 10 / 10) / c3
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de areia de (\033[32m18\033[m) litros |'.format(
            s1areia))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|(\033[34m{:.2f}\033[m) latas de água de (\033[32m18\033[m) litros     |'.format(
            ag2))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')

        print('|(\033[34m{:.3f}\033[m) ml de aditivo plástificante    |'.format(s4aditivo))
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|para cimento de (\033[32m42.5\033[m) kg usar:         |')
        print('|padiola  de (\033[35m36.33\033[m) litros              |')
        print('|                                        |')
        print('=' * 42)
        sleep(0.1)
        print(
            '\033[34m+===============\033[m(\033[32m MEDIDAS\033[m )\033[34m==============+\033[m')
        print('=' * 42)

        print('|                                        |')
        print(
            '|\033[34mAREIA\033[m ( 20 \033[35mx\033[m 37 \033[35mx\033[m 49 )                  |')
        print(
            '|\033[34mSEIXO\033[m ( 21\033[35m x\033[m 37\033[35m x\033[m 49 )                  |')
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print('|Na compra de material                   |')
        print('você deve acrecentar                     |')
        print('|desperdicio na ordem de (\033[32m10%\033[m)           |')
        print('|slump de(\033[37mabatimento\033[m) (\033[32m08\033[m)cm             |')
        print('|                                        |')
        print('=' * 42)
        print('|                                        |')
        print(
            '|seu calculo foi realizado com \033[35m(\033[m\033[32msucesso\033[m\033[35m)\033[m |')
        print('|                                        |')
        print('=' * 42)
        print('                  ')
    else:
        print("Deseja fazer mais algum calculo!")
