import asyncio
import logging
from pprint import pprint
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import CommandStart
from config import TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove
from api import values
import app.keyboards as kb

router = Router()


def formatted(spisok):
    return "\n".join(spisok)


def outputInfo(dict):
    textum = []
    time = dict['time']
    program = dict['program']
    zipped = zip(time, program)
    print(zipped)
    for item in zipped:
        textum.append(f"{item[0]} — {item[1]}")
    # return formatted(textum)
    return '\n'.join(textum)


@router.message(CommandStart())
async def cmd_start(msg: types.Message) -> None:
    await msg.answer(
        'Добро пожаловать в SumikoTV!\nПо команде /schedule '
        'можно открыть расписание телепередач на текущую неделю')


@router.message(F.text == '/schedule')
async def show_schedule_kb(msg: types.Message):
    await msg.reply('Вот расписание', reply_markup=kb.main)


@router.message(lambda message: message.text == 'ПН')
async def show_monday_schedule(message: types.Message):
    schedule = values['values']
    monday = {
        'time': [],
        'program': [],
    }
    for i in range(len(schedule)):
        if i == 0:
            continue
        else:
            monday['time'].append(schedule[i][0])
            monday['program'].append(schedule[i][1])

    await message.reply(f"Ваше расписание на понедельник:\n{outputInfo(monday)}",
                        reply_markup=ReplyKeyboardRemove())


@router.message(lambda message: message.text == 'ВТ')
async def show_monday_schedule(message: types.Message):
    schedule = values['values']
    tuesday = {
        'time': [],
        'program': [],
    }
    for i in range(len(schedule)):
        if i == 0:
            continue
        else:
            tuesday['time'].append(schedule[i][0])
            tuesday['program'].append(schedule[i][2])

    await message.reply(f"Ваше расписание на вторник:\n{outputInfo(tuesday)}",
                        reply_markup=ReplyKeyboardRemove())


@router.message(lambda message: message.text == 'СР')
async def show_monday_schedule(message: types.Message):
    schedule = values['values']
    wednesday = {
        'time': [],
        'program': [],
    }
    for i in range(len(schedule)):
        if i == 0:
            continue
        else:
            wednesday['time'].append(schedule[i][0])
            wednesday['program'].append(schedule[i][3])

    await message.reply(f"Ваше расписание на среду:\n{outputInfo(wednesday)}",
                        reply_markup=ReplyKeyboardRemove())


@router.message(lambda message: message.text == 'ЧТ')
async def show_monday_schedule(message: types.Message):
    schedule = values['values']
    thursday = {
        'time': [],
        'program': [],
    }
    for i in range(len(schedule)):
        if i == 0:
            continue
        else:
            thursday['time'].append(schedule[i][0])
            thursday['program'].append(schedule[i][4])

    await message.reply(f"Ваше расписание на четверг:\n{outputInfo(thursday)}",
                        reply_markup=ReplyKeyboardRemove())


@router.message(lambda message: message.text == 'ПТ')
async def show_monday_schedule(message: types.Message):
    schedule = values['values']
    friday = {
        'time': [],
        'program': [],
    }
    for i in range(len(schedule)):
        if i == 0:
            continue
        else:
            friday['time'].append(schedule[i][0])
            friday['program'].append(schedule[i][5])

    await message.reply(f"Ваше расписание на четверг:\n{outputInfo(friday)}",
                        reply_markup=ReplyKeyboardRemove())


@router.message(lambda message: message.text == 'СБ')
async def show_monday_schedule(message: types.Message):
    schedule = values['values']
    saturday = {
        'time': [],
        'program': [],
    }
    for i in range(len(schedule)):
        if i == 0:
            continue
        else:
            saturday['time'].append(schedule[i][0])
            saturday['program'].append(schedule[i][6])

    await message.reply(f"Ваше расписание на субботу:\n{outputInfo(saturday)}",
                        reply_markup=ReplyKeyboardRemove())


@router.message(lambda message: message.text == 'ВСК')
async def show_monday_schedule(message: types.Message):
    schedule = values['values']
    sunday = {
        'time': [],
        'program': [],
    }
    for i in range(len(schedule)):
        if i == 0:
            continue
        else:
            sunday['time'].append(schedule[i][0])
            sunday['program'].append(schedule[i][7])

    await message.reply(f"Ваше расписание на воскресенье:\n{outputInfo(sunday)}",
                        reply_markup=ReplyKeyboardRemove())