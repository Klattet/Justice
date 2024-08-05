from disnake import Event, ApplicationCommandInteraction
from disnake.ext.commands import Cog, Bot, Context, CommandError

from lib import logger

__all__ = ()

def setup(bot: Bot):
    bot.add_cog(Events(bot))

class Events(Cog):
    def __init__(self, bot: Bot):
        self.bot: Bot = bot

    @Cog.listener(Event.ready)
    async def log_ready(self) -> None:
        logger.info("Ready!")

    @Cog.listener(Event.error)
    async def error(self, event: str, *args, **kwargs) -> None:
        print(event)

    @Cog.listener(Event.command_error)
    async def command_error(self, ctx: Context, error: CommandError) -> None:
        await ctx.reply(f"Oh no! Looks like something went wrong: *{error.__class__.__name__}*", mention_author = False)

    @Cog.listener(Event.user_command_error)
    async def command_error(self, inter: ApplicationCommandInteraction, error: CommandError) -> None:
        await inter.send(f"Oh no! Looks like something went wrong: *{error.__class__.__name__}*")

    @Cog.listener(Event.slash_command_error)
    async def command_error(self, inter: ApplicationCommandInteraction, error: CommandError) -> None:
        await inter.send(f"Oh no! Looks like something went wrong: *{error.__class__.__name__}*")

    @Cog.listener(Event.message_command_error)
    async def command_error(self, inter: ApplicationCommandInteraction, error: CommandError) -> None:
        await inter.send(f"Oh no! Looks like something went wrong: *{error.__class__.__name__}*")