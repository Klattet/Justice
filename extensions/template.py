from disnake.ext.commands import Cog, Bot, Context, command, has_permissions, bot_has_permissions

__all__ = ()

def setup(bot: Bot):
    bot.add_cog(Template(bot))

class Template(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot

    @command(name = "template")
    @has_permissions(send_messages = True)
    @bot_has_permissions(send_messages = True, embed_links = True)
    async def template(self, ctx: Context) -> None:
        ...
