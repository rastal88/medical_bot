from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram import F
from aiogram.types import Message
from keyboards.symptoms_keyboard import *
from lexicon import lexicon


router: Router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    keyboard = get_symptoms_keyboard()
    await message.answer(lexicon.LEXICON_1['/start'], reply_markup=keyboard)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(lexicon.LEXICON_1['/help'])


@router.message(F.text.contains(lexicon.LEXICON_2['/cold']))
async def get_symptoms_handler(message: Message):
    keyboard2 = post_symptoms_keyboard()
    await message.answer("Выберите симптомы, которые у вас есть:", reply_markup=keyboard2)


@router.message(F.text.contains(lexicon.LEXICON_3['/general']))
async def diagnose_handler(message: Message):
    response = lexicon.LEXICON_4['/general']
    await message.answer(response)


@router.message(F.text.contains(lexicon.LEXICON_3['/cough']))
async def diagnose_handler(message: Message):
    response = lexicon.LEXICON_4['/cough']
    await message.answer(response)


@router.message(F.text.contains(lexicon.LEXICON_3['/runny_nose']))
async def diagnose_handler(message: Message):
    response = lexicon.LEXICON_4['/runny_nose']
    await message.answer(response)


@router.message(F.text.contains(lexicon.LEXICON_3['/sore_throat']))
async def diagnose_handler(message: Message):
    response = lexicon.LEXICON_4['/sore_throat']
    await message.answer(response)


@router.message(F.text.contains(lexicon.LEXICON_3['/fever']))
async def diagnose_handler(message: Message):
    response = lexicon.LEXICON_4['/fever']
    await message.answer(response)
