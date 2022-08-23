import discord
from discord.ext import commands

badwords = ["badword1", "badword2", "badword3", "badword4"]


class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # KICK command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @kick.error
    async def on_kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(
                f"You do not have the permission to kick any member, {ctx.author.mention} "
            )

    # BAN command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}")

    @ban.error
    async def on_ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(
                f"You do not have the permission to ban any member, {ctx.author.mention} "
            )

    # UNBAN command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return

    @unban.error
    async def on_unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(
                f"You do not have the permission to unban any member, {ctx.author.mention} "
            )

    # CLEAR MESSAGES
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount)

    @clear.error
    async def on_clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(
                f"You do not have the permission to delete messages this way, {ctx.author.mention} "
            )

    @commands.Cog.listener()
    async def on_message(self, message):
        for i in badwords:  # Go through the list of bad words;
            if i in message.content:
                await message.delete()
                await message.channel.send(
                    f"{message.author.mention} Don't use that word here!"
                )
                return  # So that it doesn't try to delete the message again.
        await self.bot.process_commands(message)


def setup(bot):
    bot.add_cog(Moderator(bot))
