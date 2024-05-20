from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('1 скилл')
    button_2 = KeyboardButton('2 скилл')
    button_3 = KeyboardButton('3 скилл')
    button_4 = KeyboardButton('4 скилл')
    button_5 = KeyboardButton('ульта')
    button_6 = KeyboardButton('SF')
    button_7 = KeyboardButton('перейти на 2 клаву')
    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_8 = KeyboardButton(' хускар ')
    button_9 = KeyboardButton('байбек')
    keyboard_2.add(button_8, button_9, )
    return keyboard_2
