#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import utils, discord
from discord.ext import commands

class Submissions(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

#============================================================================================================#

    async def getmember(self, ctx, arg):
        if(arg.isnumeric() == True):
            # User ID was given
            member = ctx.message.guild.get_member(int(arg))
            if(member == None):
                await ctx.send(":warning: I couldn't find a server member with ID ``{}``.".format(arg))
                return
            return member
        else:
            member = ctx.message.guild.get_member_named(arg)
            if(member == None):
                try:
                    member = ctx.message.mentions[0]
                except:
                    await ctx.send(":warning: I couldn't find a server member named ``{}``.".format(arg))
                    return
                return member
            return member

##############################################################################################################
### Accepting and rejecting staff applications ###############################################################
##############################################################################################################

    # 'staffyes' command - sends the tagged user an acception message for their staff apply
    @commands.command()
    async def staffyes(self, ctx, arg):
        if((ctx.message.channel.id == 564783779474833431) or (ctx.message.channel.id == 636354667311529984)):
            user = await self.getmember(ctx, arg)
            try:
                await user.send("Your application has been accepted. You will hear from us shortly.\nIn the meantime, you can take a look at this: <https://1literzinalco.github.io/vampirism/staff.html>")
                await ctx.send("<:vote_yes:601899059417972737> " + user.name + "'s staff application has been accepted.")
            except Exception as e:
                await ctx.send(str(e))
        else:
            await ctx.send(":warning: Use this command in a proper channel to authenticate.")

#============================================================================================================#

    # 'staffno' command - sends the tagged user a rejection message and reason for their staff apply
    @commands.command()
    async def staffno(self, ctx, arg, *args):
        if((ctx.message.channel.id == 564783779474833431) or (ctx.message.channel.id == 636354667311529984)):
            reason = ""
            for argument in args:
                reason = reason + argument + " "
            user = await self.getmember(ctx, arg)
            try:
                if len(args) == 0:
                    await user.send("Your application has been rejected. You can apply again in two weeks.")
                    await ctx.send("<:vote_no:601898704231989259> " + user.name + "'s staff application has been rejected.")
                else:
                    await user.send("Your application has been rejected. You can apply again in two weeks.\n" + reason)
                    await ctx.send("<:vote_no:601898704231989259> " + user.name + "'s staff application has been rejected.")
            except Exception as e:
                await ctx.send(str(e))
        else:
            await ctx.send(":warning: Use this command in a proper channel to authenticate.")

##############################################################################################################
### Accepting and rejecting ban appeals ######################################################################
##############################################################################################################

    # 'appealyes' command - sends the tagged user an acception message for their ban appeal
    @commands.command()
    async def appealyes(self, ctx, arg):
        if((ctx.message.channel.id == 564783779474833431) or (ctx.message.channel.id == 636354667311529984)):
            user = await self.getmember(ctx, arg)
            try:
                await user.send("Your ban appeal has been accepted. You will be unbanned within 24 hours.")
                await ctx.send("<:vote_yes:601899059417972737> " + user.name + "'s ban appeal has been accepted.")
            except Exception as e:
                await ctx.send(str(e))
        else:
            await ctx.send(":warning: Use this command in a proper channel to authenticate.")

#============================================================================================================#

    # 'appealno' command - sends the tagged user a rejection message and reason for their ban appeal
    @commands.command()
    async def appealno(self, ctx, arg, *args):
        reason = ""
        for argument in args:
            reason = reason + argument + " "
        user = await self.getmember(ctx, arg)
        if((ctx.message.channel.id == 564783779474833431) or (ctx.message.channel.id == 636354667311529984)):
            try:
                if len(args) == 0:
                    await user.send("Your ban appeal has been rejected. You can appeal again in two weeks.")
                    await ctx.send("<:vote_no:601898704231989259> " + user.name + "'s ban appeal has been rejected.")
                else:
                    await user.send("Your ban appeal has been rejected. You can appeal again in two weeks.\n" + reason)
                    await ctx.send("<:vote_no:601898704231989259> " + user.name + "'s ban appeal has been rejected.")
            except Exception as e:
                await ctx.send(str(e))
        else:
            await ctx.send(":warning: Use this command in a proper channel to authenticate.")

#============================================================================================================#

def setup(client):
    client.add_cog(Submissions(client))
    utils.log("Initialized cogs.Submissions")
