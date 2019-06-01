import discord
from discord.ext import commands
from discord import User
import time, os, random
import mysql.connector

# Insert your bot token here.
TOKEN = ""

#Opening connection to mysql
mydb = mysql.connector.connect(host="", user="", passwd="", database="")
mycursor = mydb.cursor()

# Setting the bot prefix
client = commands.Bot(command_prefix = ".")

# Setting the bot's "playing" status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='klemchri.de'))

# Sending a welcome message to new Members and giving them the "Member" role
@client.event
async def on_member_join(member):
    print("\n---[JOIN]---\n{}".format(member))
    await member.send("Welcome to the official Vampirism Discord Server.")
    roles = member.guild.roles
    for role in roles:
        if(role.name == "Member"):
            await member.add_roles(role, reason="Member just joined the Server")

    # Insert your guild id here
    if member.guild.id == "528346798138589215":
        mycursor = mydb.cursor()
        request = "INSERT INTO VampirismBot VALUES (%s, %s, %s)"
        insert = (int(member.id), 0, 0)
        mycursor.execute(request, insert)
        mydb.commit()

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
        print("Content: " + content + "")
    elif (content.startswith(".")):
        print("\n---[COMMAND]---")
        print("Author: " + "{}".format(author) + "\nChannel Name: " + cname + "\nChannel ID: " + cid + "\nTime: " + currentTime)
        print("Content: " + content + "")
    else:
        print("\n---[MESSAGE]---")
        print("Author: " + "{}".format(author) + "\nChannel Name: " + cname + "\nChannel ID: " + cid + "\nTime: " + currentTime)
        print("Content: " + content + "")
        updateDatabase(auhor.id)

    # Logging only public messages:
    if not(cname.startswith("USER")):
        if not(len(attachments) == 0):
            print("Attachment: " + attachments[0].filename)
            f = open(("logs/" + cname + ".html"), 'a+')
            f.write("Author: " + "{}".format(author) + "</br>\nAuthor ID: "+ aid + "</br>\nChannel Name: " + cname + "</br>\nChannel ID: " + cid + "</br>\nTime: " + currentTime +  "</br>\nContent: " + content + "</br>\nAttachments: " + attachments[0].filename + "</br>\n</br>\n")
            f.close()
        else:
            f = open(("logs/" + cname + ".html"), 'a+')
            f.write("Author: " + "{}".format(author) + "</br>\nAuthor ID: "+ aid + "</br>\nChannel Name: " + cname + "</br>\nChannel ID: " + cid + "</br>\nTime: " + currentTime +  "</br>\nContent: " + content + "</br>\n</br>\n")
            f.close()


        for attachment in attachments:
            await attachment.save("logs/attachments/" + attachment.filename)

    await client.process_commands(message)

# .ping command - bot answers with pong
@client.command()
async def ping(ctx):
    message = ctx.message
    author = message.author
    content = message.content
    channel = message.channel
    id = int(channel.id)
    await channel.send("{} Pong! :ping_pong:".format(author.mention))

# .accept command - sends the tagged user accepted message
@client.command()
async def accept(ctx, user: User):
    message = ctx.message
    author = message.author
    content = message.content
    channel = message.channel
    id = int(channel.id)
    if((id == 564783779474833431) or (id == 566735724628410529)):
        await user.send("Your application has been accepted. You will hear from us shortly.")
        await channel.send("Accepted :white_check_mark:")
    else:
        await channel.send("This command is suposed to be used in the \"staff-forms\" Channel")

# .reject command - sends the tagged user rejected message and reason, if given
@client.command()
async def reject(ctx, user: User, *args):
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
            await channel.send("Rejected :x:")
        else:
            await user.send("Your application has been rejected. Reason: " + reason + " You can apply again in two weeks.")
            await channel.send("Rejected :x:")
    else:
        await channel.send("This command is suposed to be used in the \"staff-forms\" Channel")

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

# ONLY run this command if you just setup the Bot
@client.command()
async def setupDB(ctx):
    if ctx.message.author.id == 152828946629525504:
        guild = ctx.message.guild
        members = guild.members
        mycursor = mydb.cursor()
        request = "INSERT INTO VampirismBot VALUES (%s, %s, %s)"
        for member in members:
            membertoinsert = (int(member.id), 0, 0)
            mycursor.execute(request, membertoinsert)
            mydb.commit()
    else:
        await ctx.message.channel.send("You dont have the permission to do that.")

def updateDatabase(userID):
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE VampirismBot SET MESSAGES=MESSAGES+1 WHERE ID ="+userID)
    mydb.commit()

client.run(TOKEN)


# .printNameToConsole command - prints the bot's name to the console
#@client.command()
#async def printNameToConsole(ctx):
#    message = ctx.message
#    print("\n##########\nChimute Vampirism\n##########")
#    await message.channel.send("Done :white_check_mark:")


# Checking for roles - Testing for other commands
#@client.command()
#async def checkForRole(ctx, roleName):
#    message = ctx.message
#    author = message.author
#    roles = author.roles
#
#    hasRole = False
#    for role in roles:
#        rname = role.name.lower()
#        print(rname)
#
#        if rname == roleName.lower():
#            await message.channel.send("You have the \"" + roleName + "\" role.")
#            hasRole = True
#    if not(hasRole):
#        await message.channel.send("You dont have the \"" + roleName + "\" role.")
