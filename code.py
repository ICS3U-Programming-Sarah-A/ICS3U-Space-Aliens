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
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # set background image to 0 & the size
    # 10 x 8 tiles of the size 16x16
    background = stage.Grid(image_bank_background, 10, 8)

    # the sprite will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # create a stage for the background  to show up on
    # and the size (10x8 tiles of the size 16x16)
    game = stage.Stage(ugame.display, 60)
    
    # sets layer of all the spite so that items show up
    # in order
    game.layers = [ship] + [background]

    # render all sprites
    game.render_block()

    # repeat forever
    while True:
        # get user input

        # update game logic for the characters to move

        # redraw the ship
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()
