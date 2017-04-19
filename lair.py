# -*- coding: utf-8 -*-
VERSION = "0.03.1a"

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import *
    from pygame.locals import *
    from model.Settings import Settings
    from model.Screen import Screen
    from model.Player import Player
    from model.Point import Point
except ImportError, err:
    print "couldn't load module. %s" % (err)
    sys.exit(2)

def main():
    # Initialise screen
    pygame.init()
    clock = pygame.time.Clock()
    #screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Lair')

    game_screen = Screen()
    game_screen.load_random_map(2048, 2048)
    game_screen.load_textures(os.path.join(os.getcwd(), 'img', 'textures.png'))
    player_start_pos = Point(512, 512, 0)
    player = Player(player_start_pos, 0, 25)

    game_screen.map.add_obj(player)

    print os.path.join(os.getcwd(), 'img', 'textures.png')
    while 1:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    player.start_move(u'UP')
                if event.key == K_DOWN:
                    player.start_move(u'DOWN')
                if event.key == K_LEFT:
                    player.start_move(u'LEFT')
                if event.key == K_RIGHT:
                    player.start_move(u'RIGHT')
            elif event.type == KEYUP:
                if event.key == K_UP:
                    player.stop_move(u'UP')
                if event.key == K_DOWN:
                    player.stop_move(u'DOWN')
                if event.key == K_LEFT:
                    player.stop_move(u'LEFT')
                if event.key == K_RIGHT:
                    player.stop_move(u'RIGHT')

        player.update()
        print player.center.coords
        game_screen.camera.center_on(player)
        print game_screen.camera.center.coords
        game_screen.blit()

        pygame.display.flip()

if __name__ == '__main__':
    main()
