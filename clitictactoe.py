import os
import time
while True:
    os.system('cls')
    print('-'*10+'Tic-Tac-Toe'+'-'*10)
    op = input('\n1) Start\n2) Exit\nEnter Option ->')
    if op == '2':
        break
    l = '123456789'
    c = 0
    while True:
        os.system('cls')
        print('-'*10+'Tic-Tac-Toe'+'-'*10)
        k = 0
        space = 10
        for i in range(1,6):
            for j in range(1,12):
                if j%4==0 and (i==1 or i==3 or i==5):
                    print('|', end='')
                elif j%4==0:
                    print('+', end='')
                elif i%2 == 0:
                    print('-', end='')
                else:
                    if j==2 or j==6 or j==10:
                        print(l[k], end='')
                        k+=1
                    else:
                        print(' ',end='')
            print()
        if l[0] == l[1] == l[2] == 'O' or l[3] == l[4] == l[5] == 'O' or l[6] == l[7] == l[8] == 'O' or l[0] == l[3] == l[6] == 'O' or l[1] == l[4] == l[7] == 'O'\
            or l[2] == l[5] == l[8] == 'O' or l[0] == l[4] == l[8] == 'O' or l[2] == l[4] == l[6] == 'O':
            print('\n----O Won----\n')
            input('Press any key to continue')
            break

        if l[0] == l[1] == l[2] == 'X' or l[3] == l[4] == l[5] == 'X' or l[6] == l[7] == l[8] == 'X' or l[0] == l[3] == l[6] == 'X' or l[1] == l[4] == l[7] == 'X'\
            or l[2] == l[5] == l[8] == 'X' or l[0] == l[4] == l[8] == 'X' or l[2] == l[4] == l[6] == 'X':
            print('\n----X Won----\n')
            input('Press any key to continue')
            break
        
        if c%2==0:
            n = input('\nPlayer-1->')
        else:
            n = input('\nPlayer-2->')

        if n.isnumeric() and int(n)>=1 and int(n)<=9:
            if l[int(n)-1] == 'O' or l[int(n)-1] == 'X':
                print('Already taken')
                input('Press any key to continue')
            else:
                if c%2==0:
                    l = l.replace(l[int(n)-1],'O')
                else:
                    l = l.replace(l[int(n)-1],'X')
                c+=1
        elif n == 'r' or n == 'R':
            l = '123456789'
            c = 0 
        elif n == 'q' or n == 'Q':
            os.system('cls')
            break
        else:
            print('----Enter valid option----\nr or R for Reset\nq or Q for Quit')
            input('Press any key to continue')