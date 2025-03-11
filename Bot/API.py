from telethon import TelegramClient
from Config import API_HASH, API_ID, PHONE_NUMBER

api_id = API_ID
api_hash = API_HASH
phone_number = PHONE_NUMBER

# Необходимо предварительно авторизоваться, чтобы был создан файл second_account,
# содержащий данные об аутентификации клиента.
client = TelegramClient(r"C:\Users\user\PycharmProjects\ProjectWorkspace\Bot\your_account.session", api_id, api_hash)


async def client_call():  # функция просмотра сообщений из канала
    client.start(phone_number)

    ch_id = '@careernitumisis'  # Канал
    dp = await client.get_entity(ch_id)  # Получаем сущность канала

    # Получаем последнее сообщение
    message = await client.get_messages(dp, limit=1)
    return message
