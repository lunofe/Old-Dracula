#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os, discord, asyncio, datetime, dotenv
from discord.ext import commands
from dotenv import load_dotenv
from discord import User
from mcstatus import MinecraftServer

class OnReady(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

#============================================================================================================#

    # Setting the bot's "playing" status
    @commands.Cog.listener()
    async def on_ready(self):
        print(str(datetime.datetime.now()) + " | Initialization completed")

        # Setting Minecraft Server
        server = MinecraftServer.lookup("147.135.9.96:25575")

        while True:
            try:
                status = server.status()
                await self.client.change_presence(activity=discord.Game(name="Online Players: {}".format(status.players.online)))
                await asyncio.sleep(60)
            except Exception as e:
                print(str(datetime.datetime.now()) + " | MCSTATS | Can't reach the Minecraft server, will try again in five minutes.")
                await asyncio.sleep(300)

#============================================================================================================#

def setup(client):
    client.add_cog(OnReady(client))
    print(str(datetime.datetime.now()) + " | Initialized cogs.OnReady")
