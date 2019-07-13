import discord
from discord.ext import commands
from discord import User

class Tools(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None
    # 'ping' command
    @commands.command()
    async def ping(self, ctx):
        message = ctx.message
        author = message.author
        content = message.content
        channel = message.channel
        id = int(channel.id)
        await channel.send("{} Pong! :ping_pong:".format(author.mention))

def setup(client):
    client.add_cog(Tools(client))
