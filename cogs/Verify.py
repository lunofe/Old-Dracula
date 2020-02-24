#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os, discord, asyncio, datetime, mysql.connector, urllib.request, json
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
    async def verify(self, ctx):
        message = ctx.message
        author = message.author
        channel = message.channel

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
        print("Welcome to Verify. Please input your Minecraft username.")
        msg_mc_username = await self.client.wait_for('message', check=check(author), timeout=30)
        mc_username = str(msg_mc_username.content)
        try:
            mc_uid = urllib.request.urlopen("https://api.mojang.com/users/profiles/minecraft/" + mc_username)
            mc_uid = mc_uid.read().decode()
            mc_uid = json.loads(mc_uid)
            mc_uid = str(mc_uid["id"])

            mc_uid = mc_uid[0:8] + "-" + mc_uid[8:12] + "-" + mc_uid[12:16] + "-" + mc_uid[16:20] + "-" + mc_uid[20:32]
            print("Selected " + mc_username + " (" + mc_uid + ")")
            stage = 1
        except:
            print("There has been an error whilst requesting the unique user id of " + mc_username + " from Mojang.")
            stage = 0

        # Stage 2
        if(stage == 1):
            print("To confirm, that " + mc_username + " is your Minecraft account, enter your current balance (/money).")
            bal1 = await self.client.wait_for('message', check=check(author), timeout=30)
            bal1 = str(bal1.content)
            try:
                db = mysql.connector.connect(
                   host="mysql.apexhosting.gdn",
                   user="apexMC79157",
                   passwd="fd78b59bb2",
                   database="apexMC79157"
                )
                cursor = db.cursor()
            except:
                print("There has been an error whilst connecting to the database.")
            try:
                cursor.execute('''SELECT dollar_balance FROM accounts WHERE uid = "''' + mc_uid + '''"''')
                result = cursor.fetchall()
                result = str(result)[11:-5]
            except:
                print("There has been an error whilst requesting the balance of " + mc_username + "(" + mc_uid + ").")
            if(result == str(bal1)):
                print("Bal 1 matches")
                stage = 2
            else:
                print("Bal1 is not matching database " + bal1 + " " + str(result))
                stage = 0

            # Stage 3
            if(stage == 2):
                print("Looks good. Now change your balance by buying or selling at the shop and enter your new balance.")
                bal2 = await self.client.wait_for('message', check=check(author), timeout=30)
                bal2 = str(bal2.content)
                if(bal2 == bal1):
                    print("You need to change your balance.")
                else:
                    try:
                        db = mysql.connector.connect(
                           host="mysql.apexhosting.gdn",
                           user="apexMC79157",
                           passwd="fd78b59bb2",
                           database="apexMC79157"
                        )
                        cursor = db.cursor()
                    except:
                        print("There has been an error whilst connecting to the database.")
                    try:
                        cursor.execute('''SELECT dollar_balance FROM accounts WHERE uid = "''' + mc_uid + '''"''')
                        result = cursor.fetchall()
                        result = str(result)[11:-5]
                    except:
                        print("There has been an error whilst requesting the balance of " + mc_username + "(" + mc_uid + ").")
                    if(result == str(bal2)):
                        print("Bal 2 matches")
                        print("Verification succesful!")
                    else:
                        print("Bal2 is not matching database " + bal2 + " " + str(result))
                        stage = 0

#============================================================================================================#

def setup(client):
    client.add_cog(Verify(client))
    print(str(datetime.datetime.now()) + " | Initialized cogs.Verify")
