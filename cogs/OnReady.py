#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import util, random, discord, asyncio, time
from discord.ext import commands
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
        if(self.client.var_start_onready == True):
            self.client.var_start_onready = False
            util.log("Initialization completed")

            serverplayers = self.client.get_channel(676209439531073541)
            sadcat = ["<:sadcat1:676391344293281802>", "<:sadcat2:676391344582688768>", "<:sadcat3:676391345320886272>", "<:sadcat4:676391344217784331>", "<:sadcat5:676391344154869770>", "<:sadcat6:676391345878859776>"]
            last_query = None

            while True:
                try:
                    server = MinecraftServer.lookup("147.135.9.96:25575")
                    status = server.status()
                    await self.client.change_presence(activity=discord.Game(name="with {} players 🎮".format(status.players.online)))
                    query = server.query()
                    playerlist = sorted(query.players.names)
                    if(last_query != playerlist):
                        if(status.players.online != 0):
                            await serverplayers.send("**{0} players: ** ``{1}``".format(status.players.online, "``, ``".join(playerlist)))
                            #print(str(datetime.datetime.now()) + " | MCSTATS | {0}".format(", ".join(query.players.names)))
                        else:
                            n = random.randint(0, 5)
                            await serverplayers.send("**0 players **" + sadcat[n])
                        last_query = playerlist
                    await asyncio.sleep(60)
                except:
                    util.log("MCSTATS", "Can't reach the Minecraft server, will try again in five minutes.")
                    await serverplayers.send("Can't reach the Minecraft server, will try again in five minutes.")
                    await asyncio.sleep(300)

#============================================================================================================#

def setup(client):
    client.add_cog(OnReady(client))
    util.log("Initialized cogs.OnReady")
