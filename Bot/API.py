from telethon import TelegramClient

api_id = 28243082  # API ID (получается при регистрации приложения на my.telegram.org)
api_hash = "a0a4287ff4b24a83c9cb4c2555339641"  # API Hash (оттуда же)
phone_number = "+79065027086"  # Номер телефона аккаунта, с которого будет выполняться код

# Необходимо предварительно авторизоваться, чтобы был создан файл second_account,
# содержащий данные об аутентификации клиента.
client = TelegramClient(r"C:\Users\user\PycharmProjects\ProjectWorkspace\Bot\your_account.session", api_id, api_hash)


async def client_call():
    client.start(phone_number)

    ch_id = '@careernitumisis'  # Канал
    dp = await client.get_entity(ch_id)  # Получаем сущность канала

    # Получаем последнее сообщение
    message = await client.get_messages(dp, limit=1)
    return message

