#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import datetime, asyncio

#============================================================================================================#

# Experimental permission system
def check_permission(executor):
    staff = [
        267633670532104193, # 1LiterZinalco
        414852953191612417, # Piklach
        270258305346043905  # Pendragon
    ]
    if executor in staff:
        return True
    else:
        return False

async def no_permission(ctx, seconds):
    await ctx.message.delete()
    botresponse = await ctx.send(":warning: No permission")
    await asyncio.sleep(seconds)
    await botresponse.delete()

#============================================================================================================#

# Checking if log file already exists and if not, creating one.
def checkfile(id):
    if(id == 0):
        # Regular log
        try:
            # File is already existing
            file_log = open("/var/www/html/dracula/" + str(datetime.date.today()) + ".md", "r")
            file_log.close()
        except:
            # File is not existing, creating Markdown head
            file_log = open("/var/www/html/dracula/" + str(datetime.date.today()) + ".md", "w")
            file_log.write("| Time | Channel | Content |\n| :------------- | :------------- | :------------- |\n")
            file_log.close()
    else:
        # Debug log
        try:
            # File is already existing
            file_log = open("/var/www/html/dracula/debug.md", "r")
            file_log.close()
        except:
            # File is not existing, creating Markdown head
            file_log = open("/var/www/html/dracula/debug.md", "w")
            file_log.write("| Datetime | Content |\n| :------------- | :------------- |\n")
            file_log.close()

#============================================================================================================#

# Removing formatting that makes the log look ugly
def format(content):
    content = content.replace("\r", " ")
    content = content.replace("\n", " ")
    return content

#============================================================================================================#

# Custom logging module. Because every other logging module seems to be crap.
def log(*args):
    if(len(args) == 1):
        # Logging without channel
        content = format(args[0]) # Removing formatting that makes the log look ugly
        print("{} | {}".format(str(datetime.datetime.now()), content))
        checkfile(0) # Checking if log file already exists and if not, creating one.
        # Writing to file
        file_log = open("/var/www/html/dracula/" + str(datetime.date.today()) + ".md", "a")
        #file_log.write("| " + str(datetime.datetime.now().time()) + " | | " + content + " |\n")
        file_log.write("| {} | | {} |\n".format(str(datetime.datetime.now().time()), content))
        file_log.close()
    elif(len(args) == 2):
        # Logging with channel
        if(args[0] != "DEBUG"):
            # Regular log
            content = format(args[1]) # Removing formatting that makes the log look ugly
            print("{} | {} | {}".format(str(datetime.datetime.now()), args[0], content))
            checkfile(0) # Checking if log file already exists and if not, creating one.
            # Writing to file
            file_log = open("/var/www/html/dracula/" + str(datetime.date.today()) + ".md", "a")
            #file_log.write("| " + str(datetime.datetime.now().time()) + " | " + args[0] + " | " + args[1] + " |\n")
            file_log.write("| {} | {} | {} |\n".format(str(datetime.datetime.now().time()), args[0], content))
            file_log.close()
        else:
            # Debug log
            content = format(args[1]) # Removing formatting that makes the log look ugly
            checkfile(1) # Checking if log file already exists and if not, creating one.
            # Writing to file
            file_log = open("/var/www/html/dracula/debug.md", "a")
            #file_log.write("| " + str(datetime.datetime.now()).replace(" ", "_") + " | " + args[1] + " |\n")
            file_log.write("| {} | {} |".format(str(datetime.datetime.now()).replace(" ", "_"), args[1]))
            file_log.close()
    else: # Logging Error
        print("There has been an error while logging.")
