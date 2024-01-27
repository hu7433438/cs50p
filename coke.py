coke_cost = 50

while True:
    coin = int(input('Insert Coin: '))
    if coin == 25 or coin == 10 or coin == 5:
        coke_cost -= coin
    if coke_cost <= 0:
        print(f'Change Owed: {-coke_cost}')
        break
    print(f'Amount Due: {coke_cost}')
