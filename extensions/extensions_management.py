import os, sys

from disnake import Message
from disnake.ext.commands import Cog, Bot, Context, group, ExtensionNotFound, ExtensionNotLoaded, ExtensionAlreadyLoaded, NoEntryPointError, ExtensionFailed, is_owner

__all__ = ()

def setup(bot: Bot) -> None:
    bot.add_cog(ExtensionManagement(bot))

class ExtensionManagement(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot

    async def load_extension(self, extension_name: str, message: Message) -> None:
        message_content: str = message.content

        print(f"Loading extension: {extension_name}")
        await message.edit(f"{message_content}\nLoading: {extension_name}")

        try:
            self.bot.load_extension(f"extensions.{extension_name}")
            print(f"Loaded extension: {extension_name}")
            await message.edit(f"{message_content}\nLoaded: {extension_name}")
        except ExtensionAlreadyLoaded:
            print(f"Failed to load extension. Extension already loaded: {extension_name}")
            await message.edit(f"{message_content}\nAlready loaded: {extension_name}")
        except ExtensionNotFound:
            print(f"Failed to load extension. Name not found: {extension_name}")
            await message.edit(f"{message_content}\nNo such extension: {extension_name}")
        except (NoEntryPointError, ExtensionFailed) as exception:
            print(f"Failed to load extension. Code failed to execute: {extension_name}")
            print(exception, file = sys.stderr, flush = True)
            await message.edit(f"{message_content}\nCode error: {extension_name}")

    @group(name = "load", invoke_without_command = True)
    @is_owner()
    async def load(self, ctx: Context, *extension_names: str) -> None:
        message: Message = await ctx.reply(f"**Loading {len(extension_names)} extensions:**\n")

        for name in extension_names:
            await self.load_extension(name, message)

    @load.command(name = "all")
    @is_owner()
    async def load_all(self, ctx: Context) -> None:
        message: Message = await ctx.reply(f"**Loading all extensions:**\n")

        for _, _, files in os.walk(os.path.join(os.getcwd(), "extensions")):
            for file in files:
                if file.endswith(".py"):
                    await self.load_extension(file[:-3], message)

    async def reload_extension(self, extension_name: str, message: Message) -> None:
        message_content: str = message.content

        print(f"Reloading extension: {extension_name}")
        await message.edit(f"{message_content}\nReloading: {extension_name}")

        try:
            self.bot.reload_extension(f"extensions.{extension_name}")
            print(f"Reloaded extension: {extension_name}")
            await message.edit(f"{message_content}\nReloaded: {extension_name}")
        except ExtensionNotLoaded:
            print(f"Failed to reload extension. Extension not loaded: {extension_name}")
            await message.edit(f"{message_content}\nNot loaded: {extension_name}")
        except ExtensionNotFound:
            print(f"Failed to reload extension. Name not found: {extension_name}")
            await message.edit(f"{message_content}\nNo such extension: {extension_name}")
        except (NoEntryPointError, ExtensionFailed) as exception:
            print(f"Failed to reload extension. Code failed to execute: {extension_name}")
            print(exception, file = sys.stderr, flush = True)
            await message.edit(f"{message_content}\nCode error: {extension_name}")

    @group(name = "reload", invoke_without_command = True)
    @is_owner()
    async def reload(self, ctx: Context, *extension_names: str) -> None:
        message: Message = await ctx.reply(f"**Reloading {len(extension_names)} extensions:**\n")

        for name in extension_names:
            await self.reload_extension(name, message)

    @reload.command(name = "all")
    @is_owner()
    async def reload_all(self, ctx: Context) -> None:
        message: Message = await ctx.reply(f"**Reloading all extensions:**\n")

        for _, _, files in os.walk(os.path.join(os.getcwd(), "extensions")):
            for file in files:
                if file.endswith(".py"):
                    await self.reload_extension(file[:-3], message)

    async def unload_extension(self, extension_name: str, message: Message) -> None:
        message_content: str = message.content

        print(f"Unloading extension: {extension_name}")
        await message.edit(f"{message_content}\nUnloading: {extension_name}")

        try:
            self.bot.unload_extension(f"extensions.{extension_name}")
            print(f"Unloaded extension: {extension_name}")
            await message.edit(f"{message_content}\nUnloaded: {extension_name}")
        except ExtensionNotLoaded:
            print(f"Failed to unload extension. Extension not loaded: {extension_name}")
            await message.edit(f"{message_content}\nNot loaded: {extension_name}")
        except ExtensionNotFound:
            print(f"Failed to unload extension. Name not found: {extension_name}")
            await message.edit(f"{message_content}\nNo such extension: {extension_name}")
        except (NoEntryPointError, ExtensionFailed) as exception:
            print(f"Failed to unload extension. Code failed to execute: {extension_name}")
            print(exception, file = sys.stderr, flush = True)
            await message.edit(f"{message_content}\nCode error: {extension_name}")

    @group(name = "unload", invoke_without_command = True)
    @is_owner()
    async def unload(self, ctx: Context, *extension_names: str) -> None:
        message: Message = await ctx.reply(f"**Unloading {len(extension_names)} extensions:**\n")

        for name in extension_names:
            await self.unload_extension(name, message)

    @unload.command(name = "all")
    @is_owner()
    async def unload_all(self, ctx: Context) -> None:
        message: Message = await ctx.reply(f"**Unloading all extensions:**\n")

        for _, _, files in os.walk(os.path.join(os.getcwd(), "extensions")):
            for file in files:
                if file.endswith(".py"):
                    await self.unload_extension(file[:-3], message)