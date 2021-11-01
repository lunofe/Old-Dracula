#    oooooooooo.                                            oooo            oooooooooo.                .
#    `888'   `Y8b                                           `888            `888'   `Y8b             .o8
#     888      888 oooo d8b  .oooo.    .ooooo.  oooo  oooo   888   .oooo.    888     888  .ooooo.  .o888oo
#     888      888 `888""8P `P  )88b  d88' `"Y8 `888  `888   888  `P  )88b   888oooo888' d88' `88b   888
#     888      888  888      .oP"888  888        888   888   888   .oP"888   888    `88b 888   888   888
#     888     d88'  888     d8(  888  888   .o8  888   888   888  d8(  888   888    .88P 888   888   888 .
#    o888bood8P'   d888b    `Y888""8o `Y8bod8P'  `V88V"V8P' o888o `Y888""8o o888bood8P'  `Y8bod8P'   "888"
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import utils, config, discord
from discord.ext import commands

class Embeds(commands.Cog):
    def __init__(self, client):
        self.client = client

#============================================================================================================#

    @commands.command()
    async def embed(self, ctx, arg):
        if ctx.message.author.id in config.STAFF:
            try:
                await ctx.message.delete()
            except:
                pass
            if arg == "rules":
                file = discord.File(open("/home/dracula/draculabot/welcome.png", "rb"))
                embed=discord.Embed(title="**Get started**", description="Get one of our official modpacks from Technic Launcher or CurseForge (formerly the Twitch App) that's always up-to-date or get a list of the current mods and compile the modpack on your own!  For an install guide, simply click on your choice below!\n\n[**Technic Launcher**](https://vampirism.co/install-technic/)\nAlways up-to-date and the easiest choice, if you just want to play on our server.\n\n[**CurseForge**](https://vampirism.co/install-curseforge/)\nFormerly known as the \"Twitch App\", this launcher is also always up-to-date and easy to use.\n\n[**Get the modlist**](https://vampirism.co/install-manually/)\nYou know what you're doing? Then this might be the right choice for you.\n\n**How do I apply to become a staff member, report a player or appeal my ban?**\nVisit [our website](https://vampirism.co/) to find out more.", color=0x620382)
                embed.set_thumbnail(url="https://static.wikia.nocookie.net/minecraft_de_gamepedia/images/d/df/Werkbank.png/revision/latest/scale-to-width-down/512")
                await ctx.send(file=file, embed=embed)
                file = discord.File(open("/home/dracula/draculabot/discord_rules.png", "rb"))
                await ctx.send(content="** **\n\n** **", file=file)
                embed=discord.Embed(title="Treat everyone with respect. Absolutely no harassment, sexism, racism, hate speech, strong/derogatory language, witch hunting or any other discrimination will be tolerated.", color=0x5865F2)
                await ctx.send(embed=embed)
                embed=discord.Embed(title="Be civil and use common sense. If you do something that's not explicitly prohibited by the rules, but we think isn't okay nonetheless, we'll still take actions as mentioned further down below.", color=0x5865F2)
                await ctx.send(embed=embed)
                embed=discord.Embed(title="Keep things family friendly. No NSFW or obscene content. This includes but is not limited to text, images, or links featuring nudity, sex, hard violence, or other graphically disturbing content.", color=0x5865F2)
                await ctx.send(embed=embed)
                embed=discord.Embed(title="No spam or self-promotion (server invites, advertisements, etc) without permission from a staff member. This includes DMing fellow members.", color=0x5865F2)
                await ctx.send(embed=embed)
                embed=discord.Embed(title="Speak English in public chats. Vampirism's community is spread all over the world and we want that everyone can be a part of it.", color=0x5865F2)
                await ctx.send(embed=embed)
                embed=discord.Embed(title="If you see something against the rules or something that makes you feel unsafe, message staff immediately. We want this server to be a welcoming space!", color=0x5865F2)
                await ctx.send(embed=embed)
                embed=discord.Embed(title="Breaking any of these rules will result in your message(s) being deleted, a temporary mute, a warning (multiple will lead to bans), a temporary ban or a permanent ban.", color=0x5865F2)
                await ctx.send(embed=embed)
            elif arg == "roles":
                embed=discord.Embed(title="Races", description="Show other people what race you're playing as on the server. Please note that your selection must actually represent the truth.")
                embed.add_field(name="<:vampire:810192589222445067> for Vampire", value="** **", inline=True)
                embed.add_field(name="<:hunter:810192589194002512> for Hunter", value="** **", inline=True)
                embed.add_field(name="<:human:810193732703486032> for Human", value="** **", inline=True)
                await ctx.send(embed=embed)
                embed=discord.Embed(title="Notifications", description="@ everyone is only being used for big and important announcements - if you're only interested in those, you don't need to do anything else. But if you want to receive all notifications instead, join the NotificationGang by clicking the bell.")
                await ctx.send(embed=embed)
            elif arg == "communities":
                embed=discord.Embed(title="Over time, a number of nations, alliances, cities, cults, etc. have emerged on this server. Some have already been around for years, some perhaps only for weeks. This channel is dedicated to show off these player-made communities.", description="If you want your community to appear here, [learn more](https://vampirism.co/communities/). See also: [Disclaimer](https://vampirism.co/communities-disclaimer/)")
                embed.set_footer(text="Data is provided by the communities and does not represent the opinion of the staff team.")
                await ctx.send(embed=embed)
                await ctx.send("** **")
                embed=discord.Embed(title="Vampire Empire", description="The Vampire Empire is the biggest union of vampires from across the server. Officially re-branded on January 31 of 2020 with the election of our Lord S_olace, we strive for equality amongst our vampire brethren.", color=0x8A1EA8)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/662771233598734386/813413990301433876/unknown.png")
                embed.add_field(name="Government Type", value="Democratic Oligarchy", inline=True)
                embed.add_field(name="Discord", value="[discord.gg/XUQEsJ876S](https://discord.gg/XUQEsJ876S)", inline=True)
                embed.add_field(name="Website", value="[vampire.batcave.net](http://vampire.batcave.net)", inline=True)
                embed.add_field(name="Leaders", value="<@306989884323790850> (Queen)\n<@335510743271211009> (Prince of Foreign Affairs)\n<@599843402070360064> (Princess of Internal Affairs)\n<@272847951213101067> (Princess of Architecture)\n<@599344040051212298> (Prince of War)", inline=False)
                await ctx.send(embed=embed)
                embed=discord.Embed(title="Democratic Hunter Empire", description="The Democratic Hunter Empire (DHE) is the original Hunter Faction established after the first Hunter elections on 4th of May, 2019, by the founding father ThugPug43, and is the largest organized group of Vampire Hunters on the server.", color=0x5555FF)
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/564260757987131426/810523553019199538/image0.png")
                embed.add_field(name="Government Type", value="Democracy", inline=True)
                embed.add_field(name="Current Government", value="<@562746047596593163> (Imperator)\n<@531969884964257793> (Consul)\n<@644336378842316803> (Consul)", inline=True)
                embed.add_field(name="Previous Election", value="January 1st, 2021 - January 7th, 2021", inline=True)
                embed.add_field(name="Next Election", value="June 1st, 2021 - June 7th, 2021", inline=True)
                embed.add_field(name="Discord", value="[discord.gg/FpPjcZt](https://discord.gg/FpPjcZt)", inline=True)
                embed.add_field(name="Website", value="[dhe.estate](https://dhe.estate)", inline=True)
                await ctx.send(embed=embed)
            elif arg == "sample":
                embed=discord.Embed(title="My Great Empire", description="This is a short description with a maximum length of 300 characters that you can use to tell players about your community. It can be short, or a bit longer like this. 300 characters are actually more than enough if you ask me. And isn't that banner lovely?")
                embed.set_thumbnail(url="https://i.imgur.com/Rt9mjBL.png")
                embed.add_field(name="Government Form", value="Democracy ", inline=True)
                embed.add_field(name="Current Government", value="Me\nMyself\n& I", inline=True)
                embed.add_field(name="Previous Election", value="1 January, 2021", inline=True)
                embed.add_field(name="Next Election", value="1 June, 2021", inline=True)
                embed.add_field(name="Discord", value="[https://discord.gg/abcdef](https://discord.gg/FpPjcZt)", inline=True)
                embed.add_field(name="Website", value="[https://example.com](https://dhe.estate)", inline=True)
                await ctx.send(embed=embed)
            else:
                channel = self.client.get_channel(564783779474833431)

                submission = arg.split("§§")

                if len(submission) == 11:
                    embed=discord.Embed(title=submission[0], description="{} years old, {}".format(submission[1], submission[2]))
                    embed.add_field(name="Minecraft username", value="``{}``".format(submission[3]), inline=True)
                    embed.add_field(name="Discord#Tag", value="``{}``".format(submission[4]), inline=True)
                    embed.add_field(name="E-mail", value="``{}``".format(submission[5]), inline=True)
                    embed.add_field(name="Do you have experience as staff?", value=submission[6], inline=False)
                    embed.add_field(name="Why do you want to be staff?", value=submission[7], inline=False)
                    embed.add_field(name="Why should you be chosen instead of someone else?", value=submission[8], inline=False)
                    embed.add_field(name="Do you have any issues with the current staff team?", value=submission[9], inline=False)
                    embed.add_field(name="How many hours per week can you contribute?", value=submission[10], inline=False)
                    submission_length = len(submission[6].split()) + len(submission[7].split()) + len(submission[8].split())
                    embed.set_footer(text="{} words".format(submission_length))
                    if submission_length > 50:
                        bot_msg = await channel.send(content="**STAFF APPLICATION** @everyone", embed=embed)
                    else:
                        bot_msg = await channel.send(content="**STAFF APP-**...LI...CATION? *I guess? Pretty short application, duh*", embed=embed)
                    await bot_msg.add_reaction("<:vote_yes:601899059417972737>")
                    await bot_msg.add_reaction("<:vote_no:601898704231989259>")
                # Ban appeals
                elif len(submission) == 4:
                    embed=discord.Embed(title=" ")
                    embed.add_field(name="Minecraft username", value="``{}``".format(submission[0]), inline=True)
                    embed.add_field(name="Contact", value="``{}``".format(submission[1]), inline=True)
                    embed.add_field(name="More about your ban", value=submission[2], inline=False)
                    embed.add_field(name="Why should you be unbanned?", value=submission[3], inline=False)
                    submission_length = len(submission[2].split()) + len(submission[3].split())
                    embed.set_footer(text="{} words".format(submission_length))
                    if submission_length > 50:
                        bot_msg = await channel.send(content="**BAN APPEAL** @everyone", embed=embed)
                    else:
                        bot_msg = await channel.send(content="**BAN APP-**...eal? *I guess? Pretty short, duh*", embed=embed)
                    await bot_msg.add_reaction("<:vote_yes:601899059417972737>")
                    await bot_msg.add_reaction("<:vote_no:601898704231989259>")
                # Player reports
                elif len(submission) == 3:
                    embed=discord.Embed(title=" ", description=submission[2])
                    if((len(submission[0]) != 0) and (len(submission[1]) != 0)):
                        embed.add_field(name="Report by", value="``{}``".format(submission[0]), inline=True)
                        embed.add_field(name="Contact", value="``{}``".format(submission[1]), inline=True)
                    await channel.send(content="**PLAYER REPORT**", embed=embed)

#============================================================================================================#

def setup(client):
    client.add_cog(Embeds(client))
    utils.log("Initialized Embeds")
