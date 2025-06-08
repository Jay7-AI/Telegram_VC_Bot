HELP_TEXT = """__**I Can Play Music In The Voice Chat**__

**/skip** __Skip The Current Playing Music.__
**/play** __Service_Or_Default (Services: youtube/saavn, Default: youtube) Song_Name | Reply_To_Audio__
**/joinvc** __Join Voice Chat.__
**/leavevc** __Leave Voice Chat.__
**/volume [1-200]** __Adjust Volume.__
**/pause** __Pause Music.__
**/resume** __Resume Music.__
**/queue plformat/Nothing** __Shows Queue List. If you send plformat with command you will get it in playlist format.__
**/delqueue** __Deletes Queue List and Playlist.__
**/playlist** __Start Playing Playlist.__
"""

REPO_TEXT = (
    "[Github](https://github.com/thehamkercat/Telegram_vc_bot)"
    + " | [Group](t.me/TGVCSUPPORT)"
)
from pyrogram import filters

@app.on_message(filters.command("J7Moody"))
async def flirty(client, message):
    await message.reply("Aapko yaad kar raha tha cutie 🥰😘")

@app.on_message(filters.command("ai"))
async def ai_gen(client, message):
    text = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else "Kuch toh bolo..."
    # Gemini ya OpenAI ka logic yahan dalna padega
    await message.reply(f"AI bolta hai: {text.upper()}")
