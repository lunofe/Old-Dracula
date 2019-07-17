# o     o                        o               .oPYo.                                    .oPYo.          o
# 8     8                                        8                                         8   `8          8
# 8     8 .oPYo. ooYoYo. .oPYo. o8 oPYo. .oPYo.  `Yooo. .oPYo. oPYo. o    o .oPYo. oPYo.  o8YooP' .oPYo.  o8P
# `b   d' .oooo8 8' 8  8 8    8  8 8  `' 8oooo8      `8 8oooo8 8  `' Y.  .P 8oooo8 8  `'   8   `b 8    8   8
#  `b d'  8    8 8  8  8 8    8  8 8     8.           8 8.     8     `b..d' 8.     8       8    8 8    8   8
#   `8'   `YooP8 8  8  8 8YooP'  8 8     `Yooo'  `YooP' `Yooo' 8      `YP'  `Yooo' 8       8oooP' `YooP'   8
# :::..::::.....:..:..:..8 ....::....:::::.....::::.....::.....:..::::::...:::.....:..:::::::......::.....:::.
# :::::::::::::::::::::::8 :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::..:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import discord
from discord.ext import commands
from cogs import Moderation, AutoModeration, ServerRole, Tools
import time, os, asyncio
from keep_alive import keep_alive
from mcstatus import MinecraftServer

##############################################################################################################
### Initial stuff ############################################################################################
##############################################################################################################

# Settings the bot's token
TOKEN = ""

#============================================================================================================#

# Setting the bot's command prefix
client = commands.Bot(command_prefix = ".")

#============================================================================================================#

# Removing the standard 'help' command
client.remove_command("help")

#============================================================================================================#

#Setting Minecraft Server
server = MinecraftServer.lookup("147.135.9.96:25575")

##############################################################################################################
### General functions ########################################################################################
##############################################################################################################

# Setting the bot's "playing" status
@client.event
async def on_ready():
    #Loading Cogs:
    client.load_extension("cogs.MessageHandler")    #Message and Command handling
    client.load_extension("cogs.Moderation")        #Admin commands
    client.load_extension("cogs.AutoModeration")    #Listeners
    client.load_extension("cogs.ServerRole")        #Role command
    client.load_extension("cogs.Tools")             #For tools like .ping

    while True:
        await client.change_presence(activity=discord.Game(name='Bot by klemchri.eu'))
        await asyncio.sleep(5)

        try:
            status = server.status()
            await client.change_presence(activity=discord.Game(name="Online Players: {}".format(status.players.online)))
            await asyncio.sleep(10)
        except Exception as e:
            print("[ERROR] Service Unavailable")

        await client.change_presence(activity=discord.Game(name='vampirism.maxanier.de'))
        await asyncio.sleep(10)

        try:
            latency = server.ping()
            await client.change_presence(activity=discord.Game(name="Ping: {} ms".format(latency)))
            await asyncio.sleep(10)
        except Exception as e:
            print("[ERROR] Service Unavailable")

#============================================================================================================#

keep_alive()
client.run(TOKEN)
