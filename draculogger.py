#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import datetime

# DracuLogger. Because every other logging module seems to be crap.

def filecheck():
    try:
        # File is already existing
        file_log = open("/var/www/html/dracula/" + str(datetime.date.today()) + ".md", "r")
        file_log.close()
    except:
        # File is not existing, creating Markdown head
        file_log = open("/var/www/html/dracula/" + str(datetime.date.today()) + ".md", "w")
        file_log.write("| Time | Type | Content |\n| :------------- | :------------- | :------------- |\n")
        file_log.close()

def noescape(content):
    content = content.replace("\r", " ")
    content = content.replace("\n", " ")
    return content

def this(content):
    # Logging to the console
    print(str(datetime.datetime.now()) + " | " + str(content))
    # Checking if file exists
    filecheck()
    # Removing newlines from content
    content = noescape(str(content))
    # Logging to file
    file_log = open("/var/www/html/dracula/" + str(datetime.date.today()) + ".md", "a")
    file_log.write("| " + str(datetime.datetime.now().time()) + " | | " + str(content) + " |\n")
    file_log.close()

def more(type, content):
    # Logging to the console
    print(str(datetime.datetime.now()) + " | " + str(type) + " | " + str(content))
    # Checking if file exists
    filecheck()
    # Removing newlines from content
    content = noescape(str(content))
    # Logging to file
    file_log = open("/var/www/html/dracula/" + str(datetime.date.today()) + ".md", "a")
    file_log.write("| " + str(datetime.datetime.now().time()) + " | " + str(type) + " | " + str(content) + " |\n")
    file_log.close()
