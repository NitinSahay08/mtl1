from bot.__init__ import create_client
from bot.config import TG_CONFIG
import pyrogram

import logging
logging.basicConfig(
    format="[%(asctime)s] [%(levelname)s] - %(message)s",
    datefmt="%d-%b-%y %I:%M:%S %p",
    level=logging.INFO,
    handlers=[logging.FileHandler(log.txt), logging.StreamHandler()]
)

# Set logging level for pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

LOGGER = logging.getLogger(__name__)
from bot import create_client

client = create_client(TG_CONFIG.stringhi)
if client:
    IS_PREMIUM_USER = client.me.is_premium
    logging.info("Bot started successfully")
    # Use the client object here
    print("Client object:", client)
else:
    logging.error("Failed to create client")
