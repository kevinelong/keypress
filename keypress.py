import curses

GET_KEY_MAP = {
    (27, 79, 80): 'F1',
    (27, 79, 81): 'F2',
    (27, 79, 82): 'F3',
    (27, 79, 83): 'F4',
    (27, 79, 84): 'F5',
    (27, 79, 85): 'F6',
    (27, 79, 86): 'F7',
    (27, 79, 87): 'F8',
    (27, 79, 88): 'F9',
    (27, 79, 89): 'F10',
    (27, 79, 90): 'F11',
    (27, 79, 91): 'F12',
    (27, 91, 65): 'UP',
    (27, 91, 66): 'DOWN',
    (27, 91, 67): 'RIGHT',
    (27, 91, 68): 'LEFT',
    (27, 91, 72): 'HOME',
    (27, 91, 70): 'END',
    (27, 91, 51, 126): 'DELETE',
    (27, 91, 53, 126): 'PAGE_UP',
    (27, 91, 54, 126): 'PAGE_DOWN',
}


def get_key():
    keys = []
    keys.append(s.getch())
    if keys[0] == 27:
        keys.append(s.getch())
        if keys[1] in range(79, 92):
            keys.append(s.getch())
            if keys[2] in range(50, 59):
                keys.append(s.getch())
    keys = tuple(keys)
    if keys in GET_KEY_MAP:
        return GET_KEY_MAP[tuple(keys)]
    elif len(keys) > 1:
        return str(keys)
    else:
        return chr(keys[0])


s = curses.initscr()
curses.noecho()
playing = True

if __name__ == '__main__':
    while playing:
        k = get_key()
        print(k, end="", flush=True)
        if k == 'q':
            playing = False
    curses.endwin()
