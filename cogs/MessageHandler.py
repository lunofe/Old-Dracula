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
import time, os, asyncio

class MessageHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

#============================================================================================================#

    # Handling Messages
    @commands.Cog.listener()
    async def on_message(self, message):
        author = message.author
        channel = message.channel
        guild = message.guild
        currentTime = time.strftime("%d.%m.%Y %H:%M:%S")

        try:
            cname = channel.name
            cid= str(channel.id)
        except AttributeError as e:
            cname= "USER " + author.name
            cid= str(author.id)

        if(int(author.id) == 578935647679807491):
            print("\n---[RESPONSE]---")
            print(cname + " (" + cid + ") @ " + currentTime)
            print("> " + message.content + "")
        elif (message.content.startswith(".")):
            print("\n---[COMMAND]---")
            print("{}".format(author) + " in " + cname + " (" + cid + ") @ " + currentTime)
            print("> " + message.content + "")
        else:
            print("\n---[MESSAGE]---")
            print("{}".format(author) + " in " + cname + " (" + cid + ") @ " + currentTime)
            print("> hidden")

        #await self.client.process_commands(message)

#============================================================================================================#

def setup(client):
    client.add_cog(MessageHandler(client))
    print("[Cog] MessageHandler cog added")
