# o     o                        o               .oPYo.                                    .oPYo.          o
# 8     8                                        8                                         8   `8          8
# 8     8 .oPYo. ooYoYo. .oPYo. o8 oPYo. .oPYo.  `Yooo. .oPYo. oPYo. o    o .oPYo. oPYo.  o8YooP' .oPYo.  o8P
# `b   d' .oooo8 8' 8  8 8    8  8 8  `' 8oooo8      `8 8oooo8 8  `' Y.  .P 8oooo8 8  `'   8   `b 8    8   8
#  `b d'  8    8 8  8  8 8    8  8 8     8.           8 8.     8     `b..d' 8.     8       8    8 8    8   8
#   `8'   `YooP8 8  8  8 8YooP'  8 8     `Yooo'  `YooP' `Yooo' 8      `YP'  `Yooo' 8       8oooP' `YooP'   8
# :::..::::.....:..:..:..8 ....::....:::::.....::::.....::.....:..::::::...:::.....:..:::::::......::.....:::.
# :::::::::::::::::::::::8 :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::..:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import discord, asyncio
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
        print("==========[VampirismBot]==========")

        discordserver = 0
        for guild in self.client.guilds:
            if guild.name == "Official Vampirism Server":
                discordserver = guild

        if discordserver == 0:
            print("[ERROR] Vampirism Server not found")
        else:
            print("\n[INFO] Currently active roles:\n")
            for role in discordserver.roles:
                print(role.name)
            print("\n[INFO] Currently active channels:\n")
            for channel in discordserver.channels:
                print(channel.name)
            print("\n[INFO] VampirismBot loaded")




        # Setting Minecraft Server
        server = MinecraftServer.lookup("147.135.9.96:25575")
        showAuthor = True

        while True:
            if showAuthor:
                await self.client.change_presence(activity=discord.Game(name='Bot by klemchri.eu'))
                await asyncio.sleep(5)
            else:
                await self.client.change_presence(activity=discord.Game(name='vampirism.maxanier.de'))
                await asyncio.sleep(5)
            showAuthor = not(showAuthor)

            try:
                status = server.status()
                await self.client.change_presence(activity=discord.Game(name="Online Players: {}".format(status.players.online)))
                await asyncio.sleep(10)
            except Exception as e:
                print("[ERROR] Service Unavailable")

#============================================================================================================#

def setup(client):
    client.add_cog(OnReady(client))
    print("[Cog] OnReady cog added")
