from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from Config import ADMIN_ID
from API import client_call
import re

FR = Router()

vacancies = {}


@FR.message(Command('add_vac_name'))
async def name_filter_def(message: Message, command: CommandObject):
    command_args: str = command.args
    if command_args:

        vacancies[message.from_user.id] = command_args
        await message.answer(f'установлено значение аргумента имени как "{command_args}"')
    else:
        await message.answer(f'воспользуйтесь командой /add_vac_name в формате: "/add_vac_name Название_Вакансии"')


@FR.message()
async def check_message(message: Message):
    text_message = await client_call()
    user_vacancy = text_message

    if user_vacancy:
        text = message.text.strip()

        vacancy_blocks = text.split("\n\n")

        for block in vacancy_blocks:

            if re.search(r'\b[\w.-]+@[\w.-]+\.\w+\b', block) and user_vacancy.lower() in block.lower():
                await message.bot.send_message(ADMIN_ID, f"📌 Найдена вакансия:\n\n{block.strip()}")
