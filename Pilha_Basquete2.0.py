bolas = int(input('Entre com o total de bolas de basquete da escola: '))
bolas_de_basquete = list(range(1, bolas + 1))
bola_gasta = 0
while True:
    print('')
    print(f'Número de bolas de basquete da escola: {bolas_de_basquete}')
    print('Pressione D para desempilhar uma bola')
    print('Pressione E para empilhar a última bola retirada')
    print('Pressione R para repor um novo estoque de bolas, se o estoque estiver zerado')
    jogo = input('Pressione S para sair: ')
    if jogo == 'D':
        if (len(bolas_de_basquete)) > 0:
            bola_gasta = bolas_de_basquete.pop()
            print('')
            print(f'Bola {bola_gasta} utilizada')
        else:
            print('Não há nenhuma bola no estoque')
    elif jogo == 'R':
        if (len(bolas_de_basquete)) == 0:
            repor = int(input('Qual a quantidade de bolas que você deseja repor ?: '))
            bolas_de_basquete_reposta = list(range(1, repor + 1))
            bolas_de_basquete = bolas_de_basquete_reposta
        else:
            print('')
            print('É necessário que não haja bolas no estoque para executar esse comando')
    elif jogo == 'E':
        if bola_gasta > 0:
            bolas_de_basquete.append(bola_gasta)
            # bola_gasta+=1
        else:
            print('Só é possivel devolver ao estoque a última bola retirada')
    elif jogo == 'S':
        break
    else:
        print('')
        print('Comando inválido ! Digite somente D, E, R, S')
