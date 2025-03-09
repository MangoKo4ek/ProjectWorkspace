import logging
import asyncio
import re
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Filter
from aiogram.types import Message
from Config import TOKEN

# Настройка логирования
logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
    level=logging.INFO
)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()


# Фильтр для поиска вакансий
class VacancyFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        """
        Фильтр, который проверяет, содержит ли сообщение ключевые слова о вакансиях.
        """
        # Ключевые слова для поиска
        keywords = ["вакансия", "работа", "зарплата", "ищем"]
        text = message.text.lower()
        return any(keyword in text for keyword in keywords)


# Асинхронная функция для извлечения информации о вакансиях
async def extract_vacancy_info(text: str) -> list[dict]:
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


# Обработчик для сообщений с вакансиями
@dp.message(VacancyFilter())  # Применяем фильтр
async def handle_group_message(message: types.Message):
    # Извлекаем информацию о вакансиях из сообщения
    vacancies = await extract_vacancy_info(message.text)

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


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())