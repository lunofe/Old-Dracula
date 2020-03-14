#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os, discord, asyncio, datetime
import draculogger as log
from discord.ext import commands
from discord import User

class Tools(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

#============================================================================================================#

    # 'ping' command
    @commands.command()
    async def ping(self, ctx):
        message = ctx.message
        channel = message.channel
        author = message.author
        await message.delete()
        ping = await channel.send("{} Pong! :ping_pong: ".format(author.mention) + str(os.uname()))
        await asyncio.sleep(10)
        await ping.delete()

#============================================================================================================#

    @commands.command()
    async def cracked(self, ctx):
        message = ctx.message
        channel = message.channel
        embed = discord.Embed(title="""This error appears when you use a "cracked" client, which is giving you access to Minecraft without paying.""", description="Software piracy is illegal. Although there is an option for servers to accept cracked clients, we will not do that, because we are strictly against software piracy. Furthermore, it involves multiple problems, for example the simple circumvention of bans.")
        embed.set_author(name="Failed to verify username?")
        await message.delete()
        await channel.send(embed=embed)

#============================================================================================================#

def setup(client):
    client.add_cog(Tools(client))
    log.this("Initialized cogs.Tools")
