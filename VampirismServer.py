import discord
from discord.ext import commands
from discord import User
import time, os, random

#Insert your bot token here
TOKEN = ""

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='klemchri.de'))

@client.event
async def on_message(message):
    author = message.author
    aname = author.name
    amention = author.mention
    content = message.content
    channel = message.channel
    guild = message.guild
    currentTime = time.strftime("%d.%m.%Y %H:%M:%S")

    try:
        cname = channel.name
    except AttributeError as e:
        cname= "Private"
    cid= str(channel.id)
    aid= str(author.id)
	
    print("\n---[MESSAGE]---")
    print("Author: " + "{}".format(author) + "\nChannel Name: " + cname + "\nChannel ID: " + cid + "\nTime: " + currentTime)
    print("Content: " + content + "")

    await client.process_commands(message)

@client.command()
async def ping(ctx):
    message = ctx.message
    author = message.author
    content = message.content
    channel = message.channel
    id = int(channel.id)
    await channel.send("{} Pong! :ping_pong:".format(author.mention))

@client.command()
async def accept(ctx, user: User):
    message = ctx.message
    author = message.author
    content = message.content
    channel = message.channel
    id = int(channel.id)
    if((id == 564783779474833431) or (id == 566735724628410529)):
        await user.send("Your request was accepted by {}.".format(author.mention))
        await channel.send("Accepted :white_check_mark:")
    else:
        await channel.send("This command is suposed to be used in the \"staff-forms\" Channel")

@client.command()
async def reject(ctx, user: User, *args):
    message = ctx.message
    author = message.author
    content = message.content
    channel = message.channel
    id = int(channel.id)
    print(args)
    reason = ""
    for x in args:
        reason = reason + x + " "

    if((id == 564783779474833431) or (id == 566735724628410529)):
        print(len(args))
        if len(args) == 0:
            await user.send("Your request was rejected by {}.".format(author.mention))
            await channel.send("Rejected :x:")
        else:
            await user.send("Your request was rejected by {}. Reason: ".format(author.mention) + reason)
            await channel.send("Rejected :x:")
    else:
        await channel.send("This command is suposed to be used in the \"staff-forms\" Channel")

client.run(TOKEN)
