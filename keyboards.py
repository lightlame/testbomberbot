from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

#Valorant command keyboard
unsubscribe_button = InlineKeyboardButton('🔕', callback_data='unsubscribe_1')
subscribe_button = InlineKeyboardButton('🔔', callback_data='subscribe_1')
valorant = InlineKeyboardMarkup(row_width=1).row(subscribe_button, unsubscribe_button)

#Setlang keyboard
russian_button = InlineKeyboardButton('russian', callback_data='0')
english_button = InlineKeyboardButton('english', callback_data='1')
setlang = InlineKeyboardMarkup().row(russian_button, english_button)

#Support button
support = InlineKeyboardMarkup()
support.add(InlineKeyboardButton('💵', url='https://www.donationalerts.com/r/patchnotebot'))