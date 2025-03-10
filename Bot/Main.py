import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from Filter import FR

from Config import TOKEN

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
    level=logging.INFO
)

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(FR)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'Привет, {message.from_user.full_name}, этот бот поможет тебе с поиском подходящей тебе вакансии!'
        f'воспользуйтесь командой /add_vac_name в формате:'
        f'"/add_vac_name Название_Вакансии", чтобы установить аргумент ожидания названия интересующей вакансии')
    await message.answer(f'{message.from_user.id}')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
