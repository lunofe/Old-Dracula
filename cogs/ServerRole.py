#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os, discord, asyncio, datetime
from discord.ext import commands
from discord import User

class ServerRole(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

#============================================================================================================#

    # Sets the author's role to Vampire or Hunter
    @commands.command()
    async def role(self, ctx, arg):
        message = ctx.message
        author = message.author
        channel = message.channel
        roles = author.guild.roles
        emoji = "<a:success:615843247457042434>"

        if(arg.lower() == "vampire"):
            for role in roles:
                if(role.name == "Hunter"):
                    await author.remove_roles(role, reason="Switching to Vampire...")
                if(role.name == "Vampire"):
                    await author.add_roles(role, reason="Now a Vampire")
            print(str(datetime.datetime.now()) + " | " + "{}".format(author) + " switched to Vampire faction.")
            await message.add_reaction(emoji)
        elif (arg.lower() == "hunter"):
            for role in roles:
                if(role.name == "Vampire"):
                    await author.remove_roles(role, reason="Switching to Hunter...")
                if(role.name == "Hunter"):
                    await author.add_roles(role, reason="Now a Hunter")
            print(str(datetime.datetime.now()) + " | " + "{}".format(author) + " switched to Hunter faction.")
            await message.add_reaction(emoji)
        elif (arg.lower() == "human"):
            for role in roles:
                if(role.name == "Vampire"):
                    await author.remove_roles(role, reason="Switching to Human...")
                if(role.name == "Hunter"):
                    await author.remove_roles(role, reason="Switching to Human...")
            print(str(datetime.datetime.now()) + " | " + "{}".format(author) + " opted out of factions.")
            await message.add_reaction(emoji)
        else:
            await channel.send("{} That's not a valid role! You can choose between `vampire`, `hunter` and `human`.".format(author.mention))

#============================================================================================================#

def setup(client):
    client.add_cog(ServerRole(client))
    print(str(datetime.datetime.now()) + " | Initialized cogs.ServerRole")
