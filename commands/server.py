from pyrogram import Client, filters
import datetime
import os
import requests
import psutil

@Client.on_message(filters.command('server', ['!']))
def server(client, message):
    # get uptime of bot service

    time = os.popen("systemctl show Helper5TGbot --property=ActiveEnterTimestamp").read()[25:-14]
    time = datetime.datetime.strptime(time, '%Y-%m-%d')
    now = datetime.datetime.today()
    uptime = (now - time)

    # get last commit on github
    request_to_github = requests.get("https://api.github.com/repos/t1mosha/Helper5TGbot/commits")
    data = request_to_github.json()[0]
    url_last_commit = data["html_url"]

    # get count commands
    count_commands = os.listdir('commands')
    count_commands.remove("__pycache__")

    message.reply_text(f"<b>🤖 Информация о боте:</b>\n<b>Uptime:</b> {uptime.days} дней\n<b>Commit:</b> {url_last_commit}\n<b>Количество команд:</b> {len(count_commands)}\n\n<b>🌐 Информация о сервере:</b>\n<b>GPU Load:</b> {psutil.cpu_percent()}", disable_web_page_preview=True)
