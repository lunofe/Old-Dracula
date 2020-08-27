#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import utils, random, discord, asyncio
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
        try:
            server = MinecraftServer.lookup("147.135.9.96:25575")
            status = server.status()
            query = server.query()
            playerlist = sorted(query.players.names)
            if(self.last_query != playerlist):
                if(status.players.online != 0):
                    await self.client.change_presence(activity=discord.Game(name="with {} players 🎮".format(status.players.online)))
                    await self.serverplayers.send("**{} players: ** ``{}``".format(status.players.online, "``, ``".join(playerlist)))
                else:
                    await self.client.change_presence(activity=discord.Game(name="vampirism.maxanier.de"))
                    await self.serverplayers.send("**0 players **" + self.sadcat[random.randint(0, 5)])
                self.last_query = playerlist
        except Exception as e:
            await self.serverplayers.send(str(e))

#============================================================================================================#

    @loop.before_loop
    async def before_loop(self):
        utils.log("MC-STATS", "Wating until ready...")
        await self.client.wait_until_ready()
        self.serverplayers = self.client.get_channel(676209439531073541)
        self.sadcat = ["<:sadcat1:676391344293281802>", "<:sadcat2:676391344582688768>", "<:sadcat3:676391345320886272>", "<:sadcat4:676391344217784331>", "<:sadcat5:676391344154869770>", "<:sadcat6:676391345878859776>"]
        self.last_query = None

#============================================================================================================#

def setup(client):
    client.add_cog(MinecraftQuery(client))
    utils.log("Initialized MinecraftQuery")
