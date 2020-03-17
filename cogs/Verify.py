#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os, discord, asyncio, dotenv, mysql.connector, urllib.request, json
import draculogger as log
from dotenv import load_dotenv
from discord.ext import commands
from discord import User

class Verify(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

##############################################################################################################
### Verification #############################################################################################
##############################################################################################################

    @commands.command()
    async def verify(self, ctx, *arg):
        message = ctx.message
        author = message.author
        channel = message.channel

        # Get login
        db_host = os.getenv("DB_HOST")
        db_name = os.getenv("DB_NAME")
        db_acc = os.getenv("DB_ACC")
        db_pass = os.getenv("DB_PASS")

        # Make sure only the author can answer
        def check(author):
            def inner_check(message):
                if(message.author == author):
                    return True
                else:
                    return False
            return inner_check

        # Stage 1
        if(len(arg) == 0):
            await message.delete()
            botresponse = await channel.send("You need to specify a Minecraft username!")
            await asyncio.sleep(5)
            await botresponse.delete()
        else:
            mc_username = str(arg[0])
            await message.delete()
            try:
                mc_uid = urllib.request.urlopen("https://api.mojang.com/users/profiles/minecraft/" + mc_username)
                mc_uid = mc_uid.read().decode()
                mc_uid = json.loads(mc_uid)
                mc_uid = str(mc_uid["id"])
                mc_uid = mc_uid[0:8] + "-" + mc_uid[8:12] + "-" + mc_uid[12:16] + "-" + mc_uid[16:20] + "-" + mc_uid[20:32]
                try:
                    db = mysql.connector.connect(host=db_host, user=db_acc, passwd=db_pass, database=db_name)
                    cursor = db.cursor()
                    cursor.execute('''SELECT discord FROM dracula_verification WHERE minecraft = "''' + mc_uid + '''"''')
                    result = cursor.fetchall()
                    if(len(result) != 1):

                        # Stage 2
                        botresponse = await channel.send("To confirm, that " + mc_username + " is your Minecraft account, enter your current balance (/money).")
                        try:
                            userresponse = await self.client.wait_for('message', check=check(author), timeout=30)
                            bal1 = str(userresponse.content)
                            await userresponse.delete()
                            try:
                                db = mysql.connector.connect(host=db_host, user=db_acc, passwd=db_pass, database=db_name)
                                cursor = db.cursor()
                                cursor.execute('''SELECT dollar_balance FROM accounts WHERE uid = "''' + mc_uid + '''"''')
                                result = cursor.fetchall()
                                result = str(result)[11:-5]
                                if(result == bal1):
                                    await botresponse.delete()

                                    # Stage 3
                                    botresponse = await channel.send("Looking good. Now change your balance by buying or selling at the shop and enter your new balance.")
                                    try:
                                        userresponse = await self.client.wait_for('message', check=check(author), timeout=60)
                                        bal2 = str(userresponse.content)
                                        await userresponse.delete()
                                        if(bal2 != bal1):
                                            try:
                                                db = mysql.connector.connect(host=db_host, user=db_acc, passwd=db_pass, database=db_name)
                                                cursor = db.cursor()
                                                cursor.execute('''SELECT dollar_balance FROM accounts WHERE uid = "''' + mc_uid + '''"''')
                                                result = cursor.fetchall()
                                                result = str(result)[11:-5]
                                                if(result == bal2):
                                                    try:
                                                        db = mysql.connector.connect(host=db_host, user=db_acc, passwd=db_pass, database=db_name)
                                                        cursor = db.cursor()

                                                        # TODO: IDs in DB eintragen

                                                        await botresponse.delete()
                                                        botresponse = await channel.send("Verification succesful!")
                                                        await asyncio.sleep(10)
                                                        await botresponse.delete()
                                                    except:
                                                        await botresponse.delete()
                                                        botresponse = await channel.send("There has been an error whilst connecting to the database.")
                                                        await asyncio.sleep(10)
                                                        await botresponse.delete()
                                                else:
                                                    await botresponse.delete()
                                                    botresponse = await channel.send("Seems like you've entered an incorrect balance!")
                                                    await asyncio.sleep(10)
                                                    await botresponse.delete()
                                            except:
                                                await botresponse.delete()
                                                botresponse = await channel.send("There has been an error whilst connecting to the database.")
                                                await asyncio.sleep(10)
                                                await botresponse.delete()
                                        else:
                                            await botresponse.delete()
                                            botresponse = await channel.send("You need to change your balance.")
                                            await asyncio.sleep(10)
                                            await botresponse.delete()
                                    except asyncio.TimeoutError:
                                        await botresponse.delete()
                                        botresponse = await channel.send("Timed out!")
                                        await asyncio.sleep(15)
                                        await botresponse.delete()
                                else:
                                    await botresponse.delete()
                                    botresponse = await channel.send("Seems like you've entered an incorrect balance!")
                                    await asyncio.sleep(10)
                                    await botresponse.delete()
                            except:
                                await botresponse.delete()
                                botresponse = await channel.send("There has been an error whilst connecting to the database.")
                                await asyncio.sleep(10)
                                await botresponse.delete()
                        except asyncio.TimeoutError:
                            await botresponse.delete()
                            botresponse = await channel.send("Timed out!")
                            await asyncio.sleep(15)
                            await botresponse.delete()
                    else:
                        botresponse = await channel.send(mc_username + " has already been linked to another Discord account.")
                        await asyncio.sleep(10)
                        await botresponse.delete()
                except:
                    botresponse = await channel.send("There has been an error whilst connecting to the database.")
                    await asyncio.sleep(10)
                    await botresponse.delete()
            except Exception as e:
                botresponse = await channel.send("There has been an error whilst requesting the UUID of " + mc_username + " from Mojang.")
                await asyncio.sleep(10)
                await botresponse.delete()

#============================================================================================================#

def setup(client):
    client.add_cog(Verify(client))
    log.this("Initialized cogs.Verify")
