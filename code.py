#!/usr/bin/env python3

# Created by: Sarah
# Created on: June 9th, 2022.
# This program  is the Space Alien program on the Pybadge.
import stage
import ugame
import constants

def game_scene():
    # this function the main game scene

    # import image for the CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # set background image to 0 & the size
    # 10 x 8 tiles of the size 16x16
    background = stage.Grid(image_bank_background, constants.SCREEN_X, constants.SCREEN_GRID_Y)

    # the sprite will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # create a stage for the background  to show up on
    # and the size (10x8 tiles of the size 16x16)
    game = stage.Stage(ugame.display, constants.FPS)

    # sets layer of all the spite so that items show up
    # in order
    game.layers = [ship] + [background]

    # render all sprites
    game.render_block()

    # repeat forever
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # this if statement executes user
        # input & does the following
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
        # update game logic for the characters to move

        # redraw the ship
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
