# DraculaBot *by [Chimute](https://chimute.org)*
This bot is used on the official Vampirism Server Discord to add administrative features, various commands and automations.

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

## Automations
- The bot is displaying the current amount of players on the server as the bots "playing" status.
- When a new user joins the Discord, they will get a welcome message.
- Furthermore, the new user gets the *Member* role.
- When a user leaves the Discord, they will get a goodbye message.
- Staff applications, ban appeals and player reports are posted automatically in #staff-forms

## Commands
| Command | Description | Permission (Rank, #Channel or @User) |
| ------ | ------ | ------ |
| .ping | Command to test if the bot is online. The bot will reply with some system information. | Everyone |
| .faction [vampire/hunter/human] | Sets the executors role to Vampire, Hunter or Human *(default member*. | Everyone |
| .notificationgang [join/leave] | Adds or removes the executor from receiving not top-priority notifications. | Everyone |
| .staffyes [@user] | Accepts [@user]s staff application. | #staff-forms |
| .staffno [@user] [reason] | Rejects [@user]s staff application. | #staff-forms |
| .appealyes [@user] | Accepts [@user]s ban appeal. | #staff-forms |
| .appealno [@user] [reason] | Rejects [@user]s ban appeal. | #staff-forms |

## Config file (.env)
```
BOT_TOKEN=
IMAP_HOST=
IMAP_ACC=
IMAP_PASS=
DB_HOST=
DB_ACC=
DB_PASS=
DB_NAME=
```


## Team
- [1LiterZinalco](https://github.com/1LiterZinalco)
- [KlemChri](https://github.com/KlemChri) _no longer maintaining_
