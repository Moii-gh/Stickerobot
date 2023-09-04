import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode

# Замените 'YOUR_API_TOKEN' на ваш токен бота
API_TOKEN = 'ТОКЕН'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Идентификатор стикера из вашего JSON-сообщения
CUSTOM_STICKER_ID = 'Индикатор'

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id

    # Отправляем стикер с использованием идентификатора из JSON
    await bot.send_sticker(user_id, CUSTOM_STICKER_ID)

    # Отправляем приветственное сообщение
    await message.reply("Добро пожаловать!")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
