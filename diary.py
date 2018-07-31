'''
This project is in order to keep my everyday thoughts .. and then return to the past .. and understand something ...
Цей проект для того, щоб зберегти мої повсякденні думки.. і потім повернутися в минуле.. і збагнути дещо...
'''

commands = {'ld':'list of diaries, список доступних щоденників', 'cd':'create diary, створити новий щоденник', 'dd':'delete diary, видалити щоденник', 'ad':'archive diary, архівувати щоденник'}
diaries_list = ['My life', 'Art', 'Miscellaneous']
cur_diary = ''
print('Hello!')

dlg_flag = True
while(dlg_flag):
    cmd = input('Обери щоденник або створи новий (help, h - довідка): ')
#    cmd = cmd.split(' ')
    if cmd.isnumeric():
        cmd = int(cmd)
        if cmd == 0:
            print('Введи додатнє число більше нуля або назву щоденника')
        elif cmd <= len(diaries_list):
            cur_diary = diaries_list[int(cmd)-1]
            print('Ви обрали щоденник', cur_diary)
            dlg_flag = False
        else:
            print(f'У списку тільки {len(diaries_list)} щоденник(-a, -ів)')
    else:
        cmd = cmd.split(' ')
        if(cmd[0] == 'help' or cmd[0] == 'h'):
            for index, content in commands.items():
                print(index + ' - ' + content)
        elif(cmd[0] in commands):
            if(cmd[0] == 'ld'):
                print('Доступні щоденники:')
                i = 0
                for diaries in diaries_list:
                    i+=1
                    print(i, '-', diaries)
            else:
                print(commands[cmd[0]])
        else:
            print('Спробуй ще..')

# (список доступних щоденників - команда dl (diaries list))')
