from pyrogram import Client, filters


@Client.on_message(filters.command('help', ['!']))
def help(client, message):
    message.reply_text(f"Привет {message.from_user.mention}, вот мои команды:\n▪️<code>!info</code> - ответом на сообщение юзера пришлёт информацию о нём\n<code>▪️!ping</code> - Понг!\n▪️<code>!shrug</code> - ¯\_(ツ)_/¯\n▪️<code>!members <чат/канал></code> - количество участников\n▪️<code>!short <ссылка> </code> - сокращает ссылку\n▪️<code>!webshot <ссылка></code> - Скриншот сайта\n▪️<code>!unshort <ссылка> </code> - показывает куда была скорочена ссылка\n▪️ <code>!jac <ваш текст></code> - генерирует цитату от Жака Фреско\n▪️ <code>!server</code> - присылает информацию о сервере")
