# junkbot
Discord is a VoIP, instant messaging and digital distribution platform designed for creating communities. Users communicate with voice calls, video calls, text messaging, media and files in private chats or as part of communities called "servers". Servers are a collection of persistent chat rooms and voice chat channels. Discord runs on Windows, macOS, Android, iOS, iPadOS, Linux, and in 
b browsers. As of December 2020, the service has over 140 million monthly active users.

`discord.py` is a modern, easy to use, feature-rich, and async ready API wrapper for Discord. It’s key features are:

- Modern Pythonic API using async/await syntax
- Sane rate limit handling that prevents 429s
- Implements the entire Discord API
- Command extension to aid with bot creation
- Easy to use with an object oriented design
- Optimised for both speed and memory

---

For the purpose of this project, I extensively worked on the discord package. With it, I have created a discord moderation bot, which as the name suggests, moderates a particular server (that is, the one which in which this has been invited to). The functionalities added to the bot are:

1. Welcoming a new user and assigning a default role to them
2. Greeting the user upon their departure from the server
3. Helping them assign custom roles with the help of message reactions and subsequently provide them access to the role-specific channels
4. Kicking a member from the server with a custom reason, the power of which is available only to those with the Moderator role.
5. Banning and unbanning a member from the server with a custom reason, the power of which is available only to those with the Moderator role.
6. Deleting the messages sent by any user, with the choice of deleting multiple quantity of messages

--- 

I also implemented the concept of cogs in the bot script. There comes a point in your bot’s development when you want to organize a collection of commands, listeners, and some state into one class. Cogs allow you to do just that. I bifurcated the moderator commands and the fun commands under two different cogs.

---

The architecture of the Bot is therefore as follows:

```
|   customBot.py
\---cogs
        FunCommands.py
        Moderator.py
```
