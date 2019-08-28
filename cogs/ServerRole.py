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
            print("{}".format(author) + " switched to Vampire faction.")
            await message.add_reaction(emoji)
        elif (arg.lower() == "hunter"):
            for role in roles:
                if(role.name == "Vampire"):
                    await author.remove_roles(role, reason="Switching to Hunter...")
                if(role.name == "Hunter"):
                    await author.add_roles(role, reason="Now a Hunter")
            print("{}".format(author) + " switched to Hunter faction.")
            await message.add_reaction(emoji)
        else:
            await channel.send("{} That's not a valid role! You can choose between `vampire` and `hunter`.".format(author.mention))

#============================================================================================================#

def setup(client):
    client.add_cog(ServerRole(client))
    print("[Cog] ServerRole cog added")
