from .__init__ import *

MSG = """
<b>Hey👋, I'm a @Internfreakbot Created By [Zaid](https://t.me/lulu786)</b>

<b>● Channel : [InternFreak Posts](https://t.me/internfreakposts)</b>
<b>● Language : [Python](https://www.python.org/)</b>
<b>● Library : [Pyrogram](https://docs.pyrogram.org/)</b>
<b>● Server : [Railway](https://railway.app/)</b>
<b>● Database : [Deta](https://deta.sh/)</b>
<b>● Credit : Everyone in this Journey</b>
"""


@bot.on_message(filters.command(['about', 'about@internfreakbot']))
async def about(_, message):
    await message.reply_text(MSG, disable_web_page_preview=True)
