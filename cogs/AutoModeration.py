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

class AutoModeration(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

#============================================================================================================#

    # Sending a welcome message to new members and giving them the "Member" role
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print("\n---[JOIN]---\nUser: {}".format(member))
        await member.send("Welcome to the official Vampirism Discord Server! To get started with the Vampirism modpack take a look at <https://chimute.org/vampirism>. We hardly ever have to mute, kick or ban people - please don't make yourself the exception and read the rules. :wink:")
        roles = member.guild.roles
        for role in roles:
            if(role.name == "Member"):
                await member.add_roles(role, reason="Member just joined the Server")

#============================================================================================================#

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        print("\n---[LEAVE]---\nUser: {}".format(member))
        member.send("We are sorry to see you go. If you want to join again please use this link: <https://discord.gg/rP8j7hA>")

#============================================================================================================#

def setup(client):
    client.add_cog(AutoModeration(client))
    print("[Cog] AutoModeration cog added")
