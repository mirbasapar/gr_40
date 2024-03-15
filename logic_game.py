from decouple import config
from random import randint

list_slot = randint(1, 10)
mymoney = config('MY_MONEY', default = 1000, cast = int )
game_over = True

class GameCasino:

    def bet_money(self):
        global mymoney
        while 1:
            try:
                bet_user = int(input(f'Ваш баланс {mymoney}$\nВведите сумму ставки: '))

                if bet_user > mymoney:
                    print('У вас недостаточно денег в балансе')

                elif bet_user <= 0:
                    print('Введите положительное число!')

                else:
                    return bet_user

            except ValueError:
                print('Введите коректное число ( только цифры )')


    def bet_number(self):
        global list_slot
        while 1:
            try:
                bet_user = int(input('Введите число вашей ставки ( 1 до 10 ): '))

                if 1 <= bet_user <= 10:
                    return bet_user

                else:
                    print('Введите число от 1 до 10')

            except ValueError:
                print('Введите коректное число ( только цифры )')


    def play_game(self):
        global mymoney, game_over
        while mymoney > 0 and game_over:
            bet_money = self.bet_money()
            bet_number = self.bet_number()

            if bet_number == list_slot:
                print('YOU WIN')
                win_money = bet_money * 2
                print(f'+{win_money}$')
                mymoney -= bet_money
                mymoney += win_money
                print(f'Ваш баланс {mymoney}')

            else:
                print('YOU LOSE')
                mymoney -= bet_money


            if mymoney != 0:
                while 1:

                    user = input('Хотите продолжить игру ? (да или нет): ').lower()

                    if user=='нет':
                        print('GAME OVER')
                        game_over = False
                        break

                    elif user=='да':
                        break

                    else:
                        print('Введите "да" или "нет" !')

            else:
                print(f'Ваш баланс {mymoney}\nВы проиграли все деньги !\nGAME OVER')




# game = GameCasino()
# game.play_game()






