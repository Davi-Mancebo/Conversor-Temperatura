def conversor(a):
    from time import sleep
    while True:
        escolha = str(input("""Escolha um deses valores:
Celcius: C
Kelvin: K
Farenheit: F
Fechar programa: 0
Escolha: """)).strip().upper()[0]
        if escolha == '0':
            print('Obrigado por testar')
            break

        for c in range(0, 4):
            print('.', end=' ')
            sleep(0.5)
        if escolha == 'C':
            print()
            print(f'{a}°C')
        elif escolha == 'K':
            k = a + 273, 15
            print()
            print(f'{k}°K')
        elif escolha == 'F':
            f = (a * 9 / 5) + 32
            print()
            print(f'{f}°F')
            sleep(3)
        else:
            print('\nEscolha invalida!!')
            sleep(0.3)
        print('==' * 20)


print('-=' * 20)
print(f'{"CONVERSOR DE TEMPERATURA":^40}')
print('-=' * 20)

temp = float(input('Insira uma temperatura (C°): '))
conversor(temp)
