from pyrogram import Client, filters


@Client.on_message(filters.command('json', ['!']))
def json(client, message):
    message.reply_text(message.reply_to_message)
