from disnake.ext.commands import Cog, Bot, Context, command

__all__ = ()

def setup(bot: Bot):
    bot.add_cog(Template(bot))

class Template(Cog):
    def __init__(self, bot: Bot):
        self.bot: Bot = bot

