from disnake import Embed, User
from disnake.ext.commands import Cog, Bot, Context, command, Greedy, has_permissions, bot_has_permissions

__all__ = ()

def setup(bot: Bot):
    bot.add_cog(Avatar(bot))

class Avatar(Cog):
    def __init__(self, bot: Bot):
        self.bot: Bot = bot

    @command(name = "avatar", aliases = ("icon", "pfp"))
    @has_permissions(send_messages = True)
    @bot_has_permissions(send_messages = True, embed_links = True)
    async def avatar(self, ctx: Context, users: Greedy[User]) -> None:
        embeds: list[Embed] = []

        if len(users) == 0:
            users.append(ctx.author)

        for user in users:
            embeds.append(Embed(url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ").set_image(url = user.display_avatar.url))

        embeds[0].set_author(name = ",   ".join(user.name for user in users))

        await ctx.reply(
            embeds = embeds,
            mention_author = False
        )

    @command(name = "default_avatar", aliases = ("defaultavatar", "default_icon", "defaulticon", "default_pfp", "defaultpfp"))
    @has_permissions(send_messages = True)
    @bot_has_permissions(send_messages = True, embed_links = True)
    async def default_avatar(self, ctx: Context, users: Greedy[User]) -> None:
        embeds: list[Embed] = []

        if len(users) == 0:
            users.append(ctx.author)

        for user in users:
            embeds.append(Embed(url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ").set_image(url = user.default_avatar.url))

        embeds[0].set_author(name = ",   ".join(user.name for user in users))

        await ctx.reply(
            embeds = embeds,
            mention_author = False
        )