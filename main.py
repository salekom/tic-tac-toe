def game_field(field): # Print game`s field in console
    print('┌───┬───┬───┐')
    print(f'│ {field[0]} │ {field[1]} │ {field[2]} │')
    print('├───┼───┼───┤')
    print(f'│ {field[3]} │ {field[4]} │ {field[5]} │')
    print('├───┼───┼───┤')
    print(f'│ {field[6]} │ {field[7]} │ {field[8]} │')
    print('└───┴───┴───┘')

  
def player_turn(step): # Player turn function
    while True:
        if step == 'X':
            player_move = input('Первый игрок. \nВведите номер поля (число от 0 до 8) для хода крестиком "Х" - ')
        elif step == 'O':
            player_move = input('Второй игрок. \nВведите номер поля (число от 0 до 8) для хода ноликом "О" - ')
        if player_move not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
            print('\nВы ввели символ вместо числа. Повторите ввод.')
            continue
        player_move = int(player_move)
        if player_move >= 0 and player_move <= 8:
            if str(field[player_move]) not in 'OX':
                field[player_move] = step
                break
            else:
                print('\nПоле занято! Повторите ввод.')
        else:
            print('\nВы ввели неправильное число. Введите число от 0 до 8.')


def verification(field): # Verification triple win game combination
    jackpots = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)) # win triples
    for triple in jackpots:
        if field[triple[0]] == field[triple[1]] == field[triple[2]]: # if all fields is equale
            return field[triple[2]]                                  # rerurn win`s symbol,
    return False                                                     # otherwise game continues.


def basic(field): # Main function of program
    num = 0
    while True:
        game_field(field)
        if num % 2 == 0:
            player_turn('X')
        else:
            player_turn("O")
        num += 1
        if num >= 5:
            x = verification(field)
            if x == 'X':
                print('\nПобедил первый игрок!\n')
                break
            if x == 'O':
                print('\nПобедил второй игрок!\n')
                break
        if num == 9:
            print('\nИгра закончилась ничьёй!\n')
            break
    game_field(field)
    

repeat = False # Parameter for the first launch of the game
answer = 'y'   # Parameter for the first launch of the game
while True: # Loop to repeat the game
    if repeat:
        answer = input('''

Повторить игру? 
Нажмите "y" если Ваш ответ "да" или
"n" если Ваш ответ "нет": 
'''
)
    if answer in ['y','Y','н','Н','у','У', 'e', 'E']:
        print('Игра "Крестики-нолики"\n')
        field = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        basic(field)
        repeat = True
    elif answer in ['n','N','т','Т']:
        break # Exit the game
    else:
        print('\nВведён неверный символ! Повторите ввод.\n')
        continue
input('Игра закончена! Нажмите "Enter"!')