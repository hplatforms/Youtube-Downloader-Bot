from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"**Merhaba**\n\nBen Bir YouTube Video ve Ses İndirme Botuyum. Beni Kullanmak İçin Bana Bir YouTube URL Gönder VEYA @vid Yazarak İstediğin Videoyu Arayarak Bulabilirisin. Unutma Playlist Linklerini Desteklemiyorum.\n\n**Geliştirici**: @trbotlistesi\n**Yardım**: @trbotlistesidestek"
    await message.reply_text(helptxt)
