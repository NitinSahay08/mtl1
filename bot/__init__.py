
import os
import logging
from bot.config import TG_CONFIG
from pyrogram import Client, enums, filters
from pyrogram.errors import RPCError
from pyrogram.types import User

# Constants
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

def create_client() -> Client:
    try:
        client = Client(
            'user',
            api_id=TG_CONFIG.api_id,
            api_hash=TG_CONFIG.api_hash,
            session_string=TG_CONFIG.stringhi,
            no_updates=True
        )
        logging.info("Client created successfully")
        
        # Get the bot's information
       # user: User = client.get_me()
        #TG_CONFIG.premium = user.is_premium
        
        return client
    except RPCError as e:
        logging.error(f"Failed making client from USER_SESSION_STRING ({TG_CONFIG.stringhi}): {e}")
        return None
    except Exception as err:
        logging.error(f"An error occurred: {err}")
        
        return None

def main() -> Client:
    if TG_CONFIG.stringhi:
        userBot = create_client()
        if userBot:
            logging.info("Bot is running")

            @userBot.on_message(filters.private & filters.command("start"))
            def start_command(client: Client, message):
                logging.info(f"Received /start command from {message.from_user.username}")
                message.reply("Hello! I'm a bot.")

            @userBot.on_message(filters.private & filters.command("help"))
            def help_command(client: Client, message):
                logging.info(f"Received /help command from {message.from_user.username}")
                message.reply("This is a help message.")

            @userBot.on_message(filters.private & filters.text)
            def text_message(client: Client, message):
                logging.info(f"Received message: {message.text}")
                message.reply("You sent: " + message.text)

            userBot.run()
            return userBot
        else:
            logging.error("Bot is not running")
            return None
    else:
        logging.error("USER_SESSION_STRING is empty")
        return None


def send_boot_message(client: Client):

    print("Bot booted with Premium Account\n\n")



log_channel = TG_CONFIG.log_channel
try:
    if Config.stringhi is None:
        raise KeyError
    logging.info("Starting USER Session")
    userBot = Client(
        name="merge-bot-user",
        session_string=Config.USER_SESSION_STRING,
        no_updates=True,
    )

except KeyError:
    userBot = None
    logging.warning("No User Session, Default Bot session will be used")



if __name__ == "__main__":

    try:

        if Config.stringhi is None:

            raise KeyError

        logging.info("Starting USER Session")

        userBot = Client(

            name="Bk-user",

            session_string=Config.stringhi,

            no_updates=True,

        )

    except KeyError:

        userBot = None

        logging.warning("No User Session, Default Bot session will be used")


    if userBot:

        try:

            @userBot.on_message(filters.private & filters.command("start"))

            def start_command(client: Client, message):

                logging.info(f"Received /start command from {message.from_user.username}")

                message.reply("Hello! I'm a bot.")


            @userBot.on_message(filters.private & filters.command("help"))

            def help_command(client: Client, message):

                logging.info(f"Received /help command from {message.from_user.username}")

                message.reply("This is a help message.")


            @userBot.on_message(filters.private & filters.text)

            def text_message(client: Client, message):

                logging.info(f"Received message: {message.text}")

                message.reply("You sent: " + message.text)


            userBot.run()

            send_boot_message(userBot)

        except Exception as err:

            logging.error(f"{err}")

            TG_CONFIG.premium = False

    else:

        logging.error("userBot is None")
