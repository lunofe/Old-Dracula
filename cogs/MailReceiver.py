#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import utils, config, discord, asyncio, quopri, email, imaplib
from discord.ext import commands, tasks

class MailReceiver(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.loop.start()

#============================================================================================================#

    def cog_unload(self):
        self.loop.cancel()

#============================================================================================================#

    @tasks.loop(minutes=15.0)
    async def loop(self):
        # Setting the channel to send the email to
        channel = self.client.get_channel(564783779474833431)

        # Setting the IMAP server and logging in
        mail = imaplib.IMAP4_SSL(config.IMAP_HOST)
        mail.login(config.IMAP_ACC, config.IMAP_PASS)

        # Selecting the inbox
        mail.select("INBOX")
        result, data = mail.uid("search", None, "ALL")
        inbox_item_list = data[0].split()

        # Splitting mail IDs
        last_mail_uid_str = data[0].decode('UTF-8').split(" ")
        last_mail_uid = int(last_mail_uid_str[-1])

        # Checking if ID was already processed
        last_edited_uid = int(utils.file("r", "last.txt"))
        if last_mail_uid == last_edited_uid:
            # If already processed:
            #utils.log("E-MAILS", "There is no new e-mail")
            pass
        else:
            # If new:
            utils.log("E-MAILS", "Update: {}, {}".format(last_mail_uid, last_edited_uid))
            diff = last_mail_uid-last_edited_uid
            while not(diff == 0):
                current_item = inbox_item_list[(diff-(2*diff))]
                result2, email_data = mail.uid("fetch", current_item, "(RFC822)")
                raw_email = email_data[0][1].decode("utf-8")

                email_message = email.message_from_string(raw_email)

                # Get the content of the email decoded and remove unnecessary stuff
                mail_body = email_message.get_payload()
                if(email_message["Content-Transfer-Encoding"] != "8bit"):
                    # Fix shitty formatting
                    mail_body = quopri.decodestring(mail_body)
                    mail_body = mail_body.decode("utf-8")
                mail_body = mail_body.replace("\r", "")
                mail_body = mail_body.replace("\n\n", "")
                contentlist = mail_body.split("§§")

                # Staff applications
                if email_message["Subject"].lower() == "staff_apply":
                    embed=discord.Embed(title=contentlist[0], description="{} years old, {}".format(contentlist[1], contentlist[2])) # Color?
                    embed.add_field(name="Minecraft username", value="``{}``".format(contentlist[3]), inline=True)
                    embed.add_field(name="Discord#Tag", value="``{}``".format(contentlist[4]), inline=True)
                    embed.add_field(name="E-mail", value="``{}``".format(contentlist[5]), inline=True)
                    embed.add_field(name="Do you have experience as staff?", value=contentlist[6], inline=False)
                    embed.add_field(name="Why do you want to be staff?", value=contentlist[7], inline=False)
                    embed.add_field(name="Why should you be chosen instead of someone else?", value=contentlist[8], inline=False)
                    embed.add_field(name="Do you have any issues with the current staff team?", value=contentlist[9], inline=False)
                    embed.add_field(name="How many hours per week can you contribute?", value=contentlist[10], inline=False)
                    submission_length = len(contentlist[6].split()) + len(contentlist[7].split()) + len(contentlist[8].split())
                    embed.set_footer(text="{} words  |  ID: {}".format(submission_length, last_mail_uid))
                    if submission_length > 50:
                        botresponse = await channel.send(content="**STAFF APPLICATION** @everyone", embed=embed)
                    else:
                        botresponse = await channel.send(content="**STAFF APP-**...LI...CATION? *I guess? Pretty short application, duh*", embed=embed)
                    await botresponse.add_reaction("<:vote_yes:601899059417972737>")
                    await botresponse.add_reaction("<:vote_no:601898704231989259>")
                # Ban appeals
                elif email_message["Subject"].lower() == "ban_appeal":
                    embed=discord.Embed(title=" ") # Color?
                    embed.add_field(name="Minecraft username", value="``{}``".format(contentlist[0]), inline=True)
                    embed.add_field(name="Contact", value="``{}``".format(contentlist[1]), inline=True)
                    embed.add_field(name="More about your ban", value=contentlist[2], inline=False)
                    embed.add_field(name="Why should you be unbanned?", value=contentlist[3], inline=False)
                    submission_length = len(contentlist[2].split()) + len(contentlist[3].split())
                    embed.set_footer(text="{} words  |  ID: {}".format(submission_length, last_mail_uid))
                    if submission_length > 50:
                        botresponse = await channel.send(content="**BAN APPEAL** @everyone", embed=embed)
                    else:
                        botresponse = await channel.send(content="**BAN APP-**...eal? *I guess? Pretty short, duh*", embed=embed)
                    await botresponse.add_reaction("<:vote_yes:601899059417972737>")
                    await botresponse.add_reaction("<:vote_no:601898704231989259>")
                # Player reports
                elif email_message["Subject"].lower() == "player_report":
                    embed=discord.Embed(title=" ", description=contentlist[2]) # Color?
                    if((len(contentlist[0]) != 0) and (len(contentlist[1]) != 0)):
                        embed.add_field(name="Report by", value="``{}``".format(contentlist[0]), inline=True)
                        embed.add_field(name="Contact", value="``{}``".format(contentlist[1]), inline=True)
                    embed.set_footer(text="ID: {}".format(submission_length, last_mail_uid))
                    if submission_length > 50:
                        botresponse = await channel.send(content="**PLAYER REPORT** @everyone", embed=embed)
                    else:
                        botresponse = await channel.send(content="**PLAYER REP-**...ort? *I guess? Pretty short, duh*", embed=embed)
                # Unknown/Error
                else:
                    await channel.send("I've received an email but don't know how to handle it: {}".format(email_message["From"]) + email_message.get_payload())
                diff = diff - 1

        # Updating last processed ID
        utils.file("w", "last.txt", last_mail_uid_str[-1])

#============================================================================================================#

    @loop.before_loop
    async def before_loop(self):
        utils.log("E-MAILS", "Wating until ready...")
        await self.client.wait_until_ready()

#============================================================================================================#

def setup(client):
    client.add_cog(MailReceiver(client))
    utils.log("Initialized MailReceiver")
