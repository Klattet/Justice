from typing import Union

from disnake import Embed, User, Member
from disnake.ext.commands import command, bot_has_permissions, has_permissions, Context, Cog, Bot, Greedy

def setup(bot) -> None:
    bot.add_cog(Info(bot))

class Info(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot

    @staticmethod
    def create_user_embed(user: User) -> Embed:
        embed: Embed = Embed(
            description = f"**User ID:** {user.id}\n"
                          f"**Account created at:** {user.created_at.strftime('%d/%m/%Y, %H:%M')}"
        )
        embed.set_thumbnail(url = user.display_avatar.url)
        return embed

    @staticmethod
    def create_member_embed(member: Member) -> Embed:
        embed: Embed = Embed(
            description = f"**User ID:** {member.id}\n"
                          f"**Account created at:** {member.created_at.strftime('%d/%m/%Y, %H:%M')}\n"
                          f"**Joined server at:** {member.joined_at.strftime('%d/%m/%Y, %H:%M')}"
        )
        if member.premium_since is not None:
            embed.description += f"\n**Nitro since:** {member.premium_since.strftime('%d/%m/%Y, %H:%M')}"
        embed.set_thumbnail(url = member.display_avatar.url)
        return embed

    @command(name = "info", aliases = ("information",))
    @has_permissions(send_messages = True)
    @bot_has_permissions(send_messages = True, embed_links = True)
    async def info(self, ctx: Context, users: Greedy[Union[User, Member]]) -> None:
        if len(users) == 0:
            users.append(ctx.author)
        elif ctx.guild:
            for i, user in enumerate(users):
                if member := ctx.guild.get_member(user.id):
                    users[i] = member

        embeds: list[Embed] = [
            self.create_member_embed(user)
            if isinstance(user, Member)
            else self.create_user_embed(user)
            for user in users
        ]

        await ctx.reply(
            embeds = embeds,
            mention_author = False
        )
