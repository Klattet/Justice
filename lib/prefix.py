
from disnake import Message
from disnake.ext.commands import Bot, when_mentioned_or

__all__ = "get_prefix",

async def get_prefix(bot: Bot, message: Message):
    return when_mentioned_or("j.")(bot, message) # TODO: Create functionality to have server specific prefixes and store default prefix in config file.