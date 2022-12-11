from InternFreak import bot, loop
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.errors import FloodWait
from ..Database.Deta import *
from ..Helpers import Utils
from ..config import botStartTime
from concurrent.futures import ThreadPoolExecutor
import psutil
import shutil
from time import time
executor = ThreadPoolExecutor(1)
