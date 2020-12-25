from pyrogram import Client, filters


@Client.on_message(filters.command('members', ['!']))
def members(client, message):
    chat = ' '.join(message.command[1:])
    if chat:
        try:
            message.reply_text(f"Количество участников: {client.get_chat_members_count(f'{message.text[8:]}')} чел.")
        except:
            message.reply_text(f"Это не чат")
    else:
        message.reply_text("У этой команды должен быть 1 аргумент")
