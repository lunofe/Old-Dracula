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

    await client.process_commands(message)

##############################################################################################################
### General functions ########################################################################################
##############################################################################################################

# Setting the bot's "playing" status
@client.event
async def on_ready():
    while True:
        await client.change_presence(activity=discord.Game(name='klemchri.eu'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name='vampirism.maxanier.de'))
        await asyncio.sleep(10)

#============================================================================================================#

# Sending a welcome message to new members and giving them the "Member" role
@client.event
async def on_member_join(member):
    print("\n---[JOIN]---\nUser: {}".format(member))
    await member.send("Welcome to the official Vampirism Discord Server! To get started with the Vampirism modpack take a look at <https://chimute.org/vampirism>. We hardly ever have to mute, kick or ban people - please don't make yourself the exception and read the rules. :wink:")
    roles = member.guild.roles
    for role in roles:
        if(role.name == "Member"):
            await member.add_roles(role, reason="Member just joined the Server")

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
### Accepting and rejecting staff applications ###############################################################
##############################################################################################################

# 'staffyes' command - sends the tagged user an acception message for their staff apply
@client.command()
async def staffyes(ctx, user: User):
    message = ctx.message
    author = message.author
    channel = message.channel
    guild = message.guild
    content = message.content
    id = int(channel.id)
    if((id == 564783779474833431) or (id == 590956693614100490)):
        await user.send("Your application has been accepted. You will hear from us shortly. In the meantime, you can take a look at this: <https://1literzinalco.github.io/vampirismpermissions/>")
        await channel.send(user.name + "'s Staff Apply → Accepted :white_check_mark:")
    else:
        await channel.send(":warning: This command is suposed to be used in the staff-forms Channel")

#============================================================================================================#

# 'staffno' command - sends the tagged user a rejection message and reason for their staff apply
@client.command()
async def staffno(ctx, user: User, *args):
    message = ctx.message
    author = message.author
    content = message.content
    channel = message.channel
    id = int(channel.id)
    print(args)
    reason = ""
    for argument in args:
        reason = reason + argument + " "

    if((id == 564783779474833431) or (id == 590956693614100490)):
        print(len(args))
        if len(args) == 0:
            await user.send("Your application has been rejected. You can try again in two weeks.")
            await channel.send(user.name + "'s Staff Apply → Rejected :x:")

        else:
            await user.send("Your application has been rejected. " + reason + " You can try again in two weeks.")
            await channel.send(user.name + "'s Staff Apply → Rejected :x:")
    else:
        await channel.send(":warning: This command is suposed to be used in the staff-forms Channel")

##############################################################################################################
### Accepting and rejecting ban appeals ######################################################################
##############################################################################################################

# 'appealyes' command - sends the tagged user an acception message for their ban appeal
@client.command()
async def appealyes(ctx, user: User):
    message = ctx.message
    author = message.author
    content = message.content
    channel = message.channel
    id = int(channel.id)
    if((id == 564783779474833431) or (id == 590956693614100490)):
        await user.send("Your ban appeal has been accepted. You will be unbanned within 24 hours.")
        await channel.send(user.name + "'s Ban Appeal → Accepted :white_check_mark:")
    else:
        await channel.send(":warning: This command is suposed to be used in the staff-forms Channel")

#============================================================================================================#

# 'appealno' command - sends the tagged user a rejection message and reason for their ban appeal
@client.command()
async def appealno(ctx, user: User, *args):
    message = ctx.message
    author = message.author
    content = message.content
    channel = message.channel
    id = int(channel.id)
    print(args)
    reason = ""
    for argument in args:
        reason = reason + argument + " "

    if((id == 564783779474833431) or (id == 590956693614100490)):
        print(len(args))
        if len(args) == 0:
            await user.send("Your ban appeal has been rejected. You can appeal again in two weeks.")
            await channel.send(user.name + "'s Ban Appeal → Rejected :x:")

        else:
            await user.send("Your ban appeal has been rejected. " + reason + " You can appeal again in two weeks.")
            await channel.send(user.name + "'s Ban Appeal → Rejected :x:")
    else:
        await channel.send(":warning: This command is suposed to be used in the staff-forms Channel")

##############################################################################################################
### Ban and kick management ##################################################################################
##############################################################################################################

# 'ban' command - bans the tagged user
@client.command()
async def ban(ctx, user: User):
    message = ctx.message
    author = message.author
    roles = author.roles

    hasRole = False
    for role in roles:
        rname = role.name.lower()
        if (rname == "admin") or (rname == "sr admin"):
            await ctx.message.guild.ban(user)
            await ctx.message.channel.send(user.name + " was banned.")
            hasRole = True

    if not(hasRole):
        await message.channel.send(":warning: You don't have permission.")

#============================================================================================================#

# 'kick' command - kicks the tagged user
@client.command()
async def kick(ctx, user: User):
    message = ctx.message
    author = message.author
    roles = author.roles

    hasRole = False
    for role in roles:
        rname = role.name.lower()
        if (rname == "admin") or (rname == "sr admin"):
            await ctx.message.guild.kick(user)
            await ctx.message.channel.send(user.name + " was kicked.")
            hasRole = True

    if not(hasRole):
        await message.channel.send(":warning: You don't have permission.")

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

#============================================================================================================#

# Error handling
@staffyes.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(':warning: Could not find the user.')
@staffno.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(':warning: Could not find the user.')
@appealyes.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(':warning: Could not find the user.')
@appealno.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(':warning: Could not find the user.')

##############################################################################################################
##############################################################################################################
##############################################################################################################

client.run(TOKEN)
