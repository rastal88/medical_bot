from lexicon import lexicon
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_symptoms_keyboard():
    kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    buttons: list[KeyboardButton] = [
        KeyboardButton(text=lexicon.LEXICON_2['/cold']),
        KeyboardButton(text=lexicon.LEXICON_2['/future'])
    ]
    kb_builder.row(*buttons)
    gs_kb: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True)
    return gs_kb


def post_symptoms_keyboard():
    kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    buttons: list[KeyboardButton] = [
        KeyboardButton(text=lexicon.LEXICON_3['/general']),
        KeyboardButton(text=lexicon.LEXICON_3['/cough']),
        KeyboardButton(text=lexicon.LEXICON_3['/runny_nose']),
        KeyboardButton(text=lexicon.LEXICON_3['/sore_throat']),
        KeyboardButton(text=lexicon.LEXICON_3['/fever'])
    ]

    kb_builder.row(*buttons, width=3)
    ps_kb: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True)
    return ps_kb
