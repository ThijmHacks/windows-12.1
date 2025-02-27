import curses
import random
import time

def matrix_effect(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(50)  # Refresh rate
    
    sh, sw = stdscr.getmaxyx()  # Get screen height and width
    columns = [0] * sw  # Track the vertical position of each column

    while True:
        stdscr.clear()
        
        for i in range(sw):
            if columns[i] < sh and random.random() > 0.98:
                columns[i] += 1
            elif columns[i] >= sh:
                columns[i] = 0  # Reset to top
            
            char = random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%^&*")
            stdscr.addch(columns[i], i, char, curses.color_pair(1))
        
        stdscr.refresh()
        time.sleep(0.05)
        
        if stdscr.getch() == 27:  # Press ESC to exit
            break

def main():
    curses.wrapper(setup)

def setup(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    matrix_effect(stdscr)
