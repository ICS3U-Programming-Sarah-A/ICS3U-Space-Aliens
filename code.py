#!/usr/bin/env python3

# Created by: Sarah
# Created on: June 9th, 2022.
# This program  is the Space Alien program on the Pybadge.
import ugame
import stage


def game_scene():
    # this function the main game scene 

    # import image for the CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # set background image to 0 & the size
    # 10 x 8 tiles of the size 16x16
    background = stage.Grid(image_bank_background, 10, 8)

    # create a stage for the background  to show up on
    # and set the frame rate to 0 fps
    game = stage.Stage(ugame.display, 60)
    
    # sets layer of all the spite so tha items show up
    # in order
    game.layers = [background]

    # render all sprites
    game.render_block()

    # repeat foever
    while True:
        pass # temp placehold

if __name__ == "__main__":
    game_scene()
