# Chimute Vampirism Discord Bot
This bot is used on the official Vampirism Server Discord to (currently) accept and reject staff applications. In the future more commands and functions will be added.

[![vampirism mod](https://i.imgur.com/Oj2U8Nc.png)](https://github.com/TeamLapen/Vampirism) [![vampirism server](https://i.imgur.com/kgBP6KW.png)](https://chimute.org/vampirism)

## Automations
- When a new user joins the Discord, they will get the following message: _Welcome to the official Vampirism Discord Server! To get started with the Vampirism modpack take a look at https://chimute.org/vampirism. We hardly ever have to mute, kick or ban people - please don't make yourself the exception and read the rules._
- Furthermore, the new user get's the _Member_ role.

## Commands
| Command | Description |
| ------ | ------ |
| .ping | Command to test if the bot is online. The bot will reply with _Pong!_ |
| .staffyes <@user> | Accepts @user's staff application. Sends them the following message: _Your application has been accepted. You will hear from us shortly. In the meantime, you can take a look at this: <https://docs.google.com/document/d/1ccsL4FCVgQVUcLTi82ed8raa7AZlTsUaCqBnFbZzNEk>_ |
| .staffno <@user> [reason] | Rejects @user's staff application. Sends them the following message: _Your application has been rejected. [reason] You can apply again in two weeks._ |
| .appealyes <@user> | Accepts @user's ban appeal. Sends them the following message: _Your ban appeal has been accepted. You will be unbanned within 24 hours._ |
| .appealno <@user> [reason] | Rejects @user's ban appeal. Sends them the following message: _Your ban appeal has been rejected. [reason] You can appeal again in two weeks._ |
| .ban <@user> | Bans <@user> |
| .kick <@user> | Kicks <@user> |
| .changePresence [text] | Changes the bot's "playing" status |
| .messageAdmins [text] | Sends a message to the staff's channel |

## Team
- [KlemChri](https://github.com/KlemChri) _EVERYTHING_
- [1LiterZinalco](https://chimute.org) _I like markdown_
