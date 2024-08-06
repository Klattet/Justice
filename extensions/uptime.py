from datetime import datetime, UTC, timedelta

from disnake import Embed
from disnake.ext.commands import Cog, Bot, Context, command, has_permissions, bot_has_permissions

__all__ = ()

def setup(bot: Bot):
    bot.add_cog(Uptime(bot))

class Uptime(Cog):
    def __init__(self, bot: Bot):
        self.bot: Bot = bot
        self.start_time: datetime = datetime.now(UTC)

    # TODO: Create a more humanreadable timedelta and make start time independent of extension reloading.

    @command(name = "uptime", aliases = ("up",))
    @has_permissions(send_messages = True)
    @bot_has_permissions(send_messages = True, embed_links = True)
    async def uptime(self, ctx: Context) -> None:
        time_delta: timedelta = datetime.now(UTC) - self.start_time
        await ctx.reply(embed = Embed(description = str(time_delta), timestamp = self.start_time), mention_author = False)