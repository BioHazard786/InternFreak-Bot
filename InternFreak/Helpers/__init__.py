from InternFreak import bot, loop
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import MediaCaptionTooLong
from concurrent.futures import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import json
import asyncio
import requests
from bs4 import BeautifulSoup
from ..Database.Deta import *
executor = ThreadPoolExecutor(10)
