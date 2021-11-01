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

class MessageHandler(commands.Cog):
    def __init__(self, client):
        self.client = client

#============================================================================================================#

    # Handling Messages
    @commands.Cog.listener()
    async def on_message(self, message):
        author = message.author
        channel = message.channel

        try: # Channel is channel
            channel_name = channel.name
            channel_id = channel.id
        except: # Channel is dm with user
            channel_name = "Direct Message with " + str(channel.recipient)
            channel_id = channel.recipient.id

        if(author.id == 578935647679807491):
            if(channel.id != 676209439531073541): # Disable logging for channel #serverplayers to prevent spam
                utils.log("DRACULA", "@ {} ({}) 💬 {}".format(channel_name, channel_id, message.content))
        elif(message.content.startswith(".")):
            utils.log("COMMAND", "{} ({}) @ {} ({}) 💬 {}".format(author, author.id, channel_name, channel_id, message.content))
        #elif(((" ip" in message.content.lower())  or  (("server" in message.content.lower())  and  ("when" in message.content.lower()))  or  (("server" in message.content.lower())  and  ("offline" in message.content.lower()))  or  (("server" in message.content.lower())  and  ("down" in message.content.lower()))  or  (("server" in message.content.lower())  and  ("up" in message.content.lower())))):
            #embed=discord.Embed(title="The server is currently offline.", description="We started upgrading the server on New Year's Eve. As soon as there is news, it will be announced in #news. Please don't message or @ping staff members to ask if the server is online or if we have a new ETA.")
            #embed.set_footer(text="This is a bot, and this action was performed automatically. If you didn't ask for the IP or when the server will be online, we're sorry.")
            #await message.channel.send(embed=embed)
        else:
            pass

#============================================================================================================#

def setup(client):
    client.add_cog(MessageHandler(client))
    utils.log("Initialized cogs.MessageHandler")
