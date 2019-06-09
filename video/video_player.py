#!/usr/bin/env python3
# from VLC import Instance, logging, sys,os, PlaybackMode
from VLC import *
import time

if __name__ == '__main__':
           
    
    movie = "new.mov"
    movie = os.path.expanduser(movie)
    # if not os.access(movie, os.R_OK):
    #     print('Error: %s file not readable' % movie)
    #     sys.exit(1)
    instance = Instance('--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')
    try:
        media = instance.media_new(movie)
        
    except (AttributeError, NameError) as e:
        print(e)
        sys.exit(1)
    
    player = instance.media_player_new()
    player.set_media(media)
    player.play()
    player.toggle_fullscreen
    def quit_app():
        """Stop and exit"""
        sys.exit(0)
    while True:
        time.sleep(600)
        player.set_media(media)
        player.play()
        print("I'm awake!")
            # k = getch()
            # print('> %s' % k)
            # if k in keybindings:
            #     keybindings[k]()
            # elif k.isdigit():
            #      # jump to fraction of the movie.
            #     player.set_position(float('0.'+k))
               

