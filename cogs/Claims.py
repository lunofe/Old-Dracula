#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import utils, config, os, discord, asyncio, json, yaml, requests
from discord.ext import commands
from ftplib import FTP

class Claims(commands.Cog):
    def __init__(self, client):
        self.client = client

#============================================================================================================#

    @commands.command()
    async def claimupdate(self, ctx):
        bot_msg = await ctx.send("*Updating the database...*")

        ftp = FTP(config.FTP_HOST)
        ftp.login(config.FTP_NAME, config.FTP_PASS)

        await bot_msg.edit(content = "*Connection established...*")

        ftp.cwd("plugins/GriefPreventionData/ClaimData")

        # Get All Files
        files = ftp.nlst()

        i=0
        # Print out the files
        for file in files:
            ftp.retrbinary("RETR " + file ,open("/home/dracula/draculabot/claims/" + file, 'wb').write)
            i+=1
            if str(i).endswith("0"):
                await bot_msg.edit(content = "*Downloaded file {} of {}...*".format(i, len(files)))

        await bot_msg.edit(content = "*Download completed.*")
        #ftp.close()

#============================================================================================================#

    @commands.command()
    async def claim(self, ctx, input_x, input_z):
        input_x = int(input_x)
        input_z = int(input_z)
        claims = []
        results = 0

        bot_msg = await ctx.send("*Searching for claims...*")

        for filename in os.listdir("/home/dracula/draculabot/claims"):
            if filename.endswith(".yml"):
                file = open("/home/dracula/draculabot/claims/"+filename, "r")
                content = file.read()
                file.close()
                content = yaml.safe_load(content)
                content["id"] = filename.split(".")[0]
                claims.append(content)

        for claim in claims:
            dim = claim["Lesser Boundary Corner"].split(";")[0]
            x_l = int(claim["Lesser Boundary Corner"].split(";")[1])
            x_g = int(claim["Greater Boundary Corner"].split(";")[1])
            z_l = int(claim["Lesser Boundary Corner"].split(";")[3])
            z_g = int(claim["Greater Boundary Corner"].split(";")[3])

            if dim == "world": # Pretty print the dimension
                dim = "Overworld"
            elif dim == "DIM1":
                dim = "End"
            elif dim == "DIM-1":
                dim = "Nether"
            if x_l > x_g: # Sort X coords so x1 is smaller than x2
                x1 = x_g
                x2 = x_l
            else:
                x1 = x_l
                x2 = x_g
            if z_l > z_g: # Sort Z coords so z1 is smaller than z2
                z1 = z_g
                z2 = z_l
            else:
                z1 = z_l
                z2 = z_g

            if (input_x >= x1) and (input_x <= x2):
                if (input_z >= z1) and (input_z <= z2):
                    results += 1
                    owner = requests.get("https://api.mojang.com/user/profiles/{}/names".format(claim["Owner"])).json()
                    owner = owner[len(owner)-1]["name"]
                    await ctx.send("Found a claim in the **{}** owned by **``{}``** with ID **{}**".format(dim, owner, claim["id"]))

        await bot_msg.delete()
        if results == 0:
            await ctx.send(":warning: Couldn't find any claim for that coordinations. Is the database up to date?")
        else:
            await asyncio.sleep(1)
            await ctx.send("*No further results*")

#============================================================================================================#

def setup(client):
    client.add_cog(Claims(client))
    utils.log("Initialized Claims")
