import os, sys

from disnake import Message
from disnake.ext.commands import Cog, Bot, Context, group, ExtensionNotFound, ExtensionNotLoaded, ExtensionAlreadyLoaded, NoEntryPointError, ExtensionFailed, is_owner

from lib import logger

__all__ = ()

def setup(bot: Bot) -> None:
    bot.add_cog(ExtensionManagement(bot))

class ExtensionManagement(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot

    async def load_extension(self, extension_name: str, message: Message) -> Message:
        message_content: str = message.content

        logger.debug(f"Loading extension: {extension_name}")
        await message.edit(f"{message_content}\nLoading: {extension_name}")

        try:
            self.bot.load_extension(f"extensions.{extension_name}")
            logger.debug(f"Loaded extension: {extension_name}")
            return await message.edit(f"{message_content}\nLoaded: {extension_name}")
        except ExtensionAlreadyLoaded:
            logger.error(f"Failed to load extension. Extension already loaded: {extension_name}")
            return await message.edit(f"{message_content}\nAlready loaded: {extension_name}")
        except ExtensionNotFound:
            logger.error(f"Failed to load extension. Name not found: {extension_name}")
            return await message.edit(f"{message_content}\nNo such extension: {extension_name}")
        except (NoEntryPointError, ExtensionFailed) as exception:
            logger.error(f"Failed to load extension. Code failed to execute: {extension_name}")
            logger.error(exception, file = sys.stderr, flush = True)
            return await message.edit(f"{message_content}\nCode error: {extension_name}")

    @group(name = "load", invoke_without_command = True)
    @is_owner()
    async def load(self, ctx: Context, *extension_names: str) -> None:
        message: Message = await ctx.reply(f"**Loading {len(extension_names)} extensions:**\n")

        for name in extension_names:
            message = await self.load_extension(name, message)

    @load.command(name = "all")
    @is_owner()
    async def load_all(self, ctx: Context) -> None:
        message: Message = await ctx.reply(f"**Loading all extensions:**\n")

        for _, _, files in os.walk(os.path.join(os.getcwd(), "extensions")):
            for file in files:
                if file.endswith(".py"):
                    message = await self.load_extension(file[:-3], message)

    async def reload_extension(self, extension_name: str, message: Message) -> Message:
        message_content: str = message.content

        logger.debug(f"Reloading extension: {extension_name}")
        await message.edit(f"{message_content}\nReloading: {extension_name}")

        try:
            self.bot.reload_extension(f"extensions.{extension_name}")
            logger.debug(f"Reloaded extension: {extension_name}")
            return await message.edit(f"{message_content}\nReloaded: {extension_name}")
        except ExtensionNotLoaded:
            logger.error(f"Failed to reload extension. Extension not loaded: {extension_name}")
            return await message.edit(f"{message_content}\nNot loaded: {extension_name}")
        except ExtensionNotFound:
            logger.error(f"Failed to reload extension. Name not found: {extension_name}")
            return await message.edit(f"{message_content}\nNo such extension: {extension_name}")
        except (NoEntryPointError, ExtensionFailed) as exception:
            logger.error(f"Failed to reload extension. Code failed to execute: {extension_name}")
            logger.error(exception, file = sys.stderr, flush = True)
            return await message.edit(f"{message_content}\nCode error: {extension_name}")

    @group(name = "reload", invoke_without_command = True)
    @is_owner()
    async def reload(self, ctx: Context, *extension_names: str) -> None:
        message: Message = await ctx.reply(f"**Reloading {len(extension_names)} extensions:**\n")

        for name in extension_names:
            message = await self.reload_extension(name, message)

    @reload.command(name = "all")
    @is_owner()
    async def reload_all(self, ctx: Context) -> None:
        message: Message = await ctx.reply(f"**Reloading all extensions:**\n")

        for _, _, files in os.walk(os.path.join(os.getcwd(), "extensions")):
            for file in files:
                if file.endswith(".py"):
                    message = await self.reload_extension(file[:-3], message)

    async def unload_extension(self, extension_name: str, message: Message) -> Message:
        message_content: str = message.content

        logger.debug(f"Unloading extension: {extension_name}")
        await message.edit(f"{message_content}\nUnloading: {extension_name}")

        try:
            self.bot.unload_extension(f"extensions.{extension_name}")
            logger.debug(f"Unloaded extension: {extension_name}")
            return await message.edit(f"{message_content}\nUnloaded: {extension_name}")
        except ExtensionNotLoaded:
            logger.error(f"Failed to unload extension. Extension not loaded: {extension_name}")
            return await message.edit(f"{message_content}\nNot loaded: {extension_name}")
        except ExtensionNotFound:
            logger.error(f"Failed to unload extension. Name not found: {extension_name}")
            return await message.edit(f"{message_content}\nNo such extension: {extension_name}")
        except (NoEntryPointError, ExtensionFailed) as exception:
            logger.error(f"Failed to unload extension. Code failed to execute: {extension_name}")
            logger.error(exception, file = sys.stderr, flush = True)
            return await message.edit(f"{message_content}\nCode error: {extension_name}")

    @group(name = "unload", invoke_without_command = True)
    @is_owner()
    async def unload(self, ctx: Context, *extension_names: str) -> None:
        message: Message = await ctx.reply(f"**Unloading {len(extension_names)} extensions:**\n")

        for name in extension_names:
            message = await self.unload_extension(name, message)

    @unload.command(name = "all")
    @is_owner()
    async def unload_all(self, ctx: Context) -> None:
        message: Message = await ctx.reply(f"**Unloading all extensions:**\n")

        for _, _, files in os.walk(os.path.join(os.getcwd(), "extensions")):
            for file in files:
                if file.endswith(".py"):
                    message = await self.unload_extension(file[:-3], message)