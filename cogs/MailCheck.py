# o     o                        o               .oPYo.                                    .oPYo.          o
# 8     8                                        8                                         8   `8          8
# 8     8 .oPYo. ooYoYo. .oPYo. o8 oPYo. .oPYo.  `Yooo. .oPYo. oPYo. o    o .oPYo. oPYo.  o8YooP' .oPYo.  o8P
# `b   d' .oooo8 8' 8  8 8    8  8 8  `' 8oooo8      `8 8oooo8 8  `' Y.  .P 8oooo8 8  `'   8   `b 8    8   8
#  `b d'  8    8 8  8  8 8    8  8 8     8.           8 8.     8     `b..d' 8.     8       8    8 8    8   8
#   `8'   `YooP8 8  8  8 8YooP'  8 8     `Yooo'  `YooP' `Yooo' 8      `YP'  `Yooo' 8       8oooP' `YooP'   8
# :::..::::.....:..:..:..8 ....::....:::::.....::::.....::.....:..::::::...:::.....:..:::::::......::.....:::.
# :::::::::::::::::::::::8 :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::..:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import discord
from discord.ext import commands
from discord import User
import email, imaplib, asyncio, time
from threading import Thread

class MailCheck(commands.Cog):

    def __init__(self, client):
        self.client = client
        self._last_member = None


    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.client.get_channel(564783779474833431)

        username = ""
        password = ""
        while True:
            mail = imaplib.IMAP4_SSL("imap.ionos.de")
            mail.login(username, password)

            mail.select("INBOX")
            result, data = mail.uid("search", None, "ALL")
            inbox_item_list = data[0].split()

            last_mail_uid_str = data[0].decode('UTF-8').split(" ")
            last_mail_uid = int(last_mail_uid_str[-1])

            lastfile = open("last.txt",'r')
            last_edited_uid = int(lastfile.read())
            if last_mail_uid == last_edited_uid:
                print("[Mail] No updates ({}".format(time.strftime("%H")) + "h)")
            else:
                print("{}, {}".format(last_mail_uid, last_edited_uid))
                diff = last_mail_uid-last_edited_uid
                while not(diff == 0):
                    current_item = inbox_item_list[(diff-(2*diff))]
                    result2, email_data = mail.uid("fetch", current_item, "(RFC822)")
                    raw_email = email_data[0][1].decode("utf-8")

                    email_message = email.message_from_string(raw_email)


                    mail_body = email_message.get_payload()
                    mail_body = mail_body.replace("\r", "")
                    mail_body = mail_body.replace("\n\n", "")

                    contentlist = mail_body.split("§§")
                    if not(email_message["Content-Transfer-Encoding"] == "8bit"):
                        await channel.send("I got a {} but I cant handle it. Please check it manualy.".format(email_message["Subject"].replace("_", " ")))
                    elif email_message["Subject"].lower() == "staff_apply":
                        await channel.send("**" + contentlist[0] + "'s STAFF APPLICATION** @here\n\n__Minecraft Username:__ ``" + contentlist[1] + "``    __Discord#Tag:__ ``" + contentlist[2] + "``    __Email:__ ``" + contentlist[3] + "``\n** **")
                        await channel.send("__◆ Do you have experience as staff?__\n" + contentlist[4])
                        await channel.send("__◆ Why do you want to be staff?__\n" + contentlist[5])
                        await channel.send("__◆ Why should you be chosen instead of someone else?__\n" + contentlist[6] + "\n** **")
                        await channel.send("__◆ Do you have any issues with the current staff team?__ \n" + contentlist[7] + "\n__◆ How many hours per week can you contribute?__ \n" + contentlist[8] + " hours")
                    elif email_message["Subject"].lower() == "ban_appeal":
                        await channel.send("**BAN APPEAL** @here\n\n__Minecraft Username:__ " + contentlist[0] + "    __Contact:__ " + contentlist[1] + "\n\n__◆ More about your ban__\n" + contentlist[2] + "\n__◆ Why should you be unbanned?__\n" + contentlist[3])
                    elif email_message["Subject"].lower() == "player_report":
                        await channel.send("**PLAYER REPORT** @here\n\n__Report by:__ ``" + contentlist[0] + "``    __Contact:__ ``" + contentlist[1] + "``\n\n" + contentlist[2])
                    else:
                        await channel.send("I got a new email but i dont know how to handle it {}:".format(email_message["From"]) + email_message.get_payload())
                    diff = diff - 1

            lastfile.close()
            lastfile = open("last.txt","w")
            lastfile.write(last_mail_uid_str[-1])
            lastfile.close()
            await asyncio.sleep(3600)

def setup(client):
    client.add_cog(MailCheck(client))
    print("[Cog] MailCheck added")
