#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import utils, discord, asyncio
from discord.ext import commands, tasks
from mcstatus import MinecraftServer

class MinecraftQuery(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.loop.start()

#============================================================================================================#

    def cog_unload(self):
        self.loop.cancel()

#============================================================================================================#

    @tasks.loop(minutes=1.0)
    async def loop(self):
        go = False

        try:
            server = MinecraftServer.lookup("vampirism.co")
            status = server.status()
            go = True
        except Exception as e:
            await self.serverplayers.send(str(e))

        if go == True:
            go = False

            try:
                usersConnected = [ user['name'] for user in status.raw['players']['sample'] ]
                go = True
            except Exception as e:
                if self.last_query != "null":
                    await self.client.change_presence(activity=discord.Game(name="vampirism.co"))
                    await self.serverplayers.send("**0 players **")
                    self.last_query = "null"

            if go == True:
                if usersConnected != self.last_query:
                    await self.client.change_presence(activity=discord.Game(name="with {} players 🎮".format(status.players.online)))
                    await self.serverplayers.send("**{} players: ** ``{}``".format(status.players.online, "``, ``".join(usersConnected)))
                    self.last_query = usersConnected

#============================================================================================================#

    @loop.before_loop
    async def before_loop(self):
        utils.log("MC-STATS", "Wating until ready...")
        await self.client.wait_until_ready()
        self.serverplayers = self.client.get_channel(676209439531073541)
        self.last_query = None

#============================================================================================================#

def setup(client):
    client.add_cog(MinecraftQuery(client))
    utils.log("Initialized MinecraftQuery")
