from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup[[
        InlineKeyboardButton("Kanal", url="https://t.me/trbotlistesi"),
        InlineKeyboardButton("Bildir", url="https://t.me/trbotlistesidestek")
    ],[
        InlineKeyboardButton("iletişim", url="https://t.me/trbotlistesidestek"),
        InlineKeyboardButton("iletişim", url="https://t.me/trbotlistesidestek")
    ]]
    welcomed = f"Merhaba <b>{message.from_user.first_name}</b>\nBen Bir YouTube Video ve Ses İndirme Botuyum. Beni Kullanmak İçin Bana Bir YouTube URL Gönder VEYA @vid Yazarak İstediğin Videoyu Arayarak Bulabilirisin"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
