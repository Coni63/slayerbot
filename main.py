import time
import typing

import pyautogui
import pygetwindow
from pygetwindow import Win32Window
from PIL import Image

import constants
import boost



def find_window(appname) -> Win32Window:
    """
    Find the window of the game and return a reference to it

    https://pypi.org/project/PyGetWindow/

    game_tile.height
    game_tile.width
    game_tile.topleft
    ...
    """
    game_tile = pygetwindow.getWindowsWithTitle(appname)[0]

    return game_tile


def check_tile_is_active(game_tile: Win32Window):
    """
    restore it if needed and activate it to be on top for the screenshot.
    """
    if game_tile.isMinimized:
        game_tile.restore()

    if not game_tile.isActive:
        game_tile.activate()
        time.sleep(0.05)


def get_image(game_tile: Win32Window) -> Image:
    """
    Make a screenshot of the game window
    """
    a = game_tile.topleft
    region = (
        a.x + constants.SIDE_OFFSET,
        a.y + constants.TITLE_BAR_HEIGHT,
        game_tile.width - 2 * constants.SIDE_OFFSET,
        game_tile.height - constants.TITLE_BAR_HEIGHT - constants.SIDE_OFFSET
    )
    image = pyautogui.screenshot(region=region)
    return image


if __name__ == "__main__":
    pyautogui.PAUSE = 2.5
    pyautogui.FAILSAFE = True

    tile = find_window(constants.APP_NAME)  # will be update on window move

    while True:
        check_tile_is_active(tile)
        screenshot = get_image(tile)

        boost.handle_boost(tile, screenshot)

        time.sleep(0.3)
