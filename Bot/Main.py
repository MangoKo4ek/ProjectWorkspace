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
# логирование включает:
# 1.Имя файла
# 2.Номер строки
# 3.Уровень сообщения
# 4.Время логирования
# 5.Сам текст сообщения

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(FR)


@dp.message(
    CommandStart())  # декоратор  указывает, что функция, следующая за ним, будет обрабатывать определённые сообщения.
async def cmd_start(message: Message):
    await message.answer(
        f'Привет, {message.from_user.full_name}, этот бот поможет тебе с поиском подходящей тебе вакансии!\n'
        f'Воспользуйтесь командой /add_vac_name в формате:\n'
        f'"/add_vac_name Название_Вакансии", чтобы установить аргумент ожидания названия интересующей вакансии\n')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
