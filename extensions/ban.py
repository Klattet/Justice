from disnake import Member
from disnake.ext.commands import Cog, Bot, Context, command, has_permissions, bot_has_permissions, Greedy, FlagConverter

__all__ = ()

def setup(bot: Bot):
    bot.add_cog(Ban(bot))

class Ban(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot

    class BanFlags(FlagConverter):
        member: Member | None
        members: list[Member] | None
        reason: str | None

    # TODO: Create timed bans.

    @command(name = "ban")
    @has_permissions(send_messages = True, ban_members = True)
    @bot_has_permissions(send_messages = True, ban_members = True)
    async def ban(self, ctx: Context, members: Greedy[Member], flags: BanFlags) -> None:
        member_set: set[Member] = set(members)

        if flags.member is not None:
            member_set.add(flags.member)
        if flags.members is not None:
            member_set.update(flags.members)

        if len(member_set) == 0:
            raise ValueError("You need to tell me who you want to ban!") # TODO: Add better error messages.

        # TODO: FINISH THIS.
