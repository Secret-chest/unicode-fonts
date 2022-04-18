"""
Convert

This module contains functions for converting text to the different
fonts and adding modifiers.
"""

import fontData
from fallbacks import *


def toFont(text: str, fontName: str, fallback: int = ORIGINAL, blockCharacter: str = "�"):
    """
    Convert text to specified font
    :param text: str: Text to convert
    :param fontName: str: Font name
    :param fallback: int: Fallback method for unsupported characters (0 (ORIGINAL), 1 (SKIP), 2 (BLOCK), or 3 (ERROR)). Default 0.
    :param blockCharacter: str: Used for fallback when fallback is 2 (BLOCK). Default �.
    :return: str
    """

    # Get font data
    font = fontData.fonts[fontName]

    # Get supported, replacement, and, if applicable, space characters.
    supported = font[0]
    replaceWith = font[1]
    if len(font) > 2:
        space = font[2]
    else:
        space = ""

    # Replace characters.
    result = ""
    for i in text:
        if i in supported:
            result += replaceWith[supported.index(i)]  # add replacement character
        else:
            if fallback == 0:
                result += i  # add original
            elif fallback == 1:
                pass
            elif fallback == 2:
                result += blockCharacter  # add a block
            elif fallback == 3:
                result += replaceWith[supported.index(i)]  # just let it raise the error
            else:
                raise InvalidFallbackError(
                    "invalid fallback. Fallback must be 0 (ORIGINAL), 1 (SKIP), 2 (BLOCK), or 3 (ERROR)")
        result += space  # add space
    return result


def modify(text: str, modifierId: str, applyToSpaces: bool = False):
    """
    Adds modifier to text
    :param text: str: Text to modify
    :param modifierId: str: Modifier ID
    :param applyToSpaces: bool: Whether to apply modifiers to spaces. Default false.
    :return:
    """

    # Get modifier
    modifier = fontData.modifiers[modifierId]
    result = ""
    for i in text:
        if (not applyToSpaces and i not in "            ​") or applyToSpaces:
            result += modifier + i
        else:
            result += i
    return result

