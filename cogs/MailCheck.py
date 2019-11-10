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
from discord import User
import email, imaplib, asyncio, time
from threading import Thread

class MailCheck(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

#============================================================================================================#

    @commands.Cog.listener()
    async def on_ready(self):
        # Setting the channel to send the email to
        channel = self.client.get_channel(564783779474833431)

        # Setting the email account login
        host = os.getenv("IMAP_HOST")
        username = os.getenv("IMAP_ACC")
        password = os.getenv("IMAP_PASS")

        while True:
            # Setting the IMAP server
            mail = imaplib.IMAP4_SSL(host)
            # Logging in
            mail.login(username, password)

            # Selecting the inbox
            mail.select("INBOX")
            result, data = mail.uid("search", None, "ALL")
            inbox_item_list = data[0].split()

            # Splitting mail IDs
            last_mail_uid_str = data[0].decode('UTF-8').split(" ")
            last_mail_uid = int(last_mail_uid_str[-1])

            # Checking if ID was already processed
            lastfile = open("last.txt",'r')
            last_edited_uid = int(lastfile.read())
            if last_mail_uid == last_edited_uid:
                # If already processed:
                print(str(datetime.datetime.now()) + " | *MAIL* There is no new e-mail")
            else:
                # If new:
                print(str(datetime.datetime.now()) + " | *MAIL* Update: " + "{}, {}".format(last_mail_uid, last_edited_uid))
                diff = last_mail_uid-last_edited_uid
                while not(diff == 0):
                    current_item = inbox_item_list[(diff-(2*diff))]
                    result2, email_data = mail.uid("fetch", current_item, "(RFC822)")
                    raw_email = email_data[0][1].decode("utf-8")

                    email_message = email.message_from_string(raw_email)

                    # Get the content of the email and remove unnecessary stuff
                    mail_body = email_message.get_payload()
                    mail_body = mail_body.replace("\r", "")
                    mail_body = mail_body.replace("\n\n", "")

                    # The data is split by §§
                    contentlist = mail_body.split("§§")
                    # Handling emails which arent encoded correctly
                    if not(email_message["Content-Transfer-Encoding"] == "8bit"):
                        await channel.send("I've received an email but don't know how to handle it. Please check it manually: {}".format(email_message["Subject"].replace("_", " ")))
                    # Staff applications
                    elif email_message["Subject"].lower() == "staff_apply":
                        await channel.send("**STAFF APPLICATION** @here\n\n__Name:__ " + contentlist[0] + " (" + contentlist[1] + " y/o, " + contentlist[2] + ")\n__Minecraft Username:__ ``" + contentlist[3] + "``    __Discord#Tag:__ ``" + contentlist[4] + "``    __Email:__ ``" + contentlist[5] + "``\n** **")
                        await channel.send("__◆ Do you have experience as staff?__\n" + contentlist[6])
                        await channel.send("__◆ Why do you want to be staff?__\n" + contentlist[7])
                        await channel.send("__◆ Why should you be chosen instead of someone else?__\n" + contentlist[8] + "\n** **")
                        await channel.send("__◆ Do you have any issues with the current staff team?__ \n" + contentlist[9] + "\n__◆ How many hours per week can you contribute?__ \n" + contentlist[10] + " hours")
                    # Ban appeals
                    elif email_message["Subject"].lower() == "ban_appeal":
                        await channel.send("**BAN APPEAL** @here\n\n__Minecraft Username:__ ``" + contentlist[0] + "``    __Contact:__ ``" + contentlist[1] + "``\n\n__◆ More about your ban__\n" + contentlist[2] + "\n__◆ Why should you be unbanned?__\n" + contentlist[3])
                    # Player reports
                    elif email_message["Subject"].lower() == "player_report":
                        await channel.send("**PLAYER REPORT** @here\n\n__Report by:__ ``" + contentlist[0] + "``    __Contact:__ ``" + contentlist[1] + "``\n\n" + contentlist[2])
                    # Unknown/Error
                    else:
                        await channel.send("I've received an email but don't know how to handle it. {}:".format(email_message["From"]) + email_message.get_payload())
                    diff = diff - 1

            # Updating last processed ID
            lastfile.close()
            lastfile = open("last.txt","w")
            lastfile.write(last_mail_uid_str[-1])
            lastfile.close()

            # Sleeping for one hour
            await asyncio.sleep(3600)

#============================================================================================================#

def setup(client):
    client.add_cog(MailCheck(client))
    print(str(datetime.datetime.now()) + " | Initialized cogs.MailCheck")
