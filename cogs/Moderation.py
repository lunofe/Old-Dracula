#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os, discord, asyncio, datetime, dotenv
from discord.ext import commands
from dotenv import load_dotenv
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
        channel_id = int(channel.id)

        if((channel_id == 564783779474833431) or (channel_id == 636354667311529984)):
            try:
                await user.send("Your application has been accepted. You will hear from us shortly.\nIn the meantime, you can take a look at this: <https://1literzinalco.github.io/VampPerms>")
                await channel.send("<:vote_yes:601899059417972737> " + user.name + "'s staff application has been accepted.")
            except:
                await channel.send(":warning: Invalid user.")
        else:
            await channel.send(":warning: Use this command in a proper channel to authenticate.")

#============================================================================================================#

    # 'staffno' command - sends the tagged user a rejection message and reason for their staff apply
    @commands.command()
    async def staffno(self, ctx, user: User, *args):
        message = ctx.message
        author = message.author
        channel = message.channel
        channel_id = int(channel.id)
        reason = ""
        for argument in args:
            reason = reason + argument + " "

        if((channel_id == 564783779474833431) or (channel_id == 636354667311529984)):
            try:
                if len(args) == 0:
                    await user.send("Your application has been rejected. You can apply again in two weeks.")
                    await channel.send("<:vote_no:601898704231989259> " + user.name + "'s staff application has been rejected.")
                else:
                    await user.send("Your application has been rejected. You can apply again in two weeks.\n" + reason)
                    await channel.send("<:vote_no:601898704231989259> " + user.name + "'s staff application has been rejected.")
            except:
                await channel.send(":warning: Invalid user.")
        else:
            await channel.send(":warning: Use this command in a proper channel to authenticate.")

##############################################################################################################
### Accepting and rejecting ban appeals ######################################################################
##############################################################################################################

    # 'appealyes' command - sends the tagged user an acception message for their ban appeal
    @commands.command()
    async def appealyes(self, ctx, user: User):
        message = ctx.message
        author = message.author
        channel = message.channel
        channel_id = int(channel.id)

        if((channel_id == 564783779474833431) or (channel_id == 636354667311529984)):
            try:
                await user.send("Your ban appeal has been accepted. You will be unbanned within 24 hours.")
                await channel.send("<:vote_yes:601899059417972737> " + user.name + "'s ban appeal has been accepted.")
            except:
                await channel.send(":warning: Invalid user.")
        else:
            await channel.send(":warning: Use this command in a proper channel to authenticate.")

#============================================================================================================#

    # 'appealno' command - sends the tagged user a rejection message and reason for their ban appeal
    @commands.command()
    async def appealno(self, ctx, user: User, *args):
        message = ctx.message
        author = message.author
        channel = message.channel
        channel_id = int(channel.id)

        reason = ""
        for argument in args:
            reason = reason + argument + " "

        if((channel_id == 564783779474833431) or (channel_id == 636354667311529984)):
            try:
                if len(args) == 0:
                    await user.send("Your ban appeal has been rejected. You can appeal again in two weeks.")
                    await channel.send("<:vote_no:601898704231989259> " + user.name + "'s ban appeal has been rejected.")
                else:
                    await user.send("Your ban appeal has been rejected. You can appeal again in two weeks.\n" + reason)
                    await channel.send("<:vote_no:601898704231989259> " + user.name + "'s ban appeal has been rejected.")
            except:
                await channel.send(":warning: Invalid user.")
        else:
            await channel.send(":warning: Use this command in a proper channel to authenticate.")

#============================================================================================================#

def setup(client):
    client.add_cog(Moderation(client))
    print(str(datetime.datetime.now()) + " | Initialized cogs.Moderation")
