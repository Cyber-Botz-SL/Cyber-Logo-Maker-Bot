# Sorry I not Have Logo api I don't no How to create logo Api. I give TechZ logo api Ok

from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# API By TechZBots || https://t.me/TechZBots
LOGO_API_URL1 = "https://techzbotsapi.herokuapp.com/logo?text="

LOGO_API_URL2 = "https://techzbotsapi.herokuapp.com/logo?square=true&text="
