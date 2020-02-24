#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os, discord, asyncio, datetime, dotenv, mysql.connector, urllib.request, json
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

        # Init
        stage = 0

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
                print("Selected " + mc_username + " (" + mc_uid + ")")
                stage = 1

                # Stage 2
                if(stage == 1):
                    botresponse = await channel.send("To confirm, that " + mc_username + " is your Minecraft account, enter your current balance (/money).")
                    try:
                        userresponse = await self.client.wait_for('message', check=check(author), timeout=30)
                        bal1 = str(userresponse.content)
                        await userresponse.delete()
                        try:
                            db = mysql.connector.connect(
                               host=db_host,
                               user=db_acc,
                               passwd=db_pass,
                               database=db_name
                            )
                            cursor = db.cursor()
                            try:
                                cursor.execute('''SELECT dollar_balance FROM accounts WHERE uid = "''' + mc_uid + '''"''')
                                result = cursor.fetchall()
                                result = str(result)[11:-5]
                                if(result == bal1):
                                    await botresponse.delete()
                                    print("Bal 1 matches")
                                    stage = 2

                                    # Stage 3
                                    if(stage == 2):
                                        botresponse = await channel.send("Looking good. Now change your balance by buying or selling at the shop and enter your new balance.")
                                        try:
                                            userresponse = await self.client.wait_for('message', check=check(author), timeout=30)
                                            bal2 = str(userresponse.content)
                                            await userresponse.delete()
                                            if(bal2 == bal1):
                                                await botresponse.delete()
                                                botresponse = await channel.send("You need to change your balance.")
                                                await asyncio.sleep(5)
                                                await botresponse.delete()
                                            else:
                                                try:
                                                    db = mysql.connector.connect(
                                                       host=db_host,
                                                       user=db_acc,
                                                       passwd=db_pass,
                                                       database=db_name
                                                    )
                                                    cursor = db.cursor()
                                                    try:
                                                        cursor.execute('''SELECT dollar_balance FROM accounts WHERE uid = "''' + mc_uid + '''"''')
                                                        result = cursor.fetchall()
                                                        result = str(result)[11:-5]
                                                        if(result == bal2):
                                                            await botresponse.delete()
                                                            print("Bal 2 matches")
                                                            botresponse = await channel.send("Verification succesful!")
                                                            await asyncio.sleep(5)
                                                            await botresponse.delete()
                                                        else:
                                                            await botresponse.delete()
                                                            botresponse = await channel.send("Seems like you've entered an incorrect balance!")
                                                            stage = 0
                                                            await asyncio.sleep(5)
                                                            await botresponse.delete()
                                                    except:
                                                        await botresponse.delete()
                                                        botresponse = await channel.send("There has been an error whilst requesting the balance of " + mc_username + "(" + mc_uid + ").")
                                                        await asyncio.sleep(5)
                                                        await botresponse.delete()
                                                except:
                                                    await botresponse.delete()
                                                    botresponse = await channel.send("There has been an error whilst connecting to the database.")
                                                    await asyncio.sleep(5)
                                                    await botresponse.delete()
                                        except asyncio.TimeoutError:
                                            await botresponse.delete()
                                            botresponse = await channel.send("Timed out!")
                                            await asyncio.sleep(10)
                                            await botresponse.delete()
                                else:
                                    await botresponse.delete()
                                    botresponse = await channel.send("Seems like you've entered an incorrect balance!")
                                    stage = 0
                                    await asyncio.sleep(5)
                                    await botresponse.delete()
                            except:
                                await botresponse.delete()
                                botresponse = await channel.send("There has been an error whilst requesting the balance of " + mc_username + "(" + mc_uid + ").")
                                await asyncio.sleep(5)
                                await botresponse.delete()
                        except:
                            await botresponse.delete()
                            botresponse = await channel.send("There has been an error whilst connecting to the database.")
                            await asyncio.sleep(5)
                            await botresponse.delete()
                    except asyncio.TimeoutError:
                        await botresponse.delete()
                        botresponse = await channel.send("Timed out!")
                        await asyncio.sleep(10)
                        await botresponse.delete()
            except:
                botresponse = await channel.send("There has been an error whilst requesting the UUID of " + mc_username + " from Mojang.")
                stage = 0
                await asyncio.sleep(5)
                await botresponse.delete()

#============================================================================================================#

def setup(client):
    client.add_cog(Verify(client))
    print(str(datetime.datetime.now()) + " | Initialized cogs.Verify")
