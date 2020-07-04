from game import Game
import curses
import curses.ascii


class TextInterface:
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

        self.stdscr.keypad(True)
        self.stdscr.refresh()
        self.playing = True
        self.game = Game()

    def __del__(self):
        self.stdscr.clear()
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def draw(self):
        self.stdscr.clear()
        s = self.game.board.get_state()

        for y in range(len(s)):
            for x in range(len(s[y])):
                v = s[y][x]
                self.stdscr.addstr(y, x * 2, v)
        print(self.game.character.score)

    def stop(self):
        self.playing = False

    def user_input(self):
        k = self.stdscr.getch()

        if k in [curses.ascii.ESC, ord('q'), ord('Q'), ord('x'), ord('X')]:
            self.playing = False
        elif k in [curses.KEY_UP, ord('w'), ord('W')]:
            self.game.forward()
        elif k in [curses.KEY_LEFT, ord('a'), ord('A')]:
            self.game.turn_left()
        elif k in [curses.KEY_RIGHT, ord('d'), ord('D')]:
            self.game.turn_right()
        elif k in [curses.KEY_DOWN, ord('s'), ord('S')]:
            self.game.backward()

    def start(self):
        while self.playing:
            self.draw()
            self.user_input()
            self.game.check_collisions()


TextInterface().start()
