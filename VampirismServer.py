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
from cogs import Moderation, AutoModeration
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
    aname = author.name
    amention = author.mention
    content = message.content
    channel = message.channel
    guild = message.guild
    currentTime = time.strftime("%d.%m.%Y %H:%M:%S")
    attachments = message.attachments

    try:
        cname = channel.name
    except AttributeError as e:
        cname= "USER " + author.name
    cid= str(channel.id)
    aid= str(author.id)

    if(int(author.id) == 578935647679807491):
        print("\n---[RESPONSE]---")
        print(cname + " (" + cid + ") @ " + currentTime)
        print("> " + content + "")
    elif (content.startswith(".")):
        print("\n---[COMMAND]---")
        print("{}".format(author) + " in " + cname + " (" + cid + ") @ " + currentTime)
        print("> " + content + "")
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
    client.load_extension("cogs.Moderation")
    client.load_extension("cogs.AutoModeration")

    while True:
        await client.change_presence(activity=discord.Game(name='klemchri.eu'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name='vampirism.maxanier.de'))
        await asyncio.sleep(10)

#============================================================================================================#

# 'ping' command
@client.command()
async def ping(ctx):
    message = ctx.message
    author = message.author
    content = message.content
    channel = message.channel
    id = int(channel.id)
    await channel.send("{} Pong! :ping_pong:".format(author.mention))

#============================================================================================================#

# 'role' command - lets users change their roles
@client.command()
async def role(ctx, arg):
    message = ctx.message
    author = message.author
    channel = message.channel
    guild = message.guild
    roles = author.guild.roles
    if(arg == "vampire".lower()):
        for role in roles:
            if(role.name == "Hunter"):
                await author.remove_roles(role, reason="Switched to Vampire")
            if(role.name == "Vampire"):
                await author.add_roles(role, reason="Now a Vampire")
        print("{}".format(author) + " switched to Vampire.")
    elif (arg == "hunter".lower()):
        for role in roles:
            if(role.name == "Vampire"):
                await author.remove_roles(role, reason="Switched to Hunter")
            if(role.name == "Hunter"):
                await author.add_roles(role, reason="Now a Hunter")
        print("{}".format(author) + " switched to Hunter.")
    else:
        await channel.send("{} That's not a valid role! You can choose between 'vampire' and 'hunter'.".format(author.mention))



##############################################################################################################
### Misc. functions ##########################################################################################
##############################################################################################################

# 'messageAdmins' command - sends a message to the staff's channel
@client.command()
async def messageAdmins(ctx, *args):
    if ctx.message.author.id == 152828946629525504:
        guild = client.get_guild(528346798138589215)
        channels = guild.text_channels
        message = ""

        for x in args:
            message = message + x + " "
        for channel in channels:
            if channel.id == 528350308976295946:
                msg = await channel.send(message)
                #msg.add_reaction("👍")
                #msg.add_reaction("👎")
    else:
        await ctx.message.channel.send(":warning: You don't have permission.")



##############################################################################################################
##############################################################################################################
##############################################################################################################

client.run(TOKEN)
