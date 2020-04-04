import discord
from discord.ext import commands
from discord.utils import find
import os

client = commands.Bot(command_prefix = '?')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('waving | ?help'))
    print('No one`s arround to help')

@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello **{}**! My name is **Wave**, im an utility bot made by Ransomwave#8880! Type `?help` for a list fo commands! -- https://cdn.discordapp.com/attachments/652905724443361300/688321317992529929/MOSHED-2020-3-13-14-42-34.jpg'.format(guild.name))

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def help(ctx):

    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title="Bot prefix: ?",
        description="This is a list of commands that the bot currently has"
    )

    embed.set_author(name="Wave Bot Commands", icon_url="https://cdn.discordapp.com/attachments/652905724443361300/688321317992529929/MOSHED-2020-3-13-14-42-34.jpg")
    embed.set_image(url="https://cdn.discordapp.com/attachments/652905724443361300/688321317992529929/MOSHED-2020-3-13-14-42-34.jpg")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/652905724443361300/688321317992529929/MOSHED-2020-3-13-14-42-34.jpg")
    embed.add_field(name="?ping", value="This has the bot say pong.", inline=False)
    embed.add_field(name="?help", value="Shows this message.", inline=False)
    embed.add_field(name="?invite", value="Shows the invite link for the bot.", inline=False)
    embed.add_field(name="?clear (number)", value="Deletes a determined amount of messages", inline=False)
    embed.add_field(name="?credits", value="Shows the owner's social media and credits.", inline=False)
    embed.add_field(name="?ban @user (reason)", value="Bans a member.", inline=True)
    embed.add_field(name="?kick @user (reason)", value="Kicks a member.", inline=True)
    embed.add_field(name="Support server", value="For any further help join the support server. https://discord.gg/KT7JYzG", inline=False)
    embed.set_footer(text="Made by Ransomwave#8880 -- Ender777456")

    await ctx.send(embed=embed)

@client.command()
async def version(ctx):
    await ctx.send('Bot version is currently `BETA 0.0.9`')

@client.command()
async def credits(ctx):
    await ctx.send('Bot made with python 3.8.2 - Scripted by Ender777456 (https://www.Youtube.com/Ender777456), **Thank you for using!**')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, * , reason=None):
 await member.kick(reason=reason)

@client.command()
async def say(ctx, *, something):
    """Say something!"""
    if something is None:
        await ctx.send("What do you want to say?")
        return

    await ctx.send(f"{something}")

@client.command(aliases=['resume','stop', 'summon', 'join', 'music'])
async def play(ctx):
    await ctx.send('Sorry m8, we don`t do that.')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, * , reason=None):
 await member.ban(reason=reason)

@client.command(aliases=['delete','purge'])
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.send('✅ `Messages deleted succefully!` ✅')

@client.command()
async def invite(ctx):
    await ctx.send('Invite me to **YOUR SERVER** with this link! 👉 https://discordapp.com/oauth2/authorize?client_id=660140130454994964&scope=bot&permissions=8')


client.run(os.environ['token'])
