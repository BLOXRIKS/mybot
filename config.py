import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'your_token_here')
DATABASE_FILE = 'clicker_bot.db'
CLICK_VALUE = 1
BASE_BOOST_COST = 10
BASE_AUTOCLICK_COST = 100
AUTOCLICK_AMOUNT = 1
DAILY_REWARD = 100
BOOST_MULTIPLIERS = {1: 1.5, 2: 2.0, 3: 3.0, 4: 5.0, 5: 10.0}
AUTOCLICK_LEVELS = {1: 1, 2: 5, 3: 10, 4: 20, 5: 50}