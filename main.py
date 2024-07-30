import yaml

from disnake import Intents
from disnake.ext.commands import Bot

from lib import get_prefix

def bot_task() -> None:

    bot: Bot = Bot(
        command_prefix = get_prefix,

        # TODO: Have bot settings in a config file.
        case_insensitive = True,
        strip_after_prefix = True,

        intents = Intents.all() # TODO: Decide on a more limited intents option.
    )

    bot.load_extensions("extensions")

    with open("config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)

    bot.run(config["discord_api_token"])

# Sneaky color code 0xC94B58

if __name__ == "__main__":
    bot_task()
