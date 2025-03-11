from aiogram import types, Dispatcher
from function import func

dp = Dispatcher()

@dp.message()  
async def handler(message: types.Message):
    
    vcs = func(message.text)

    if vcs:
        for vc in vcs:
            response = (
                f"📌 Вакансия: {vc['title']}\n"
                f"💸 Зарплата: {vc['salary']}\n"
                f"📧 Контакты: {vc['contacts']}\n"
                f"📄 Описание:\n{vc['description']}"
            )

            
            await message.answer(response)
