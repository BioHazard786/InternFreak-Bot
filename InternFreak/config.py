from os import getenv
from dotenv import load_dotenv
load_dotenv("config.env")


BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
CHANNEL = int(getenv("CHANNEL"))
CODING_GROUP = int(getenv("CODING_GROUP"))
DETA = getenv("DETA")
