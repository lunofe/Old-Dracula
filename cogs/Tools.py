#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import util, os, discord, asyncio
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
        embed = discord.Embed(title="""First try to restart both Minecraft and your Minecraft launcher. If this error still appears, you are most likely using a "cracked" client, which is giving you access to Minecraft without paying.""", description="Software piracy is illegal. Although there is an option for servers to accept cracked clients, we will not do that, because we are strictly against software piracy. Furthermore, it involves multiple problems, for example the simple circumvention of bans.")
        embed.set_author(name="Failed to verify username?")
        await message.delete()
        await channel.send(embed=embed)

#============================================================================================================#

    @commands.command()
    async def delete(self, ctx, *args):
        if(util.check_permission(ctx.message.author.id)):
            author = ctx.message.author.name
            await ctx.message.delete()
            if(len(args) != 2):
                botresponse = await ctx.send(":warning: Wrong syntax. Define a range using `.delete <latest message> <oldest message>`")
                await asyncio.sleep(3)
                await botresponse.delete()
                return
            counter = 0
            new = await ctx.channel.fetch_message(int(args[0]))
            old = await ctx.channel.fetch_message(int(args[1]))

            async with ctx.channel.typing():
                bucket = await ctx.channel.history(limit=500, before=new.created_at, after=old.created_at, oldest_first=False).flatten()
                await new.delete()
                for msg in bucket:
                    await msg.delete()
                    counter = counter + 1
                await old.delete()
            botresponse = await ctx.send("{} messages have been deleted by {}.".format(str(counter + 2), author))
            util.log("TOOLS", "{} messages have been deleted by {}.".format(str(counter + 2), author))
            await asyncio.sleep(10)
            await botresponse.delete()
        else:
            await util.no_permission(ctx, 10)

#============================================================================================================#

def setup(client):
    client.add_cog(Tools(client))
    util.log("Initialized cogs.Tools")
