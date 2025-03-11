from aiogram import types, Router
from function import func

rt = Router()

@rt.message()
async def handler(message: types.Message):
    
    vcs = func(message.text)

    if vcs:
        for vc in vcs:
            mes = (
                f"📌 Вакансия: {vc['title']}\n"
                f"💸 Зарплата: {vc['salary']}\n"
                f"📧 Контакты: {vc['contacts']}\n"
                f"📄 Описание: {vc['description']}"
            )

            
            await message.answer(mes)
