import logging
import asyncio
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import Command
import config

API_TOKEN = config.token

# Enable logging to see messages in the console
logging.basicConfig(level=logging.INFO)
API_TOKEN="8175675277:AAGTN7Emrv2_gAqWxPRYHDG0TFp_sKOej7k"
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()


@router.message(Command("start"))
async def send_welcome(message: types.Message):
   await message.answer("Привет!  Выберите опцию:")
    

@router.message()
async def echo(message: types.Message):
    await message.answer(message.text)


dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
