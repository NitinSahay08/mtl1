import os
import logging
from pyrogram import Client, enums
from pyrogram.errors import AuthError, RPCError
import time

LOG_FILE = 'log.txt'
USER_SESSION_STRING_KEY = 'tringhi'

# Set up logging
logging.basicConfig(
    format="[%(asctime)s] [%(levelname)s] - %(message)s",
    datefmt="%d-%b-%y %I:%M:%S %p",
    level=logging.INFO,
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()]
)

# Set logging level for pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

LOGGER = logging.getLogger(__name__)

def main():
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
                
                no_updates=True
            )
            user.start()
            IS_PREMIUM_USER = user.me.is_premium
            logging.info("Bot started successfully")
        except (AuthError, RPCError) as e:
            logging.error(f"Failed making client from USER_SESSION_STRING: {e}")
            user = ''
    else:
        logging.warning("No session string provided. Cannot create client.")
        exit(1)  # Exit with error code 1 if no session string is provided

    # Keep the bot running
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
