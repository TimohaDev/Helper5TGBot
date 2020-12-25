from pyrogram import Client, filters


@Client.on_message(filters.command('shrug', ['!']))
def shrug(client, message):
    message.reply_text(f"¯\_(ツ)_/¯")
