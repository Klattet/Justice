# A Discord bot written in Python

# Goals
- Make Discord chat moderation simple and convenient.
- Offer novelty features to spice up the chatroom experience.

# Background
This was one of my first projects in Python that I started around 2017. I used it as a hobby project to teach myself programming. However, all the code in this repo is relatively new. I have returned to this project to rewrite it several times, to see how my programming experience has improved. This iteration is still missing some functions that I have implemented before, and I will add more functions later.\
\
Do not ask me to publish the previous iterations of this project, it would be too embarrassing. Besides, it would degenerate the training data for Copilot ;)\
\
I first used the [discord.py](https://github.com/Rapptz/discord.py) library as a wrapper for the Discord API. Due to the [end of development](https://gist.github.com/Rapptz/4a2f62751b9600a31a0d3c78100287f1) of the library (it has since resumed development), I swapped to the [pycord](https://github.com/Pycord-Development/pycord) library, which is an independent fork of [discord.py](https://github.com/Rapptz/discord.py).\
\
Then, as part of my [bachelor project](https://github.com/Klattet/StudassBot), I had to create a separate Discord bot. In that project I used [disnake](https://github.com/DisnakeDev/disnake) because it advertised more efficient memory usage, something that was valuable for the project. Since my experience with [disnake](https://github.com/DisnakeDev/disnake) was good, I decided to use it in this project as well.\
\
The name and persona of the bot is based on a character from the video game Helltaker, called [Justice](https://helltaker.fandom.com/wiki/Justice). She is one of the demons encountered as The Helltaker ventures into hell. In the game she is described as "The Awesome Demon" and is the most relaxed and chill demon in the cast. Most of the demons in the game are initially enemies, and most of them will kill The Helltaker if the player, but [Justice](https://helltaker.fandom.com/wiki/Justice) will not.\
\
The character [Justice](https://helltaker.fandom.com/wiki/Justice) is based on the myth of [Lady Justice](https://en.wikipedia.org/wiki/Lady_Justice). In reference to the saying "Justice is blind", she is also depicted as actually being blind. In the web-comic "Justice joins the team", [Justice](https://helltaker.fandom.com/wiki/Justice) is dressed as a police officer, a design that resonated well with her character being the personification of justice.\
\
Due to [Justice](https://helltaker.fandom.com/wiki/Justice)'s chill personality and design inspiration from the justice system, it seemed like a fitting persona for a moderation bot.

## Features
### Implemented
#### Novelty
- Magic 8ball - Let fate decide.

#### Utility
- Display Icon - Show one or more user or server icons.

#### Bot
- Logger - Write events to a logfile for easier debugging.
- Error - Always give a response and handle errors gracefully without crashing.
- Hot Reload - Code changes take effect without restarting.
- Rich Presence - Automatically change activity and status based on whether commands have been used recently or not.

### Work in progress
#### Novelty
- Snipe - Someone said something embarrassing and deleted their message? If you're quick, you can snipe their message and expose them.

#### Utility
- Info - Display detailed info about a user.

#### Moderation
- Ban - Permanently or temporarily banish a user from a server.

#### Bot
- Uptime - Show how long the bot has been online.

### Planned
#### Moderation
- Kick - Remove a user, but they can still come back.
- Mute - Silence a user for a length of time.
- Welcome - Automatically welcome new users to a server.

#### Bot
- Prefix - Allow individual users to choose their own prefix to interact with the bot, or allow moderators to choose prefix in their server.

## Dependencies
| Dependency | Usecase |
|---|---|
| [disnake](https://github.com/DisnakeDev/disnake) | Wrapper for the Discord API, used to send and receive information to Discord. |
| [PyYAML](https://github.com/yaml/pyyaml) | Read .yaml configuration file. |


After cloning this repo, I recommend creating a virtual environment with:
```commandline
python -m venv .venv
```
Then activating it with:
```commandline
source .venv/bin/activate
```

Run either of the commands below to install dependencies.
```commandline
pip install disnake PyYAML
```
```commandline
pip install -r requirements.txt
```
