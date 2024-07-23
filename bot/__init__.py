import os
import logging
from pyrogram import Client, enums

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

def create_client(session_string: str) -> Client:
    try:
        client = Client(
            TG_CONFIG.session_name,
            api_id=TG_CONFIG.api_id,
            api_hash=TG_CONFIG.api_hash,
            session_string=session_string,
            no_updates=True
        )
        client.start()
        return client
    except Exception as e:
        logging.error(f"Failed making client from USER_SESSION_STRING: {e}")
        return None
