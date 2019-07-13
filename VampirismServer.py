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
from discord import User
from cogs import Moderation, AutoModeration, ServerRole, Tools
import time, os, random, asyncio
from http.server import BaseHTTPRequestHandler, HTTPServer

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

# Showing commands on the console for debug purposes:
@client.event
async def on_message(message):
    author = message.author
    channel = message.channel
    guild = message.guild
    currentTime = time.strftime("%d.%m.%Y %H:%M:%S")

    try:
        cname = channel.name
    except AttributeError as e:
        cname= "USER " + author.name
    cid= str(channel.id)
    aid= str(author.id)

    if(int(author.id) == 578935647679807491):
        print("\n---[RESPONSE]---")
        print(cname + " (" + cid + ") @ " + currentTime)
        print("> " + message.content + "")
    elif (message.content.startswith(".")):
        print("\n---[COMMAND]---")
        print("{}".format(author) + " in " + cname + " (" + cid + ") @ " + currentTime)
        print("> " + message.content + "")
    else:
        print("\n---[MESSAGE]---")
        print("{}".format(author) + " in " + cname + " (" + cid + ") @ " + currentTime)
        print("> hidden")

    await client.process_commands(message)

##############################################################################################################
### General functions ########################################################################################
##############################################################################################################

# Setting the bot's "playing" status
@client.event
async def on_ready():
    #Loading Cogs:
    client.load_extension("cogs.Moderation")        #Admin commands
    client.load_extension("cogs.AutoModeration")    #Listeners
    client.load_extension("cogs.ServerRole")        #Role command
    client.load_extension("cogs.Tools")             #For tools like .ping

    while True:
        await client.change_presence(activity=discord.Game(name='klemchri.eu'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name='vampirism.maxanier.de'))
        await asyncio.sleep(10)

#============================================================================================================#

client.run(TOKEN)
