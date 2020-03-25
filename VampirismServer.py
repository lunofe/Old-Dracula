#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os, discord, dotenv
import draculogger as log
from discord.ext import commands
from dotenv import load_dotenv
#from cogs import Utils, MessageHandler, OnReady, Moderation, Automation, ServerRole, Tools, MailCheck

##############################################################################################################
### Initial stuff ############################################################################################
##############################################################################################################

# Startup
log.this("STARTUP BEGIN...")
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
client = commands.Bot(command_prefix = ".")

# Removing the standard "help" command
client.remove_command("help")

# Loading Cogs:
client.load_extension("cogs.OnReady")
client.load_extension("cogs.MessageHandler")
client.load_extension("cogs.Tools")
client.load_extension("cogs.Automation")
client.load_extension("cogs.Submissions")
client.load_extension("cogs.ServerRole")
client.load_extension("cogs.MailCheck")
#client.load_extension("cogs.Verify")
#client.load_extension("cogs.Music")

# Starting the Bot
log.this("STARTUP CLEAR, RUNNING BOT")
client.run(TOKEN)
