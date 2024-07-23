from bot.__init__ import create_client
from bot.config import TG_CONFIG

client = create_client(TG_CONFIG.stringhi)
if client:
    # Use the client object here
    pass
else:
    logging.error("Failed to create client")
