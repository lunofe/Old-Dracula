# o     o                        o               .oPYo.                                    .oPYo.          o
# 8     8                                        8                                         8   `8          8
# 8     8 .oPYo. ooYoYo. .oPYo. o8 oPYo. .oPYo.  `Yooo. .oPYo. oPYo. o    o .oPYo. oPYo.  o8YooP' .oPYo.  o8P
# `b   d' .oooo8 8' 8  8 8    8  8 8  `' 8oooo8      `8 8oooo8 8  `' Y.  .P 8oooo8 8  `'   8   `b 8    8   8
#  `b d'  8    8 8  8  8 8    8  8 8     8.           8 8.     8     `b..d' 8.     8       8    8 8    8   8
#   `8'   `YooP8 8  8  8 8YooP'  8 8     `Yooo'  `YooP' `Yooo' 8      `YP'  `Yooo' 8       8oooP' `YooP'   8
# :::..::::.....:..:..:..8 ....::....:::::.....::::.....::.....:..::::::...:::.....:..:::::::......::.....:::.
# :::::::::::::::::::::::8 :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::..:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import discord, asyncio
from discord.ext import commands
from cogs import Moderation, Automation, ServerRole, Tools
from keep_alive import keep_alive

##############################################################################################################
### Initial stuff ############################################################################################
##############################################################################################################

# Settings the bot's token
TOKEN = ""

# Setting the bot's command prefix
client = commands.Bot(command_prefix = ".")

# Removing the standard 'help' command
client.remove_command("help")

# Loading Cogs:
client.load_extension("cogs.MessageHandler")    # Message and command handling
client.load_extension("cogs.Moderation")        # Admin commands
client.load_extension("cogs.Automation")        # Listeners for automations
client.load_extension("cogs.ServerRole")        # Role command
client.load_extension("cogs.Tools")             # For tools like ping
client.load_extension("cogs.OnReady")           # on_ready event

# Running the web server
keep_alive()

# Starting the Bot
client.run(TOKEN)
