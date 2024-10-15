import random

from disnake.ext.commands import Cog, command, Bot, Context, has_permissions, bot_has_permissions

__all__ = ()

def setup(bot: Bot):
    bot.add_cog(Ball(bot))

class Ball(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
        self.answers = (
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        )

    @command(name = "8ball", aliases = ("ball", "ask"))
    @has_permissions(send_messages = True)
    @bot_has_permissions(send_messages = True)
    async def ball(self, ctx: Context):
        await ctx.reply(
            random.choice(self.answers),
            mention_author = False
        )
