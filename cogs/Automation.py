#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import config, utils, random, string, discord
from discord.ext import commands

class Automation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

#============================================================================================================#

    # Sending a welcome message to new members and giving them the "Member" role
    @commands.Cog.listener()
    async def on_member_join(self, member):
        utils.log("MEMBER", "{} ({}) just joined the server".format(member, member.id))
        role_member = member.guild.get_role(543106097997676554)
        channel_staffimportant = member.guild.get_channel(565239330763964416)

        if(member.id in config.SPAM):
            secret = "".join((random.choice(string.ascii_letters + string.digits) for i in range(16)))
            try:
                await member.send("**Manual Verification Required**\nYou have triggered our spam protection and are therefore not authorized to read or write messages.\nPlease contact <@267633670532104193> or open a ticket in the <#679722116043505723> channel and provide this code: ||``{}``||".format(secret))
                await channel_staffimportant.send("<@{}> has joined the server and triggered the spam protection. Secret: ||``{}``||".format(member.id, secret))
            except Exception as e:
                await channel_staffimportant.send("<@{}> has joined the server and triggered the spam protection, but I couldn't let them know: {}".format(member.id, e))
        else:
            await member.add_roles(role_member, reason="Member just joined the server")
            try:
                await member.send("Welcome to the Official Vampirism Server! To get started with the Vampirism modpack take a look at <https://chimute.org/vampirism>. We hardly ever have to mute, kick or ban people - please don't make yourself the exception and read the rules. :wink:")
            except Exception as e:
                print(str(e))

#============================================================================================================#

def setup(client):
    client.add_cog(Automation(client))
    utils.log("Initialized cogs.Automation")
