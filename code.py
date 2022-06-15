#!/usr/bin/env python3

# Created by: Sarah
# Created on: June 9th, 2022.
# This program  is the Space Alien program on the Pybadge.
import ugame
import stage

import constants


def menu_scene():
    # this function the main game scene

    # import image for the CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # adds the text objects
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.NEW_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.NEW_PALETTE, buffer=None
    )
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # set background image to 0 & the size
    # 10 x 8 tiles of the size 16x16
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    # create a stage for the background  to show up on
    # and the size (10x8 tiles of the size 16x16)
    game = stage.Stage(ugame.display, constants.FPS)

    # sets layer of all the spite so that items show up
    # in order
    game.layers = text + [background]

    # render all sprites
    game.render_block()

    # repeat forever
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # this if statement executes user
        # input & does the following
        if keys & ugame.K_START != 0:
            game_scene()

        # redreaws the sprite
        game.tick()


def game_scene():
    # this function the main game scene

    # import image for the CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that keep state information
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # imports the sound into the game
    pew_sound = open("pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # set background image to 0 & the size
    # 10 x 8 tiles of the size 16x16
    background = stage.Grid(
        image_bank_background, constants.SCREEN_X, constants.SCREEN_GRID_Y
    )

    # the sprite will be updated every frame
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    alien = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # create a stage for the background  to show up on
    # and the size (10x8 tiles of the size 16x16)
    game = stage.Stage(ugame.display, constants.FPS)

    # sets layer of all the spite so that items show up
    # in order
    game.layers = [ship] + [alien] + [background]

    # render all sprites
    game.render_block()

    # repeat forever
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # this block of code executes when the A button is
        # pressed
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
            else:
                if a_button == constants.button_state["button_still_pressed"]:
                    a_button = constants.button_state["button_released"]
                else:
                    a_button = constants.button_state["button_up"]

        # this if statement executes user
        # input & does the following
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")

        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        # play sounds once A button has been pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
            # sound play pew sound
            pass

        # redraw the ship
        game.render_sprites([ship] + [alien])
        game.tick()


if __name__ == "__main__":
    menu_scene()
