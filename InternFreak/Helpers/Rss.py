from .__init__ import *
from ..Helpers.FetchPosts import fetch_posts
from InternFreak.config import CHANNEL, CODING_GROUP

def jsload(file):
    with open(file, 'r') as js:
        return json.load(js)


def jsdump(obj, file):
    with open(file, 'w') as js:
        json.dump(obj, js, indent=4)


async def save_posts():
    posts = await loop.run_in_executor(executor, lambda: fetch_posts())
    if posts:
        jsdump(posts, "Intern.json")


async def upload_posts():
    posts = jsload("Intern.json")
    result = await loop.run_in_executor(executor, lambda: fetchIds())
    for title, content in posts.items():
        CAPTION = ''
        if await loop.run_in_executor(executor, lambda: check(content["Link"])):
            CAPTION += f'<b>{title}</b>\n\n'
            for key, value in content.items():
                if key == 'Thumbnail' or key == 'Apply' or key == 'Link':
                    continue
                if isinstance(value, list):
                    KEY_POINTS = ''
                    for item in value:
                        KEY_POINTS += f'<code>{item}</code>\n'
                    CAPTION += f'<b>{key}</b> - {KEY_POINTS}\n\n'
                else:
                    CAPTION += f'<b>{key}</b> - <code>{value}</code>\n\n'
            button = [
                [
                    InlineKeyboardButton(
                        text="Apply", url=content["Apply"]),
                    InlineKeyboardButton(
                        text="Post Link", url=content["Link"]),
                ]
            ]
            markup = InlineKeyboardMarkup(inline_keyboard=button)
            try:
                post = await bot.send_photo(
                    chat_id=CHANNEL,
                    photo=content["Thumbnail"].replace(" ", "%20"),
                    caption=CAPTION,
                    reply_markup=markup,
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)

            except MediaCaptionTooLong:
                post = await bot.send_photo(
                    chat_id=CHANNEL,
                    photo=content["Thumbnail"].replace(" ", "%20"),
                    reply_markup=markup,
                )
            except:
                continue

            await bot.send_sticker(
                chat_id=CHANNEL,
                sticker="CAACAgUAAx0CSVhoDAABFM_aYk01ZlDsdO_9BtdfYyLaKwI0QJ4AAjsAA0NzyRIuGBJU0KTNKyME"
            )
            await loop.run_in_executor(executor, lambda: publish(content["Link"], title, str(post.id)))
            info = await bot.copy_message(chat_id=CODING_GROUP, from_chat_id=CHANNEL, message_id=post.id, reply_markup=markup)
            await bot.pin_chat_message(chat_id=CODING_GROUP, message_id=info.id)
            for users in result:
                try:
                    await bot.copy_message(chat_id=int(
                        users["key"]), from_chat_id=CHANNEL, message_id=post.id, reply_markup=markup)
                except FloodWait as e:
                    await asyncio.sleep(e.x)

            await asyncio.sleep(3)

save_post = AsyncIOScheduler()
save_post.add_job(save_posts, 'interval', minutes=1)
save_post.start()

upload_post = AsyncIOScheduler()
upload_post.add_job(upload_posts, 'interval', minutes=2)
upload_post.start()
