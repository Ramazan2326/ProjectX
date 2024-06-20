from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='ПН'), KeyboardButton(text='ВТ'),
         KeyboardButton(text='СР'), KeyboardButton(text='ЧТ')],
        [KeyboardButton(text='ПТ'), KeyboardButton(text='СБ'),
         KeyboardButton(text='ВСК')]
    ], resize_keyboard=True, input_field_placeholder='Выбери день недели.')
