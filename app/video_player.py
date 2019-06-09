#!/usr/bin/env python3
# from VLC import Instance, logging, sys,os, PlaybackMode
from VLC import *
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    try:
        from msvcrt import getch
    except ImportError:
        import termios
        import tty

        def getch():  # getchar(), getc(stdin)  #PYCHOK flake
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
            return ch

           
    if ( 1 ==1):
        movie = sys.argv.pop()
        movie = os.path.expanduser(movie)
        if not os.access(movie, os.R_OK):
            print('Error: %s file not readable' % movie)
            sys.exit(1)

        instance = Instance('--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')

        try:
            media = instance.media_new(movie)
            
        except (AttributeError, NameError) as e:
            print(e)
            sys.exit(1)
        
        player = instance.media_player_new()
        player.set_media(media)
        player.play()
        player.
        player.toggle_fullscreen

        def quit_app():
            """Stop and exit"""
            sys.exit(0)

        keybindings = {
            'q': quit_app,
            'f': player.toggle_fullscreen
            }

        print('Press q to quit, ? to get help.%s' % os.linesep)
        while True:
            k = getch()
            print('> %s' % k)
            if k in keybindings:
                keybindings[k]()
            elif k.isdigit():
                 # jump to fraction of the movie.
                player.set_position(float('0.'+k))
               

    else:
        print('Usage: %s [options] <movie_filename>' % sys.argv[0])
        print('Once launched, type ? for help.')
        print('')

