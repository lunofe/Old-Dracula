#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os, discord, asyncio, datetime
import draculogger as log
from discord.ext import commands
from discord import User

class ServerRole(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

##############################################################################################################
### Faction roles ############################################################################################
##############################################################################################################

    @commands.command()
    async def faction(self, ctx, arg):
        message = ctx.message
        author = message.author
        channel = message.channel
        roles = author.guild.roles
        emojis = ["<:d_:672399150079541279>", "<:o_:672399150297513993>", "<:n_:672399150251507712>", "<:e_:672399150263959552>", "<a:success:615843247457042434>"]

        if(arg.lower() == "vampire"):
            for role in roles:
                if(role.name == "Hunter"):
                    await author.remove_roles(role, reason="Switching to Vampire...")
                if(role.name == "Vampire"):
                    await author.add_roles(role, reason="Now a Vampire")
            log.more("FACTIONS", "{} switched to Vampire faction.".format(author))
            await message.add_reaction(emojis[0])
            await message.add_reaction(emojis[1])
            await message.add_reaction(emojis[2])
            await message.add_reaction(emojis[3])
            await message.add_reaction(emojis[4])
            await asyncio.sleep(5)
            await message.delete()
        elif (arg.lower() == "hunter"):
            for role in roles:
                if(role.name == "Vampire"):
                    await author.remove_roles(role, reason="Switching to Hunter...")
                if(role.name == "Hunter"):
                    await author.add_roles(role, reason="Now a Hunter")
            log.more("FACTIONS", "{} switched to Hunter faction.".format(author))
            await message.add_reaction(emojis[0])
            await message.add_reaction(emojis[1])
            await message.add_reaction(emojis[2])
            await message.add_reaction(emojis[3])
            await message.add_reaction(emojis[4])
            await asyncio.sleep(5)
            await message.delete()
        elif (arg.lower() == "human"):
            for role in roles:
                if(role.name == "Vampire"):
                    await author.remove_roles(role, reason="Switching to Human...")
                if(role.name == "Hunter"):
                    await author.remove_roles(role, reason="Switching to Human...")
            log.more("FACTIONS", "{} switched to Human faction.".format(author))
            await message.add_reaction(emojis[0])
            await message.add_reaction(emojis[1])
            await message.add_reaction(emojis[2])
            await message.add_reaction(emojis[3])
            await message.add_reaction(emojis[4])
            await asyncio.sleep(5)
            await message.delete()
        else:
            await message.delete()
            botresponse = await channel.send("{} That's not a valid faction! You can choose between `vampire`, `hunter` and `human`.".format(author.mention))
            await asyncio.sleep(10)
            await botresponse.delete()

##############################################################################################################
### Notifications ############################################################################################
##############################################################################################################

    @commands.command()
    async def notificationgang(self, ctx, arg):
        message = ctx.message
        author = message.author
        channel = message.channel
        roles = author.guild.roles
        emojis = ["<:d_:672399150079541279>", "<:o_:672399150297513993>", "<:n_:672399150251507712>", "<:e_:672399150263959552>", "<a:success:615843247457042434>"]

        if(arg.lower() == "join"):
            for role in roles:
                if(role.name == "NotificationGang"):
                    await author.add_roles(role, reason="Opted in to all notifications")
            log.more("NOTIFY", "{} opted into all notifications.".format(author))
            await message.add_reaction(emojis[0])
            await message.add_reaction(emojis[1])
            await message.add_reaction(emojis[2])
            await message.add_reaction(emojis[3])
            await message.add_reaction(emojis[4])
            await asyncio.sleep(5)
            await message.delete()
        elif (arg.lower() == "leave"):
            for role in roles:
                if(role.name == "NotificationGang"):
                    await author.remove_roles(role, reason="Opted out of all notifications")
            log.more("NOTIFY", "{} opted out of all notifications.".format(author))
            await message.add_reaction(emojis[0])
            await message.add_reaction(emojis[1])
            await message.add_reaction(emojis[2])
            await message.add_reaction(emojis[3])
            await message.add_reaction(emojis[4])
            await asyncio.sleep(5)
            await message.delete()
        else:
            await message.delete()
            invalidOptionMessage = await channel.send("{} That's not a valid option! You can choose between `join` and `leave`.".format(author.mention))
            await asyncio.sleep(10)
            await invalidOptionMessage.delete()

#============================================================================================================#

def setup(client):
    client.add_cog(ServerRole(client))
    log.this("Initialized cogs.ServerRole")
