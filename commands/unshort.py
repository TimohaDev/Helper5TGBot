from pyrogram import Client, filters
import requests

@Client.on_message(filters.command('unshort', ['!']))
def unshort(client, message):
    link = ' '.join(message.command[1:])
    if link:
        try:
            response = requests.get(f'https://unshorten.me/s/{message.text[9:]}')
            message.reply_text(response.text, disable_web_page_preview=True)
        except:
            message.reply_text(f"Что-то не то")
    else:
        message.reply_text("У этой команды должен быть 1 аргумент")
