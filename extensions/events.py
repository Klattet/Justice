from disnake.ext.commands import Cog, Bot

from lib import logger

__all__ = ()

def setup(bot: Bot):
    bot.add_cog(Events(bot))

class Events(Cog):
    def __init__(self, bot: Bot):
        self.bot: Bot = bot

    @Cog.listener("on_ready")
    async def log_ready(self) -> None:
        logger.info("Ready!")