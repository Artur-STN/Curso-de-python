print('\033[30;1m▲▼\033[m'*10)
num = int(input('\033[36;1mQuer ver a tabuada de qual valor?\033[m '))
uad = 1
while True:
    print('\033[30;1m▲▼\033[m' * 10)
    if num < 0:
        print('\033[32;1mPrograma Tabuada Encerrado. Volte Sempre!\033[m')
        break
    for tabuada in range(1, 11):
        print(f'\033[31;1m{num} \033[m\033[32;1mX \033[34;1m{uad} \033[m\033[33;1m= {num * uad}\033[m')
        uad += 1
        if uad >= 11:
            uad = 1
    print('\033[30;1m▲▼\033[m' * 10)
    num = int(input('\033[36;1mQuer ver a tabuada de qual valor?\033[m '))
    print('\033[30;1m▲▼\033[m'*10)
