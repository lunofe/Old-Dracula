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

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

##############################################################################################################
### Accepting and rejecting staff applications ###############################################################
##############################################################################################################

        # 'staffyes' command - sends the tagged user an acception message for their staff apply
    @commands.command()
    async def staffyes(self, ctx, user: User):
        message = ctx.message
        author = message.author
        channel = message.channel
        guild = message.guild
        content = message.content
        id = int(channel.id)
        if((id == 564783779474833431) or (id == 590956693614100490)):
            await user.send("Your application has been accepted. You will hear from us shortly. In the meantime, you can take a look at this: <https://1literzinalco.github.io/vampirismpermissions/>")
            await channel.send(user.name + "'s Staff Apply → Accepted :white_check_mark:")
        else:
            await channel.send(":warning: This command is suposed to be used in the staff-forms Channel")
#============================================================================================================#

    # 'staffno' command - sends the tagged user a rejection message and reason for their staff apply
    @commands.command()
    async def staffno(self, ctx, user: User, *args):
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
                await user.send("Your application has been rejected. You can try again in two weeks.")
                await channel.send(user.name + "'s Staff Apply → Rejected :x:")

            else:
                await user.send("Your application has been rejected. " + reason + " You can try again in two weeks.")
                await channel.send(user.name + "'s Staff Apply → Rejected :x:")
        else:
            await channel.send(":warning: This command is suposed to be used in the staff-forms Channel")

##############################################################################################################
### Accepting and rejecting ban appeals ######################################################################
##############################################################################################################

    # 'appealyes' command - sends the tagged user an acception message for their ban appeal
    @commands.command()
    async def appealyes(self, ctx, user: User):
        message = ctx.message
        author = message.author
        content = message.content
        channel = message.channel
        id = int(channel.id)
        if((id == 564783779474833431) or (id == 590956693614100490)):
            await user.send("Your ban appeal has been accepted. You will be unbanned within 24 hours.")
            await channel.send(user.name + "'s Ban Appeal → Accepted :white_check_mark:")
        else:
            await channel.send(":warning: This command is suposed to be used in the staff-forms Channel")

#============================================================================================================#

    # 'appealno' command - sends the tagged user a rejection message and reason for their ban appeal
    @commands.command()
    async def appealno(self, ctx, user: User, *args):
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
                await channel.send(user.name + "'s Ban Appeal → Rejected :x:")

            else:
                await user.send("Your ban appeal has been rejected. " + reason + " You can appeal again in two weeks.")
                await channel.send(user.name + "'s Ban Appeal → Rejected :x:")
        else:
            await channel.send(":warning: This command is suposed to be used in the staff-forms Channel")

##############################################################################################################
### Ban and kick management ##################################################################################
##############################################################################################################

    # 'ban' command - bans the tagged user
    @commands.command()
    async def ban(self, ctx, user: User):
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
            await message.channel.send(":warning: You don't have permission.")

#============================================================================================================#

        # 'kick' command - kicks the tagged user
    @commands.command()
    async def kick(self, ctx, user: User):
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
            await message.channel.send(":warning: You don't have permission.")
#============================================================================================================#

    # Error handling
    @staffyes.error
    async def info_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(':warning: Could not find the user.')
    @staffno.error
    async def info_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(':warning: Could not find the user.')
    @appealyes.error
    async def info_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(':warning: Could not find the user.')
    @appealno.error
    async def info_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(':warning: Could not find the user.')

#============================================================================================================#

def setup(client):
    client.add_cog(Moderation(client))
