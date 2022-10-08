from .__init__ import *
from ..Helpers.FetchPosts import fetch_posts

CAPTION = """
<b>{title}</b>

<b>{date_key}</b> - <code>{date}</code>

<b>{description_key}</b> - <code>{description}</code>

<b>{deignation_key}</b> - <code>{deignation}</code>

<b>{batch_key}</b> - <code>{batch}</code>

<b>{salary_key}</b> - <code>{salary}</code>

<b>{important_key}</b> - <code>{important}</code>

<b>{location_key}</b> - <code>{location}</code>

<b>{extra_key}</b> - <code>{extra}</code>
"""

CHANNEL = -1001504019946
CODING_GROUP = -1001419259815


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
    for title, content in posts.items():
        if await loop.run_in_executor(executor, lambda: check(content["link"])):
            headings = list(content.keys())
            button = [
                [
                    InlineKeyboardButton(
                        text="Apply", url=content["Apply"]),
                ]
            ]
            markup = InlineKeyboardMarkup(inline_keyboard=button)
            try:
                post = await bot.send_photo(
                    chat_id=CHANNEL,
                    photo=content["Thumbnail"].replace(" ", "%20"),
                    caption=CAPTION.format(
                        title=title,
                        date_key=headings[1],
                        date=content[headings[1]],
                        description_key=headings[2],
                        description=content[headings[2]],
                        deignation_key=headings[3],
                        deignation=content[headings[3]],
                        batch_key=headings[4],
                        batch=content[headings[4]],
                        salary_key=headings[5],
                        salary=content[headings[5]],
                        important_key=headings[6],
                        important=content[headings[6]],
                        location_key=headings[7],
                        location=content[headings[7]],
                        extra_key=headings[8],
                        extra=content[headings[8]],
                    ),
                    reply_markup=markup
                )
                await bot.send_sticker(
                    chat_id=CHANNEL,
                    sticker="CAACAgUAAx0CSVhoDAABFM_aYk01ZlDsdO_9BtdfYyLaKwI0QJ4AAjsAA0NzyRIuGBJU0KTNKyME"
                )
                await loop.run_in_executor(executor, lambda: publish(content["link"], title, str(post.id)))
                info = await bot.copy_message(chat_id=CODING_GROUP, from_chat_id=CHANNEL, message_id=post.id, reply_markup=markup)
                await bot.pin_chat_message(chat_id=CODING_GROUP, message_id=info.id)
                result = await loop.run_in_executor(executor, lambda: fetchIds())
                for users in result:
                    try:
                        await bot.copy_message(chat_id=int(
                            users["key"]), from_chat_id=CHANNEL, message_id=post.id, reply_markup=markup)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)

                await asyncio.sleep(3)
            except:
                pass

save_post = AsyncIOScheduler()
save_post.add_job(save_posts, 'interval', minutes=1)
save_post.start()

upload_post = AsyncIOScheduler()
upload_post.add_job(upload_posts, 'interval', minutes=2)
upload_post.start()
