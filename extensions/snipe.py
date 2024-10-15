
from disnake import Message, User, Member, Embed
from disnake.ext.commands import Cog, Bot, command, Context, has_permissions, bot_has_permissions, guild_only

def setup(bot: Bot):
    bot.add_cog(Snipe(bot))

class Snipe(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
        self.cache: dict[int, dict[int, Message]] = {} # guild id, user id, message

    @Cog.listener("on_message_delete")
    async def cache_deleted_message(self, message: Message) -> None:
        if not message.guild: return

        if message.guild.id not in self.cache.keys():
            self.cache[message.guild.id] = {}

        self.cache[message.guild.id][message.author.id] = message

    @command(name = "snipe")
    @has_permissions(send_messages = True)
    @bot_has_permissions(send_messages = True, embed_links = True)
    @guild_only()
    async def snipe(self, ctx: Context, user: User | Member) -> None:
        #await ctx.reply("Please also let me know which user to snipe when using this command!")

        if ctx.guild.id not in self.cache.keys() or user.id not in self.cache[ctx.guild.id].keys():
            await ctx.reply("No messages to snipe.", mention_author = False)

        embed: Embed = Embed(description = self.cache[ctx.guild.id][user.id].content)
        embed.set_author(name = self.cache[ctx.guild.id][user.id].author.display_name, icon_url = self.cache[ctx.guild.id][user.id].author.display_avatar)

        await ctx.reply(
            embed = embed,
            files = [await attachment.to_file(use_cached = True) for attachment in self.cache[ctx.guild.id][user.id].attachments],
            mention_author = False
        )

