from .__init__ import *


@bot.on_message(filters.command(['start', 'start@internfreakbot']) & filters.private)
async def command3(_, message):
    await message.reply_text("<code>I am Alive :)</code>")
