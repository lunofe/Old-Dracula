#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import discord
import draculogger as log
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

#============================================================================================================#

    @commands.command()
    async def MdKsJnZzzeLEfQRs(self, ctx):
        voicechannel = self.client.get_channel(574505494698262538)
        v = [None, None]
        try:
            await v[1].disconnect()
            v[1] = None
            log.more("MUSIC", "Bot has left the previous voice channel")
        except Exception as e:
            log.more("MUSIC", str(e))
        try:
            v[0] = voicechannel
            try:
                v[1] = await v[0].connect()
                log.more("MUSIC", "Bot has joined the voice channel")
            except Exception as e:
                log.more("MUSIC", str(e))
        except Exception as e:
            log.more("MUSIC", str(e))
        try:
            v[1].play(discord.FFmpegPCMAudio("/home/dracula/ping.mp3"))
            log.more("MUSIC", "Bot has started streaming")
        except Exception as e:
            log.more("MUSIC", str(e))

#============================================================================================================#

def setup(client):
    client.add_cog(Music(client))
    log.more("Initialized cogs.Music")
