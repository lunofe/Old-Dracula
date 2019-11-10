#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os, discord, asyncio, datetime, dotenv
from discord.ext import commands
from dotenv import load_dotenv
from cogs import MessageHandler, Moderation, Automation, ServerRole, Tools, OnReady, MailCheck

##############################################################################################################
### Initial stuff ############################################################################################
##############################################################################################################

# Loading the configuration
print(str(str(datetime.datetime.now())) + " | Initialization...")
load_dotenv()

# Settings the bot's token
TOKEN = os.getenv("BOT_TOKEN")

# Setting the bot's command prefix
client = commands.Bot(command_prefix = ".")

# Removing the standard 'help' command
client.remove_command("help")

# Loading Cogs:
client.load_extension("cogs.OnReady")           #on_ready event
client.load_extension("cogs.MessageHandler")    #Message and Command handling
client.load_extension("cogs.Tools")             #For tools like .ping
client.load_extension("cogs.Automation")        #Listeners
client.load_extension("cogs.Moderation")        #Admin commands
client.load_extension("cogs.ServerRole")        #Role command
client.load_extension("cogs.MailCheck")         #Checking mails

# Starting the Bot
client.run(TOKEN)
