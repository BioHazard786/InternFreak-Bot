import asyncio
from pyrogram import Client, filters
import glob
from os.path import dirname, basename, isfile, join
from importlib import import_module

__all__ = ['bot', 'loop']

loop = asyncio.get_event_loop()

bot = Client(
    "InternFreak",
    api_id=14313036,
    api_hash="a510f6536294df0dfa5f8f18b797b11f",
    bot_token="5481966629:AAEvGusEJDr9qyyLLlxfeXyFH6g0GFhA_sY"
)

files = glob.glob(join(join(dirname(__file__), 'Plugins'), '*py'))
plugins = [basename(f)[:-3] for f in files if isfile(f)
           and not f.endswith('__init__.py')]

files = glob.glob(join(join(dirname(__file__), 'Helpers'), '*py'))
feeds = [basename(f)[:-3] for f in files if isfile(f)
         and not f.endswith('__init__.py')]

for plug in plugins:
    import_module('InternFreak.Plugins.'+plug)

for feed in feeds:
    import_module('InternFreak.Helpers.'+feed)
