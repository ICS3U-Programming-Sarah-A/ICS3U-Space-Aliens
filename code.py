#!/usr/bin/env python3

# Created by: Sarah
# Created on: June 9th, 2022.
# This program  is the Space Alien program on the Pybadge.
import random
import time

# This line of code executes the libraries that have been
# imported
import constants
import stage
import ugame


def splash_scene():
    # this function the splash scene

    # imports the sound into the game
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # import image for the CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # set background image to 0 & the size
    # 10 x 8 tiles of the size 16x16
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    # used this program to split the image into tile:
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # create a stage for the background  to show up on
    # and the size (10x8 tiles of the size 16x16)
    game = stage.Stage(ugame.display, constants.FPS)

    # sets layer of all the spite so that items show up
    # in order
    game.layers = [background]

    # render all sprites
    game.render_block()

    # repeat forever
    while True:
        # a time in which it waits for 2 seconds
        time.sleep(2.0)
        menu_scene()


def menu_scene():
    # this function the menu scene

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

        # redraws the sprite
        game.tick()


def game_scene():
    # this function the main game scene

    # keeps track of the score
    score = 0
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {}".format(score))

    def show_alien():
        # this function takes an alien off from the screen & moves
        # it
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                break

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

    # imports the sound into the game
    boom_sound = open("boom.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # set background image to 0 & the size
    # 10 x 8 tiles of the size 16x16
    background = stage.Grid(
        image_bank_background, constants.SCREEN_X, constants.SCREEN_GRID_Y
    )

    # this loop selects a random image from the image bank. Each time
    # it loads it, it picks a different image.
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            title_picker = random.randint(1, 3)
            background.tile(x_location, y_location, title_picker)

    # the sprite will be updated every frame
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    # creates a list of aliens & places them onto the screen, then
    # add it to the list of aliens
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(
            image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        aliens.append(a_single_alien)
    # place 1 alien on the screen
    show_alien()

    # creates a list of laster for when we shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(
            image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
    lasers.append(a_single_laser)

    # create a stage for the background  to show up on
    # and the size (10x8 tiles of the size 16x16)
    game = stage.Stage(ugame.display, constants.FPS)

    # sets layer of all the spite so that items show up
    # in order
    game.layers = [score_text] + lasers + [ship] + aliens + [background]

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
            pass
        if keys & ugame.K_SELECT:
            pass

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
            # fires a laser if all hasn't been used yet
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break

        # sound play pew sound then breaks out of loop ^
        # each frame move the lasers, that have been fired
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(
                    lasers[laser_number].x,
                    lasers[laser_number].y - constants.LASER_SPEED,
                )
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

        # checks to see if the alien is on the screen
        # moves its
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(
                    aliens[alien_number].x,
                    aliens[alien_number].y + constants.ALIEN_SPEED,
                )
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )
                    show_alien()
                    score -= 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score {}".format(score))

        # this loop keeps in check of the collison &
        # if the laser hits on of the aliens, as well as the bounding
        # boxes
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(
                            lasers[laser_number].x + 6,
                            lasers[laser_number].y + 2,
                            lasers[laser_number].x + 11,
                            lasers[laser_number].y + 12,
                            aliens[alien_number].x + 1,
                            aliens[alien_number].y,
                            aliens[alien_number].x + 15,
                            aliens[alien_number].y + 15,
                        ):
                            # you hit an alien
                            aliens[alien_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            lasers[laser_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {}".format(score))

        # redraws the ship
        game.render_sprites(aliens + lasers + [ship])
        game.tick()


if __name__ == "__main__":
    splash_scene()
