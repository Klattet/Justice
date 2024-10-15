from typing import Union

from disnake import Embed, User, Member, Guild
from disnake.ext.commands import Cog, Bot, Context, command, Greedy, has_permissions, bot_has_permissions

__all__ = ()

def setup(bot: Bot):
    bot.add_cog(Avatar(bot))

class Avatar(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot

    @command(name = "avatar", aliases = ("icon", "pfp"))
    @has_permissions(send_messages = True)
    @bot_has_permissions(send_messages = True, embed_links = True)
    async def avatar(self, ctx: Context, users: Greedy[Union[User, Member]]) -> None:
        if len(users) == 0:
            users.append(ctx.author)

        embeds: list[Embed] = [Embed(url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ").set_image(url = user.display_avatar.url) for user in users]

        embeds[0].set_author(name = ",   ".join(user.name for user in users))

        await ctx.reply(
            embeds = embeds,
            mention_author = False
        )

    @command(name = "default_avatar", aliases = ("defaultavatar", "default_icon", "defaulticon", "default_pfp", "defaultpfp"))
    @has_permissions(send_messages = True)
    @bot_has_permissions(send_messages = True, embed_links = True)
    async def default_avatar(self, ctx: Context, users: Greedy[Union[User, Member]]) -> None:
        if len(users) == 0:
            users.append(ctx.author)

        embeds: list[Embed] = [Embed(url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ").set_image(url = user.default_avatar.url) for user in users]

        embeds[0].set_author(name = ",   ".join(user.name for user in users))

        await ctx.reply(
            embeds = embeds,
            mention_author = False
        )

    @command(name = "guild_avatar", aliases = ("guildavatar", "guild_icon", "guildicon", "guild_pfp", "guildpfp", "server_avatar", "serveravatar", "server_icon", "servericon", "server_pfp", "serverpfp"))
    @has_permissions(send_messages = True)
    @bot_has_permissions(send_messages = True, embed_links = True)
    async def guild_avatar(self, ctx: Context, guilds: Greedy[Guild]) -> None:
        if len(guilds) == 0:
            guilds.append(ctx.guild)

        embeds: list[Embed] = [Embed(url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ").set_image(url = guild.icon.url) for guild in guilds]

        embeds[0].set_author(name = ",   ".join(guild.name for guild in guilds))

        await ctx.reply(
            embeds = embeds,
            mention_author = False
        )
