from asyncio import CancelledError

from disnake import Activity, Status, ActivityType
from disnake.ext.commands import Cog, Bot, Context

__all__ = ()

def setup(bot: Bot):
    bot.add_cog(Presence(bot))

class Presence(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot

        self.idle = Activity(
            type = ActivityType.competing,
            name = "pancake flipping contest."
        )
        self.online = Activity(
            type = ActivityType.listening,
            name = "commands."
        )

    @Cog.listener("on_ready")
    async def start(self) -> None:
        await self.bot.change_presence(status = Status.idle, activity = self.idle)

    @Cog.listener("on_command")
    async def awake(self, ctx: Context) -> None:
        if ctx.guild is None: return

        if ctx.me.status != Status.online:
            await self.bot.change_presence(status = Status.online, activity = self.online)
        try:
            await self.bot.wait_for(event = "command", check = lambda c: c.guild is not None, timeout = 300.0)
        except TimeoutError:
            await self.bot.change_presence(status = Status.idle, activity = self.idle)
        except CancelledError:
            pass
