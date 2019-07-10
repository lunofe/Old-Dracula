import discord
from discord.ext import commands
from discord import User
import time, os, random, asyncio
from http.server import BaseHTTPRequestHandler, HTTPServer

# Insert your bot token here.
TOKEN = ""


# Setting the bot's command prefix
client = commands.Bot(command_prefix = ".")

client.remove_command("help")


# Setting the bot's "playing" status
@client.event
async def on_ready():
    while True:
        await client.change_presence(activity=discord.Game(name='klemchri.eu'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name='vampirism.maxanier.de'))
        await asyncio.sleep(10)



# Sending a welcome message to new members and giving them the "Member" role
@client.event
async def on_member_join(member):
    print("\n---[JOIN]---\nUser: {}".format(member))
    await member.send("Welcome to the official Vampirism Discord Server! To get started with the Vampirism modpack take a look at <https://chimute.org/vampirism>. We hardly ever have to mute, kick or ban people - please don't make yourself the exception and read the rules. :wink:")
    roles = member.guild.roles
    for role in roles:
        if(role.name == "Member"):
            await member.add_roles(role, reason="Member just joined the Server")


# Do I need to explain this?
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

    # Showing all messages on the console for debug purposes:
    if(int(author.id) == 578935647679807491):
        print("\n---[RESPONSE]---")
        print("Channel Name: " + cname + "\nChannel ID: " + cid + "\nTime: " + currentTime)
        print("Content: " + content)
    elif (content.startswith(".")):
        print("\n---[COMMAND]---")
        print("Author: " + "{}".format(author) + "\nChannel Name: " + cname + "\nChannel ID: " + cid + "\nTime: " + currentTime)
        print("Content: " + content)
    else:
        print("\n---[MESSAGE]---")
        print("Author: " + "{}".format(author) + "\nChannel Name: " + cname + "\nChannel ID: " + cid + "\nTime: " + currentTime)
        print("Content: hidden")

    await client.process_commands(message)


@client.command()
async def help(ctx):
    try:
        await ctx.message.channel.send("Are you new to the Vampirism mod? Do /kit vamp_guide ingame and you'll get everything you need!\nHow does XY work on the server? Check <https://chimute.org/vampirism/guidebook>!\nStill need help? Ask your question in #questions-and-help!")
    except Exception as e:
        await ctx.message.author.send("Are you new to the Vampirism mod? Do /kit vamp_guide ingame and you'll get everything you need!\nHow does XY work on the server? Check <https://chimute.org/vampirism/guidebook>!\nStill need help? Ask your question in #questions-and-help!")


# .ping command - bot answers with pong
@client.command()
async def ping(ctx):
    message = ctx.message
    author = message.author
    content = message.content
    channel = message.channel
    id = int(channel.id)
    await channel.send("{} Pong! :ping_pong:".format(author.mention))


# .staffyes command - sends the tagged user acception message for their staff apply
@client.command()
async def staffyes(ctx, user: User):
    message = ctx.message
    author = message.author
    channel = message.channel
    guild = message.guild
    content = message.content
    id = int(channel.id)
    if((id == 564783779474833431) or (id == 590956693614100490)):
        await user.send("Your application has been accepted. You will hear from us shortly. In the meantime, you can take a look at this: <https://docs.google.com/document/d/1ccsL4FCVgQVUcLTi82ed8raa7AZlTsUaCqBnFbZzNEk>")
        await channel.send("Staff Apply → Accepted :white_check_mark:")
    else:
        await channel.send("This command is suposed to be used in the staff-forms Channel")


# .staffno command - sends the tagged user rejection message and reason for their staff apply
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
            await user.send("Your application has been rejected. You can apply again in two weeks.")
            await channel.send("Staff Apply → Rejected :x:")

        else:
            await user.send("Your application has been rejected. Reason: " + reason + " You can apply again in two weeks.")
            await channel.send("Staff Apply → Rejected :x:")
    else:
        await channel.send("This command is suposed to be used in the staff-forms Channel")


# .appealyes command - sends the tagged user acception message for their ban appeal
@client.command()
async def appealyes(ctx, user: User):
    message = ctx.message
    author = message.author
    content = message.content
    channel = message.channel
    id = int(channel.id)
    if((id == 564783779474833431) or (id == 590956693614100490)):
        await user.send("Your ban appeal has been accepted. You will be unbanned within 24 hours.")
        await channel.send("Ban Appeal → Accepted :white_check_mark:")
    else:
        await channel.send("This command is suposed to be used in the staff-forms Channel")


# .appealno command - sends the tagged user rejection message and reason for their ban appeal
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
            await channel.send("Ban Appeal → Rejected :x:")

        else:
            await user.send("Your ban appeal has been rejected. Reason: " + reason + " You can appeal again in two weeks.")
            await channel.send("Ban Appeal → Rejected :x:")
    else:
        await channel.send("This command is suposed to be used in the staff-forms Channel")


# .ban command - bans the tagged user
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
        await message.channel.send("You don't have the permission to do that.")


# .kick command - kicks the tagged user
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
        await message.channel.send("You don't have the permission to do that.")


# .changePresence command - changes the bot's "playing" status via Discord
#@client.command()
#async def changePresence(ctx, *args):
#    auhtorID = int(ctx.message.author.id)
#    if(auhtorID == 152828946629525504 or auhtorID == 267633670532104193): # Change to your ID
#        playing = ""
#        for word in args:
#            playing = playing + word
#        await client.change_presence(activity=discord.Game(name=playing))
#    else:
#        await ctx.message.channel.send("You don't have the permission to do that.")


# .messageAdmins command - sends a message to the staff's channel
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
        await ctx.message.channel.send("You don't have the permission to do that.")

# .role command - let users change their roles
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

# Error handling
@staffyes.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Bad Argument: User not found')

@staffno.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Bad Argument: User not found')

@appealyes.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Bad Argument: User not found')

@appealno.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Bad Argument: User not found')


client.run(TOKEN)
