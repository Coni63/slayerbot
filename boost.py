import pyautogui
import numpy as np

from pygetwindow import Win32Window
from PIL import Image

import constants


def handle_boost(tile: Win32Window, screenshot: Image):
    if _check_boost(screenshot):
        _click_boost(tile)


def _check_boost(image: Image) -> bool:
    """
    Check a small square on top of the boost button tu check if the timer is running (darker button)

    blue = 149 when mouse is over the boost button
    blue = 155 when the button is free
    blue < 149 when boost is active
    """
    region = (
        # left, top, right, bottom
        constants.SPRINT_BUTTON_AREA_LEFT,
        image.height - constants.SPRINT_BUTTON_AREA_TOP,
        constants.SPRINT_BUTTON_AREA_RIGHT,
        image.height - constants.SPRINT_BUTTON_AREA_BOTTOM
    )
    sub = image.crop(region)
    blue_intensity = np.array(sub).mean(axis=0).mean(axis=0)[2]
    return blue_intensity > 148


def _click_boost(game_tile: Win32Window) -> bool:
    """
    Click arount the middle of the button
    Not on top to not impact the average color checked for the boost availability
    """
    x = game_tile.left + constants.SIDE_OFFSET + constants.SPRINT_BUTTON_CLICK_LEFT
    y = game_tile.bottom - constants.SIDE_OFFSET - constants.SPRINT_BUTTON_CLICK_BOTTOM
    pyautogui.click(x=x, y=y)
