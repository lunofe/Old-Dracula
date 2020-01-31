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

class Automation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

#============================================================================================================#

    # Sending a welcome message to new members and giving them the "Member" role
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(str(datetime.datetime.now()) + " | MEMBERS | {}".format(member) + " just joined the server")
        await member.send("Welcome to the official Vampirism Discord Server! To get started with the Vampirism modpack take a look at <https://chimute.org/vampirism>. We hardly ever have to mute, kick or ban people - please don't make yourself the exception and read the rules. :wink:")
        roles = member.guild.roles
        for role in roles:
            if(role.name == "Member"):
                await member.add_roles(role, reason="Member just joined the server")

#============================================================================================================#

    # Sending a goodbye message to members who left the Discord
    @commands.Cog.listener()
    async def on_member_leave(self, member):
        print(str(datetime.datetime.now()) + " | MEMBERS | {}".format(member) + " just left the server")
        member.send("We are sorry to see you go. If you want to join again, please use this link: <https://discord.gg/rP8j7hA>")

#============================================================================================================#

def setup(client):
    client.add_cog(Automation(client))
    print(str(datetime.datetime.now()) + " | Initialized cogs.Automation")
