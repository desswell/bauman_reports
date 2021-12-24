import config
import logging
import translate
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pasring import parsing
from aiogram.types import BotCommand
from sub import sub
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot, storage=storage)
db = sub('db.db')
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/subscribe", description="Подписаться"),
        BotCommand(command="/unsubscribe", description="Отписаться"),
        BotCommand(command="/currency", description="Актуальный курс"),
        BotCommand(command="/translate", description="Обмен валюты")
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if not db.subscriber_exists(message.from_user.id):
        db.add_subscriber(message.from_user.id)
        await message.answer(
            "Вы успешно подписались на рассылку!\n Теперь вы можете получать актуальные курсы валюты")
    elif not db.subscriber_check(message.from_user.id):
        db.update_subscription(message.from_user.id, True)
        await message.answer("Вы подписались снова!")
    else:
        await message.answer("Вы уже подписаны")

# Команда отписки
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if not db.subscriber_exists(message.from_user.id):
        db.add_subscriber(message.from_user.id, False)
        await message.answer("Вы итак не подписаны.")
    else:
        db.update_subscription(message.from_user.id, False)
        await message.answer("Вы успешно отписаны от рассылки.")


@dp.message_handler(commands=['currency'])
async def currency(message: types.Message):
    if db.subscriber_exists(message.from_user.id) and db.subscriber_check(message.from_user.id):
        a = parsing()
        a[0] += ':'
        a[1] = 'USD: ' + a[1] + ' руб.'
        a[2] = 'EUR: ' + a[2] + ' руб.'
        for i in a:
            await message.answer(i)
    else:
        await message.answer(
            'Вы должны подписаться для получения актуальной информации.\nПропишите команду /subscribe и пользуйтесь любым предоставленным функционалом.')


if __name__ == '__main__':
    translate.register_handlers_translate(dp)
    executor.start_polling(dp, skip_updates=False)