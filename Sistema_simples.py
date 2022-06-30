from time import sleep
import os


# DEFININDO FUNÇÕES

def clear():
    os.system('cls')


def linha():
    print('===' * 15)


def menu():
    print('''
  [ 1 ] Comprar
  [ 2 ] Encerrar
  ''')


def pagar():
    linha()
    print('''
  [ 1 ] Á vista
  [ 2 ] Parcelado em até 10x com juros de 5%''')
    linha()


def continuar():
    linha()
    print('Realizar uma nova compra? Sim ou Não:')


def parcela():
    linha()
    print('Em quantas vezes deseja parcelar?')
    linha()


# INICIANDO APLICAÇÃO
while True:
    linha()
    print('Sistema Simples')
    linha()
    menu()
    linha()
    escolha = int(input('Selecione a opção desejada:'))
    clear()

    # ESCOLHA
    if escolha == 1:
        linha()
        print('''
    CÓDIGO ELETRODOMÉSTICOS:
    [ 111 ] Televisão 42 polegadas:R$ 2500
    [ 112 ] Playstation 5:R$ 4100
    [ 113 ] Microondas:R$ 250''')
        linha()
        print('''
    CÓDIGO BRIQUEDOS
    [ 121 ] Boneca barbie:R$ 120
    [ 122 ] Carrinho ferrari:R$ 250
    [ 123 ] Bola de futebol:R$ 100''')
        linha()
        opcao = int(input('Selecione o iten desejado:'))
        clear()

        # TELEVISÃO 42 R$2500
        if opcao == 111:
            valor = 2500
            pagar()
            pg = int(input('Qual forma de pagamento:'))
            clear()
            if pg == 1:
                linha()
                print('Valor para pagamento:')
                linha()
                quanto = float(input(':R$'))
                clear()
                if quanto >= 2500:
                    total = quanto - 2500
                    linha()
                    print('Compra de Televisão 42 polegadas realizada com sucesso!!!')
                    linha()
                    sleep(3)
                    clear()
                    linha()
                    print('Valor do produto R${}. Você pagou com {:.2f} e receberá R${:.2f} de troco.'.format(valor,
                                                                                                              quanto,
                                                                                                              total))
                    continuar()
                    cont = str(input(':')).upper()
                    clear()
                    if cont == 'SIM':
                        continue
                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break
                else:
                    linha()
                    print('Compra não efetuada!!!')
                    linha()
                    sleep(1)
                    clear()
                    linha()
                    print('Valor inferior ao do produto, efetue o pagamento referente ao produto.')
                    linha()
                    sleep(3)
                    clear()


            elif pg == 2:
                linha()
                for i in range(2, 11):
                    soma = 2500 / i + (2500 * 5 / 100)
                    print('R$2500 x {} = R${:.2f}'.format(i, soma))
                parcela()
                vezes = int(input(':'))
                valor = 2500
                clear()

                if vezes == vezes:
                    linha()
                    print(
                        'Você selecionou pagar em {} vezes com inclusão de 5% que dá o total de R${:.2f}'.format(vezes,
                                                                                                                 valor + (
                                                                                                                             valor * 5 / 100)))
                    linha()
                    sleep(3)
                    clear()
                    linha()
                    print('Confirmar compra? Sim ou Não')
                    linha()
                    confirm = str(input(':')).upper()
                    clear()
                    if confirm == 'SIM':
                        linha()
                        print('Compra efetuada com sucesso!!!')
                        linha()
                        sleep(2)
                        clear()
                        continuar()
                        linha()
                        cont = str(input(':')).upper()
                        clear()
                        if cont == 'SIM':
                            continue

                        else:
                            linha()
                            print('ENCERRANDO SISTEMA...')
                            linha()
                            sleep(2)
                            clear()
                            linha()
                            print('VOLTE SEMPRE.')
                            linha()
                            sleep(1)
                            clear()
                            break


                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break

                        continuar()
                        linha()
                    cont = str(input(':')).upper()
                    clear()
                    if cont == 'SIM':
                        continue
                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break





        # PLAYSTATION 5 R$4100
        elif opcao == 112:
            valor = 4100
            pagar()
            pg = int(input('Qual forma de pagamento:'))
            clear()
            if pg == 1:
                linha()
                print('Valor para pagamento:')
                linha()
                quanto = float(input(':R$'))
                clear()
                if quanto >= 4100:
                    total = quanto - 4100
                    linha()
                    print('Compra de Playstation 5 realizada com sucesso!!!')
                    linha()
                    sleep(3)
                    clear()
                    linha()
                    print('Valor do produto R${}. Você pagou com R${:.2f} e receberá R${:.2f} de troco.'.format(valor,
                                                                                                                quanto,
                                                                                                                total))
                    continuar()
                    cont = str(input(':')).upper()
                    clear()
                    if cont == 'SIM':
                        continue
                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break
                else:
                    linha()
                    print('Compra não efetuada!!!')
                    linha()
                    sleep(1)
                    clear()
                    linha()
                    print('Valor inferior ao do produto, efetue o pagamento referente ao produto.')
                    linha()
                    sleep(3)
                    clear()

            elif pg == 2:
                linha()
                for i in range(2, 11):
                    soma = 4100 / i + (4100 * 5 / 100)
                    print('R$4100 x {} = R${:.2f}'.format(i, soma))
                parcela()
                vezes = int(input(':'))
                valor = 4100
                clear()

                if vezes == vezes:
                    linha()
                    print(
                        'Você selecionou pagar em {} vezes com inclusão de 5% que dá o total de R${:.2f}'.format(vezes,
                                                                                                                 valor + (
                                                                                                                             valor * 5 / 100)))
                    linha()
                    sleep(3)
                    clear()
                    linha()
                    print('Confirmar compra? Sim ou Não')
                    linha()
                    confirm = str(input(':')).upper()
                    clear()
                    if confirm == 'SIM':
                        linha()
                        print('Compra efetuada com sucesso!!!')
                        linha()
                        sleep(2)
                        clear()
                        continuar()
                        linha()
                        cont = str(input(':')).upper()
                        clear()
                        if cont == 'SIM':
                            continue

                        else:
                            linha()
                            print('ENCERRANDO SISTEMA...')
                            linha()
                            sleep(2)
                            clear()
                            linha()
                            print('VOLTE SEMPRE.')
                            linha()
                            sleep(1)
                            clear()
                            break


                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break

                        continuar()
                        linha()
                    cont = str(input(':')).upper()
                    clear()
                    if cont == 'SIM':
                        continue
                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break


        # MICROONDAS R$250
        elif opcao == 113:
            valor = 250
            pagar()
            pg = int(input('Qual forma de pagamento:'))
            clear()
            if pg == 1:
                linha()
                print('Valor para pagamento:')
                linha()
                quanto = float(input(':R$'))
                clear()
                if quanto >= 250:
                    total = quanto - 250
                    linha()
                    print('Compra de Microondas realizada com sucesso!!!')
                    linha()
                    sleep(3)
                    clear()
                    linha()
                    print('Valor do produto R${}. Você pagou com R${:.2f} e receberá R${:.2f} de troco.'.format(valor,
                                                                                                                quanto,
                                                                                                                total))
                    continuar()
                    cont = str(input(':')).upper()
                    clear()
                    if cont == 'SIM':
                        continue
                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break
                else:
                    linha()
                    print('Compra não efetuada!!!')
                    linha()
                    sleep(1)
                    clear()
                    linha()
                    print('Valor inferior ao do produto, efetue o pagamento referente ao produto.')
                    linha()
                    sleep(3)
                    clear()

            elif pg == 2:
                linha()
                for i in range(2, 11):
                    soma = 250 / i + (250 * 5 / 100)
                    print('R$250 x {} = R${:.2f}'.format(i, soma))
                parcela()
                vezes = int(input(':'))
                valor = 250
                clear()

                if vezes == vezes:
                    linha()
                    print(
                        'Você selecionou pagar em {} vezes com inclusão de 5% que dá o total de R${:.2f}'.format(vezes,
                                                                                                                 valor + (
                                                                                                                             valor * 5 / 100)))
                    linha()
                    sleep(3)
                    clear()
                    linha()
                    print('Confirmar compra? Sim ou Não')
                    linha()
                    confirm = str(input(':')).upper()
                    clear()
                    if confirm == 'SIM':
                        linha()
                        print('Compra efetuada com sucesso!!!')
                        linha()
                        sleep(2)
                        clear()
                        continuar()
                        linha()
                        cont = str(input(':')).upper()
                        clear()
                        if cont == 'SIM':
                            continue

                        else:
                            linha()
                            print('ENCERRANDO SISTEMA...')
                            linha()
                            sleep(2)
                            clear()
                            linha()
                            print('VOLTE SEMPRE.')
                            linha()
                            sleep(1)
                            clear()
                            break


                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break

                        continuar()
                        linha()
                    cont = str(input(':')).upper()
                    clear()
                    if cont == 'SIM':
                        continue
                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break





        # BONECA BARBIE
        elif opcao == 121:
            valor = 120
            pagar()
            pg = int(input('Qual forma de pagamento:'))
            clear()
            if pg == 1:
                linha()
                print('Valor para pagamento:')
                linha()
                quanto = float(input(':R$'))
                clear()
                if quanto >= 120:
                    total = quanto - 120
                    linha()
                    print('Compra de Boneca Barbie realizada com sucesso!!!')
                    linha()
                    sleep(3)
                    clear()
                    linha()
                    print('Valor do produto R${}. Você pagou com R${:.2f} e receberá R${:.2f} de troco.'.format(valor,
                                                                                                                quanto,
                                                                                                                total))
                    continuar()
                    cont = str(input(':')).upper()
                    clear()
                    if cont == 'SIM':
                        continue
                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break
                else:
                    linha()
                    print('Compra não efetuada!!!')
                    linha()
                    sleep(1)
                    clear()
                    linha()
                    print('Valor inferior ao do produto, efetue o pagamento referente ao produto.')
                    linha()
                    sleep(3)
                    clear()

            elif pg == 2:
                linha()
                for i in range(2, 11):
                    soma = 120 / i + (120 * 5 / 100)
                    print('R$120 x {} =   R${:.2f}'.format(i, soma))
                parcela()
                vezes = int(input(':'))
                valor = 120
                clear()

                if vezes == vezes:
                    linha()
                    print(
                        'Você selecionou pagar em {} vezes com inclusão de 5% que dá o total de R${:.2f}'.format(vezes,
                                                                                                                 valor + (
                                                                                                                             valor * 5 / 100)))
                    linha()
                    sleep(3)
                    clear()
                    linha()
                    print('Confirmar compra? Sim ou Não')
                    linha()
                    confirm = str(input(':')).upper()
                    clear()
                    if confirm == 'SIM':
                        linha()
                        print('Compra efetuada com sucesso!!!')
                        linha()
                        sleep(2)
                        clear()
                        continuar()
                        linha()
                        cont = str(input(':')).upper()
                        clear()
                        if cont == 'SIM':
                            continue

                        else:
                            linha()
                            print('ENCERRANDO SISTEMA...')
                            linha()
                            sleep(2)
                            clear()
                            linha()
                            print('VOLTE SEMPRE.')
                            linha()
                            sleep(1)
                            clear()
                            break


                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break

                        continuar()
                        linha()
                    cont = str(input(':')).upper()
                    clear()
                    if cont == 'SIM':
                        continue
                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break





        # CARRINHO FERRARI R$250
        elif opcao == 122:
            valor = 250
            pagar()
            pg = int(input('Qual forma de pagamento:'))
            clear()
            if pg == 1:
                linha()
                print('Valor para pagamento:')
                linha()
                quanto = float(input(':R$'))
                clear()
                if quanto >= 250:
                    total = quanto - 250
                    linha()
                    print('Compra de Carrinho Ferrari realizada com sucesso!!!')
                    linha()
                    sleep(3)
                    clear()
                    linha()
                    print('Valor do produto R${}. Você pagou com {:.2f} e receberá R${:.2f} de troco.'.format(valor,
                                                                                                              quanto,
                                                                                                              total))
                    continuar()
                    cont = str(input(':')).upper()
                    clear()
                    if cont == 'SIM':
                        continue
                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break
                else:
                    linha()
                    print('Compra não efetuada!!!')
                    linha()
                    sleep(1)
                    clear()
                    linha()
                    print('Valor inferior ao do produto, efetue o pagamento referente ao produto.')
                    linha()
                    sleep(3)
                    clear()

            elif pg == 2:
                linha()
                for i in range(2, 11):
                    soma = 250 / i + (250 * 5 / 100)
                    print('R$250 x {} = R${:.2f}'.format(i, soma))
                parcela()
                vezes = int(input(':'))
                valor = 250
                clear()

                if vezes == vezes:
                    linha()
                    print(
                        'Você selecionou pagar em {} vezes com inclusão de 5% que dá o total de R${:.2f}'.format(vezes,
                                                                                                                 valor + (
                                                                                                                             valor * 5 / 100)))
                    linha()
                    sleep(3)
                    clear()
                    linha()
                    print('Confirmar compra? Sim ou Não')
                    linha()
                    confirm = str(input(':')).upper()
                    clear()
                    if confirm == 'SIM':
                        linha()
                        print('Compra efetuada com sucesso!!!')
                        linha()
                        sleep(2)
                        clear()
                        continuar()
                        linha()
                        cont = str(input(':')).upper()
                        clear()
                        if cont == 'SIM':
                            continue

                        else:
                            linha()
                            print('ENCERRANDO SISTEMA...')
                            linha()
                            sleep(2)
                            clear()
                            linha()
                            print('VOLTE SEMPRE.')
                            linha()
                            sleep(1)
                            clear()
                            break


                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break

                        continuar()
                        linha()
                    cont = str(input(':')).upper()
                    clear()
                    if cont == 'SIM':
                        continue
                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break



        # BOLA DE FUTEBOL R$100
        elif opcao == 123:
            valor = 100
            pagar()
            pg = int(input('Qual forma de pagamento:'))
            clear()
            if pg == 1:
                linha()
                print('Valor para pagamento:')
                linha()
                quanto = float(input(':R$'))
                clear()
                if quanto >= 100:
                    total = quanto - 100
                    linha()
                    print('Compra de Bola de Futebol realizada com sucesso!!!')
                    linha()
                    sleep(3)
                    clear()
                    linha()
                    print('Valor do produto R${}. Você pagou com {:.2f} e receberá R${:.2f} de troco.'.format(valor,
                                                                                                              quanto,
                                                                                                              total))
                    continuar()
                    cont = str(input(':')).upper()
                    clear()
                    if cont == 'SIM':
                        continue
                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break
                else:
                    linha()
                    print('Compra não efetuada!!!')
                    linha()
                    sleep(1)
                    clear()
                    linha()
                    print('Valor inferior ao do produto, efetue o pagamento referente ao produto.')
                    linha()
                    sleep(3)
                    clear()

            elif pg == 2:
                linha()
                for i in range(2, 11):
                    soma = 100 / i + (100 * 5 / 100)
                    print('R$100 x {} = R${:.2f}'.format(i, soma))
                parcela()
                vezes = int(input(':'))
                valor = 100
                clear()

                if vezes == vezes:
                    linha()
                    print(
                        'Você selecionou pagar em {} vezes com inclusão de 5% que dá o total de R${:.2f}'.format(vezes,
                                                                                                                 valor + (
                                                                                                                             valor * 5 / 100)))
                    linha()
                    sleep(3)
                    clear()
                    linha()
                    print('Confirmar compra? Sim ou Não')
                    linha()
                    confirm = str(input(':')).upper()
                    clear()
                    if confirm == 'SIM':
                        linha()
                        print('Compra efetuada com sucesso!!!')
                        linha()
                        sleep(2)
                        clear()
                        continuar()
                        linha()
                        cont = str(input(':')).upper()
                        clear()
                        if cont == 'SIM':
                            continue

                        else:
                            linha()
                            print('ENCERRANDO SISTEMA...')
                            linha()
                            sleep(2)
                            clear()
                            linha()
                            print('VOLTE SEMPRE.')
                            linha()
                            sleep(1)
                            clear()
                            break


                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break

                        continuar()
                        linha()
                    cont = str(input(':')).upper()
                    clear()
                    if cont == 'SIM':
                        continue
                    else:
                        linha()
                        print('ENCERRANDO SISTEMA...')
                        linha()
                        sleep(2)
                        clear()
                        linha()
                        print('VOLTE SEMPRE.')
                        linha()
                        sleep(1)
                        clear()
                        break



        else:
            linha()
            print('Inválido! Tente novamente.')
            linha()
            sleep(1)
            clear()
            continue



    elif escolha == 2:
        linha()
        print('ENCERRANDO SISTEMA!!!')
        print('AGUARDE...')
        linha()
        sleep(2)
        clear()
        linha()
        print('Até a próxima.')
        linha()
        sleep(1.50)
        clear()
        break

    else:
        linha()
        print('Invalido, tente novamente!!!')
        linha()
        sleep(1)
        clear()
