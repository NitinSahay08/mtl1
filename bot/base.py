from bot.__init__ import create_client
from bot.config import TG_CONFIG

from bot import create_client

client = create_client(TG_CONFIG.stringhi)
if client:
    IS_PREMIUM_USER = client.me.is_premium
    logging.info("Bot started successfully")
    # Use the client object here
    print("Client object:", client)
else:
    logging.error("Failed to create client")
