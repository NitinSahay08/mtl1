import os
import logging
from pyrogram import Client, enums
from pyrogram.errors import AuthError, RPCError

class TG_CONFIG:
    api_id = 123456  # Replace with your Telegram API ID
    api_hash = "your_api_hash_here"  # Replace with your Telegram API hash
    session_name = "my_telegram_session"  # Replace with your desired session name
    session_string = ""  # Replace with your Telegram session string (optional)
    log_file = "telegram_bot.log"  # Replace with your desired log file path

# Logging configuration
logging.basicConfig(
    format="[%(asctime)s] [%(levelname)s] - %(message)s",
    datefmt="%d-%b-%y %I:%M:%S %p",
    handlers=[logging.FileHandler(TG_CONFIG.log_file), logging.StreamHandler()],
    level=logging.DEBUG  # Set to DEBUG for development or testing
)

# Telegram bot setup
IS_PREMIUM_USER = False
USER_SESSION_STRING = TG_CONFIG.session_string

if len(USER_SESSION_STRING) != 0:
    logging.info("Creating client from USER_SESSION_STRING")
    try:
        user = Client(
            TG_CONFIG.session_name,
            api_id=TG_CONFIG.api_id,
            api_hash=TG_CONFIG.api_hash,
            session_string=TG_CONFIG.session_string,
            parse_mode=enums.ParseMode.HTML,
            no_updates=True
        ).start()
        IS_PREMIUM_USER = user.me.is_premium
    except (AuthError, RPCError) as e:
        logging.error(f"Failed making client from USER_SESSION_STRING: {e}")
        user = ''
else:
    logging.warning("No session string provided. Cannot create client.")
