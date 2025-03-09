import logging
import asyncio
import re
from aiogram import Bot, Dispatcher, types
from Config import TOKEN

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


def extract_vacancy_info(text):
    """
    Извлекает информацию о вакансии из текста.
    :param text: Текст сообщения.
    :return: Список словарей с информацией о вакансиях.
    """
    # Разделяем текст на блоки (вакансии обычно разделены пустыми строками)
    blocks = re.split(r"\n\s*\n", text.strip())

    vacancies = []

    for block in blocks:
        # Извлекаем название вакансии (первая строка)
        title_match = re.search(r"^(.+?)\n", block)
        title = title_match.group(1).strip() if title_match else "Название не указано"

        # Извлекаем зарплату
        salary_match = re.search(r"зарплат[а-я]*\s*[:–-]?\s*([\d\s₽руб\.]+)", block, re.IGNORECASE)
        salary = salary_match.group(1).strip() if salary_match else "Не указана"

        # Извлекаем контакты (email)
        contacts_match = re.search(r"Контакты:\s*([\w.-]+@[\w.-]+\.\w+)", block, re.IGNORECASE)
        contacts = contacts_match.group(1).strip() if contacts_match else "Не указаны"

        # Формируем результат
        vacancy_info = {
            "title": title,
            "salary": salary,
            "contacts": contacts,
            "description": block.strip(),
        }
        vacancies.append(vacancy_info)

    return vacancies


@dp.message()  # Обработчик для всех сообщений
async def handle_group_message(message: types.Message):
    # Извлекаем информацию о вакансиях из сообщения
    vacancies = extract_vacancy_info(message.text)

    if vacancies:
        for vacancy in vacancies:
            # Формируем ответ
            response = (
                f"📌 Вакансия: {vacancy['title']}\n"
                f"💸 Зарплата: {vacancy['salary']}\n"
                f"📧 Контакты: {vacancy['contacts']}\n"
                f"📄 Описание:\n{vacancy['description']}"
            )

            # Отправляем результат пользователю
            await message.answer(response)
    else:
        await message.answer("Вакансии в сообщении не найдены.")