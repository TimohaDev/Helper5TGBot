from pyrogram import Client, filters
import requests

@Client.on_message(filters.command('jac', ['!']))
def jac(client, message):
    text = ' '.join(message.command[1:])

    r = requests.get("https://api.timoha.site/generate_fresko", params={"text": text})
    if r.status_code == requests.codes.ok and r.json()["success"] == True:
        client.send_photo(message.chat.id, r.json()["url"], caption='Сгенерировано с помощью api.timoha.site')
    else:
        client.send_message(message.chat.id, 'Произошла ошибка')
