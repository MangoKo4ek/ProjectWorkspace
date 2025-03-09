from telethon import TelegramClient

api_id = 28243082  # API ID (получается при регистрации приложения на my.telegram.org)
api_hash = "a0a4287ff4b24a83c9cb4c2555339641"  # API Hash (оттуда же)
phone_number = "+79065027086"  # Номер телефона аккаунта, с которого будет выполняться код

# Необходимо предварительно авторизоваться, чтобы был создан файл second_account,
# содержащий данные об аутентификации клиента.
client = TelegramClient(r"C:\Users\user\PycharmProjects\ProjectWorkspace\Bot\your_account.session", api_id, api_hash)


async def client_call():
    client.start(phone_number)

    username = '@careernitumisis'  # Канал
    dp = await client.get_entity(username)  # Получаем сущность канала

    # Получаем последнее сообщение
    messages = await client.get_message_history(dp, limit=1)  # Получаем одно сообщение
    text_message = messages[0].text  # Получаем текст первого сообщения из списка

    # Отключаемся от клиента
    await client.disconnect()

    # Возвращаем текстовое сообщение для дальнейшего использования
    return text_message
