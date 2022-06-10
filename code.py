#!/usr/bin/env python3

# Created by: Sarah
# Created on: June 9th, 2022.
# This program  is the Space Alien program on the Pybadge.
import stage
import ugame


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
        keys = ugame.buttons.get_pressed()

        # this if statement executes user
        # input & does the following
        if keys & ugame.K_X:
            print("A has been pressed.")
        if keys & ugame.K_O:
            print("B has been pressed.")
        if keys & ugame.K_START:
            print("Start has been pressed.")
        if keys & ugame.K_SELECT:
            print("Select has been pressed.")
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
        # update game logic for the characters to move

        # redraw the ship
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
