from pyrogram import Client, filters
import requests

@Client.on_message(filters.command('short', ['!']))
def short(client, message):
    link = ' '.join(message.command[1:])
    if link:
        try:
            response = requests.get(f'https://is.gd/create.php?format=simple&url={message.text[6:]}')
            message.reply_text(response.text,disable_web_page_preview=True)
        except:
            message.reply_text(f"Что-то не то")
    else:
        message.reply_text("У этой команды должен быть 1 аргумент")
