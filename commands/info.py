from pyrogram import Client, filters


@Client.on_message(filters.command('info', ['!']))
def info(client, message):
    if message.reply_to_message:
        user=message.reply_to_message.from_user
        message.reply_text(f'Имя: {user.first_name} \nФамилия: {user.last_name}\nВ сети: {user.status} \nАйди: {user.id} \nЮзернейм: @{user.username}\nЭто бот: {"✅" if user.is_bot else "❌"}\nЭто скамер: {"✅" if user.is_scam else "❌"}')
    else:
        message.reply_text(f"Сообщение должно быть реплаем")
