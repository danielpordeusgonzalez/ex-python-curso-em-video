while True:
    n = int(input('quer ver a tabuada de que valor: '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 10):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)

