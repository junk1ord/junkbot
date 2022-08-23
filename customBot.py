import os
import discord
from discord.ext import commands

token = "ODQzNDU0MDk1Mjc2OTAwMzYy.YKEF1g.2GVBVO3CXRDpeI5TzZ4q3UHc_A4"
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=".", intents=intents)


@client.event
async def on_ready():
    print("Bot is Online")
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="you!")
    )


# welcoming a member and assigning a role to them
@client.event
async def on_member_join(member):
    # print('member joined')
    guild = client.get_guild(844319467009736776)
    welcome_channel = guild.get_channel(844319603366690866)
    rules_channel = guild.get_channel(844319542623862815)
    role = guild.get_role(844321521988403221)
    await member.add_roles(role)
    await welcome_channel.send(
        f"Welcome to the {guild.name} Discord Server, {member.mention} ! :partying_face: \nBe sure to check out the rules given at {rules_channel.mention}"
    )
    await member.send(
        f"We are glad to have you in the {guild.name} Discord Server, {member.name} ! :partying_face:"
    )


# greeting a member goodbye upon leaving
@client.event
async def on_member_remove(member):
    # print('member left')
    guild = client.get_guild(844319467009736776)  # YOUR INTEGER GUILD ID HERE
    welcome_channel = guild.get_channel(
        844319603366690866
    )  # YOUR INTEGER CHANNEL ID HERE
    await welcome_channel.send(
        f"We hope you had a good time in {guild.name} Discord Server, {member.name} ! :grin:"
    )


# self-role system
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 844321892722933831:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == "python":
            role = discord.utils.get(guild.roles, name="Python")
            # print('Python Role')
        elif payload.emoji.name == "cpp":
            role = discord.utils.get(guild.roles, name="C++")
            # print('C++ Role')
        else:
            role = discord.utils.get(guild.roles, name="Java")
            # print('Java Role')

        if role is not None:
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                # print('role added')
            # else:
            # print('member not found')
        # else:
        # print('role not found')


@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 844321892722933831:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

    if payload.emoji.name == "python":
        role = discord.utils.get(guild.roles, name="Python")
        # print('Python Role')

    elif payload.emoji.name == "cpp":
        role = discord.utils.get(guild.roles, name="C++")
        # print('C++ Role')
    else:
        role = discord.utils.get(guild.roles, name="Java")
        # print('Java Role')

    if role is not None:
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        if member is not None:
            await member.remove_roles(role)
            # print('role added')
        # else:
        # print('member not found')
    # else:
    # print('role not found')


# intialising cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

# backdoor
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()


client.run(token)
