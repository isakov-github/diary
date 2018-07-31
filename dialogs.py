'''
file dialogs.py
ver 0.1
Created 31/07/2018 by Isakov V.E.
Various dialogs procedures
'''

#GLOBAL VARIABLES
lengs = {0:'english'}
commands = {'ld':'list of diaries, список доступних щоденників', 'cd':'create diary, створити новий щоденник', 'dd':'delete diary, видалити щоденник', 'ad':'archive diary, архівувати щоденник'}
diaries_list = ['My life', 'Art', 'Miscellaneous']
cur_diary = ''

def dialog(dlg):
    ''' Shows specific dialog depending on dlg value
        return value depends on dlg as well
        return False if not succeded
        possible values of dlg - ('language', 'user', 'diary', 'search')
    '''
    if dlg == 'language':
        if len(lengs) == 1:
            print('Currently only English available')
            return lengs[0]
        while(True):
            print('Please, choose a language (Press Enter to default English).')
            ans = input("Type 'help' for available languages: ")
            if (ans == 'help' or ans == 'h'):
                print('Available laguages:')
                for i, val in lengs.items():
                    print(i, '-', val)
            elif ans in lengs:
                current_language = ans
                return lengs[ans]
            elif ans == '':
                return lengs[0]
            else:
                print('Try again..')
    elif dlg == 'user':
        pass
    elif dlg == 'diary':
        while(True):
            cmd = input('Please, choose a diary or create a new one (h for help): ')
            if cmd.isnumeric():
                cmd = int(cmd)
                if cmd == 0:
                    print("Enter a number or diary's name")
                elif cmd <= len(diaries_list):
                    cur_diary = diaries_list[int(cmd)-1]
                    print("You've chosen the diary:", cur_diary)
                    return cur_diary
                else:
                    print(f'There are only {len(diaries_list)} diaries')
            else:
                cmd = cmd.split(' ')
                if(cmd[0] == 'help' or cmd[0] == 'h'):
                    for index, content in commands.items():
                        print(index + ' - ' + content)
                elif(cmd[0] in commands):
                    if(cmd[0] == 'ld'):
                        print('Available diaries:')
                        i = 0
                        for diaries in diaries_list:
                            i+=1
                            print(i, '-', diaries)
                    else:
                        print(commands[cmd[0]])
                else:
                    print('Try again..')
    elif dlg == 'search':
        pass
    else:
        print('DBG: ERROR: Func dialog - dlg isn"t in list')
