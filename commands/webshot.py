from pyrogram import Client, filters


@Client.on_message(filters.command('webshot', ['!']))
def webshot(client, message):
    link = ' '.join(message.command[1:])
    if link:
        try:
            message.reply_document(f"https://webshot.deam.io/{message.text.split()[1]}/?width=1920&height=1080?type=png",caption=f"Скриншот сайта \"{message.text.split()[1]}\"")
        except:
            message.reply_text(f"Что-то не то")
    else:
        message.reply_text("У этой команды должен быть 1 аргумент")
