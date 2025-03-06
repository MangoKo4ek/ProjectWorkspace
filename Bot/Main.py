import logging
import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher


logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
    level=logging.INFO
)

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
