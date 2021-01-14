from pyrogram import Client, filters


@Client.on_message(filters.command('json', ['!']))
def ping(client, message):
    message.reply_text(message)
