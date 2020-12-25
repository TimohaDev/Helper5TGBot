from pyrogram import Client, filters
import requests
from config import token, admins, api_hash, api_id
import time
commands = dict(root="commands")
app = Client("session", api_id, api_hash, bot_token=token, plugins=commands)



def register(user_id):
    file = open('db.txt', 'a')
    file.write(str(user_id) + '\n')
    file.close()

def is_registered(user_id):
    read = open('db.txt')


    if str(user_id) in read.read():
        result = True
    else:
        result = False

    return result


@app.on_message(filters.command('start'))
def start_message(client, message):
    if not is_registered(message.from_user.id):
        register(message.from_user.id)

    message.reply_text("Привет :) !help для получения помощи")

@app.on_message(filters.command("send"))
def send_command(client, message):
    if message.chat.id not in admins:
        pass
    else:
        file = open('db.txt')

        goods = 0
        unsuccessful = 0
        for i in file:
            try:
                app.forward_messages(i.strip(), message.chat.id, [message.reply_to_message.message_id], as_copy = True)
                time.sleep(0.04)
                goods += 1
            except Exception as e:
                print(e)
                unsuccessful += 1
                continue
        message.reply_text(f'<b>Рассылка завершена!</b>\n\nСтатистика:\nУспешно: {goods}\nНеуспешно: {unsuccessful}')






app.run()
