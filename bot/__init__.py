import os
import logging
from pyrogram import Client, filters, enums
from pyrogram.errors import RPCError

LOG_FILE = 'log.txt'

# Set up logging
logging.basicConfig(
    format="[%(asctime)s] [%(levelname)s] - %(message)s",
    datefmt="%d-%b-%y %I:%M:%S %p",
    level=logging.INFO,
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()]
)

# Set logging level for pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import time

from pyrogram.types import Message, User
from bot.config import ScaryGhost
from bot.config import TG_CONFIG as Config

botStartTime = time.time()

class BhootbnglaBot(Client):

    def start(self):
        super().start()
        try:
            self.send_message(chat_id=int(ScaryGhost.owner), text="<b>Bot Started!</b>")
        except RPCError as err:
            logging.error(f"Boot alert failed! Please start bot in PM: {err}")
        return logging.info("Bot Started!")

    def stop(self):
        super().stop()
        return logging.info("Bot Stopped!")

tamtaplay = BhootbnglaBot(
    name="Tmta-play",
    api_id=Config.api_id,
    api_hash=Config.api_hash,
    bot_token=Config.bot_token,
    workers=300,
    app_version="Bhootbangla",
)

if not os.path.exists("downloads"):
    os.makedirs("downloads")

LOGCHANNEL = ScaryGhost.log_channel

try:
    if Config.stringhi is None:
        raise KeyError
    logging.info("Starting USER Session")
    userBot = Client(
        name="tamtabot-user",
        session_string=Config.stringhi,
        no_updates=True,
    )

except KeyError:
    userBot = None
    logging.warning("No User Session, Default Bot session will be used")

def main():
    """
    Main entry point for the bot.
    """
    try:
        if userBot:
            userBot.start()
            userBot.send_message(
                chat_id=int(LOGCHANNEL),
                text="Bot booted with Premium",
                disable_web_page_preview=True,
            )
            user = userBot.get_me()
            Config.premium = user.is_premium
        else:
            Config.premium = False
    except Exception as err:
        logging.error(f"Error in main function: {err}")
        Config.premium = False
    finally:
        if userBot:
            userBot.stop()

    tamtaplay.start()
    try:
        # Define bot commands
        @tamtaplay.on_message(filters.command("start"))
        def start_handler(client, message):
            message.reply_text("Welcome to Bhootbngla Bot!")

        @tamtaplay.on_message(filters.command("help"))
        def help_handler(client, message):
            message.reply_text("This is a help message!")



        tamtaplay.run()
    except Exception as err:
        logging.error(f"Error in bot logic: {err}")
    finally:
        tamtaplay.stop()

if __name__ == "__main__":
    main()
