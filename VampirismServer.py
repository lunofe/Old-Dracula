import discord
from discord.ext import commands
from discord import User
import time, os, random

# Insert your bot token here.
TOKEN = ""


# Setting the bot's command prefix
client = commands.Bot(command_prefix = ".")

# Setting the bot's "playing" status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='klemchri.de'))

# Sending a welcome message to new members and giving them the "Member" role
@client.event
async def on_member_join(member):
    print("\n---[JOIN]---\n{}".format(member))
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
        print(cname + " (" + cid + ") @ " + currentTime)
        print("> " + content + "")
    elif (content.startswith(".")):
        print("\n---[COMMAND]---")
        print("{}".format(author) + " in " + cname + " (" + cid + ") @ " + currentTime)
        print("> " + content + "")
    else:
        print("\n---[MESSAGE]---")

@client.event
async def on_reaction_add(reaction, user):
    print("\n---[REACTION]---")
    print("{} has reacted with ".format(user) + reaction.emoji + " to "+ reaction.message.content + " (" reaction.message.id + ")")

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
    content = message.content
    channel = message.channel
    id = int(channel.id)
    if((id == 564783779474833431) or (id == 566735724628410529) or (id == 571594243852992513)):
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

    if((id == 564783779474833431) or (id == 566735724628410529)):
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
    if((id == 564783779474833431) or (id == 566735724628410529) or (id == 571594243852992513)):
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

    if((id == 564783779474833431) or (id == 566735724628410529)):
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
        await message.channel.send("You dont have the permission to do that.")

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
        await message.channel.send("You dont have the permission to do that.")

# .changePresence command - changes the bot's "playing" status via Discord
@client.command()
async def changePresence(ctx, *args):
    auhtorID = int(ctx.message.author.id)
    if(auhtorID == 152828946629525504 or auhtorID == 267633670532104193): # Change to your ID
        playing = ""
        for word in args:
            playing = playing + word
        await client.change_presence(activity=discord.Game(name=playing))
    else:
        await ctx.message.channel.send("You dont have the permission to do that.")

# .messageAdmins command - sends a message to the staff's channel
@client.command()
async def messageAdmins(ctx, *args):
    guild = client.get_guild(528346798138589215)
    channels = guild.text_channels
    message = ""

    for x in args:
        message = message + x + " "
    for channel in channels:
        if channel.id == 564783442206654466:
            msg = await channel.send(message)
            #msg.add_reaction("👍")
            #msg.add_reaction("👎")

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
