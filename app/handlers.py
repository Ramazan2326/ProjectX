import asyncio
import logging
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import CommandStart
from config import TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import app.keyboards as kb

router = Router()


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
    await message.reply("Ваше расписание на понедельник...", reply_markup=ReplyKeyboardRemove())


@router.message(lambda message: message.text == 'ВТ')
async def show_monday_schedule(message: types.Message):
    await message.reply("Ваше расписание на вторник...", reply_markup=ReplyKeyboardRemove())


@router.message(lambda message: message.text == 'СР')
async def show_monday_schedule(message: types.Message):
    await message.reply("Ваше расписание на среду...", reply_markup=ReplyKeyboardRemove())


@router.message(lambda message: message.text == 'ЧТ')
async def show_monday_schedule(message: types.Message):
    await message.reply("Ваше расписание на четверг...", reply_markup=ReplyKeyboardRemove())


@router.message(lambda message: message.text == 'ПТ')
async def show_monday_schedule(message: types.Message):
    await message.reply("Ваше расписание на пятницу...", reply_markup=ReplyKeyboardRemove())
