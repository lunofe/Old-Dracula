# DraculaBot ᵇʸ ᶜʰᶦᵐᵘᵗᵉ
This bot is used on the official Vampirism Server Discord to add administrative features, various commands and automations.

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

## Automations
- The bot is displaying the current amount of players on the server as the bot's "playing" status.
- When a new user joins the Discord, they will get a welcome message: *Welcome to the official Vampirism Discord Server! To get started with the Vampirism modpack take a look at https://chimute.org/vampirism. We hardly ever have to mute, kick or ban people - please don't make yourself the exception and read the rules.*
- Furthermore, the new user gets the *Member* role.
- When a user leaves the Discord, they will get a goodbye message: *We are sorry to see you go. If you want to join again, please use this link: https://discord.gg/rP8j7hA*
- Staff applications, ban appeals and player reports are posted automatically in #staff-forms

## Commands
| Command | Description | Permission (Rank, #Channel or @User) |
| ------ | ------ | ------ |
| .ping | Command to test if the bot is online. The bot will reply with _Pong!_ | Everyone |
| .role [vampire/hunter/unselect] | Sets the message author's role to Vampire, Hunter *or remove both*. | Everyone |
| .staffyes [@user] | Accepts [@user]'s staff application. Sends them the following message: _Your application has been accepted. You will hear from us shortly. In the meantime, you can take a look at this: <https://1literzinalco.github.io/vampirismpermissions/>_ | #staff-forms |
| .staffno [@user] [reason] | Rejects [@user]'s staff application. Sends them the following message: _Your application has been rejected. [reason] You can apply again in two weeks._ | #staff-forms |
| .appealyes [@user] | Accepts [@user]'s ban appeal. Sends them the following message: _Your ban appeal has been accepted. You will be unbanned within 24 hours._ | #staff-forms |
| .appealno [@user] [reason] | Rejects [@user]'s ban appeal. Sends them the following message: _Your ban appeal has been rejected. [reason] You can appeal again in two weeks._ | #staff-forms |

## Team
- [1LiterZinalco](https://github.com/1LiterZinalco)
- [KlemChri](https://github.com/KlemChri) _no longer maintaining_
