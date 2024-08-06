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


    # TODO: Handle exception messages and logging better.

    @Cog.listener(Event.error)
    async def error(self, event: str, *args, **kwargs) -> None:
        logger.exception(f"Generic error {event}.")

    @Cog.listener(Event.command_error)
    async def command_error(self, ctx: Context, error: CommandError) -> None:
        await ctx.reply(f"Oh no! Looks like something went wrong: *{error.__class__.__name__}*", mention_author = False)
        logger.exception("Command exception occurred.", exc_info = error)

    @Cog.listener(Event.user_command_error)
    async def user_command_error(self, inter: ApplicationCommandInteraction, error: CommandError) -> None:
        await inter.send(f"Oh no! Looks like something went wrong: *{error.__class__.__name__}*")
        logger.exception("User command exception occurred.", exc_info = error)

    @Cog.listener(Event.slash_command_error)
    async def slash_command_error(self, inter: ApplicationCommandInteraction, error: CommandError) -> None:
        await inter.send(f"Oh no! Looks like something went wrong: *{error.__class__.__name__}*")
        logger.exception("Slash command exception occurred.", exc_info = error)

    @Cog.listener(Event.message_command_error)
    async def message_command_error(self, inter: ApplicationCommandInteraction, error: CommandError) -> None:
        await inter.send(f"Oh no! Looks like something went wrong: *{error.__class__.__name__}*")
        logger.exception("Message command exception occurred.", exc_info = error)