import discord
from discord.ext import commands
from discord.utils import find
import random
import praw
import aiohttp
import asyncio
from googletrans import Translator

#discord
client = commands.Bot(command_prefix = '?')
client.remove_command('help')

#reddit api
reddit = praw.Reddit(client_id='LPnSJQpV6wzRUQ',
                     client_secret='C2IG__SgCzLuTyzAEelMQpbFj1Y',
                     user_agent='wave discord bot')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"?help | REBORN"))
    print('Wave`s running.')

#variables
waifulinks = ("https://pm1.narvii.com/6514/68b6018b1743baa6ae4fa421d57e402479233f8e_hq.jpg", "https://cdn.discordapp.com/attachments/617095061666136072/709917760511279124/da1.gif", "https://cdn.discordapp.com/attachments/617095061666136072/709740490517381220/anime-nekopara-coconut-nekopara-heterochromia-wallpaper-preview.jpg", "https://cdn.discordapp.com/attachments/617095061666136072/709026193214799954/80332574_p2_master12001.webp", "https://cdn.discordapp.com/attachments/617095061666136072/708474653756358696/Screenshot_20200329-175754_MX_Player.jpg", "https://cdn.discordapp.com/attachments/617095061666136072/707552692972814376/Screenshot_20200120-160400_MX_Player.jpg", "https://cdn.discordapp.com/attachments/617095061666136072/706951895788290058/tumblr_ptq0jxEMwM1v6bs4yo3_1280.jpg", "https://cdn.discordapp.com/attachments/617095061666136072/706837154801647626/image0.jpg", "https://cdn.discordapp.com/attachments/617095061666136072/706647983470542859/667fdef2.jpg", "https://cdn.discordapp.com/attachments/617095061666136072/706571376525443072/ezgif-2-fbe1ad005bf1.gif", "https://cdn.discordapp.com/attachments/688782992243687434/710527337556475955/5c831c437eef059a00e185bf879a9d41.png", "https://cdn.discordapp.com/attachments/700737114861469838/717436062628184084/chika.jpg", "https://cdn.discordapp.com/attachments/700737114861469838/717436067988373625/elma.png", "https://cdn.discordapp.com/attachments/700737114861469838/717436095868174346/fuhrer.jpg", "https://cdn.discordapp.com/attachments/700737114861469838/717436097335918632/JUST_MONIKA.jpg", "https://cdn.discordapp.com/attachments/700737114861469838/717436117124775977/lucoa.png", "https://cdn.discordapp.com/attachments/700737114861469838/717436098099413013/kobayashi.jpg", "https://cdn.discordapp.com/attachments/700737114861469838/717436129774796820/mai-san_S_I_M_P.jpg", "https://cdn.discordapp.com/attachments/700737114861469838/717436168358330368/neko.png", "https://cdn.discordapp.com/attachments/700737114861469838/717436189493297152/sagiri.jpg", "https://cdn.discordapp.com/attachments/700737114861469838/717436248968527972/ram.png", "https://cdn.discordapp.com/attachments/700737114861469838/717436255213715486/shigure.png", "https://cdn.discordapp.com/attachments/700737114861469838/717436256212090951/yuri.png", "https://cdn.discordapp.com/attachments/700737114861469838/717436271735209984/rem.jpg", "https://cdn.discordapp.com/attachments/700737114861469838/717436297827844196/natsuki.jpg", "https://cdn.discordapp.com/attachments/700737114861469838/717436328765030541/komisan.jpg", "https://cdn.discordapp.com/attachments/700737114861469838/717436348658614372/kanna.png", "https://cdn.discordapp.com/attachments/700737114861469838/717436357332697138/hayasaka.png", "https://cdn.discordapp.com/attachments/700737114861469838/717436398776352808/maika.png", "https://cdn.discordapp.com/attachments/700737114861469838/717436466812157983/chocola.png", "https://cdn.discordapp.com/attachments/700737114861469838/717436497665458206/emilia.png", "https://cdn.discordapp.com/attachments/700737114861469838/717436622072840292/the_diamond_waifu.png", "https://cdn.discordapp.com/attachments/693158585085067328/718116508806676480/Chiyoda_momo.jpg")
responses = ("It is certain.", "It is decidedly so.", "Without a doubt.", "Yes – definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful.")

#start things
@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('> Hello **{}**! My name is **Wave**, im an utility bot made by Ransomwave! Type **?help** for a list of commands! -- https://cdn.discordapp.com/attachments/652905724443361300/688321317992529929/MOSHED-2020-3-13-14-42-34.jpg'.format(guild.name))

@client.command()
async def ping(ctx):
        embed = discord.Embed(colour=discord.Colour.blue())

        embed.set_author(name=f"Pong! 🏓")
        embed.set_footer(text="Made by Ransomwave")

        embed.add_field(name="**Client Latency**", value=f"My ping is **{client.latency * 1000}ms**")
        await ctx.send(embed=embed)


#main command list
@client.command()
async def help(ctx):

    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title="Bot prefix: ``?``",
        description=f"Here are my commands, {ctx.author.mention}"
    )

    embed.set_author(name="Wave Bot Commands")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/652905724443361300/688321317992529929/MOSHED-2020-3-13-14-42-34.jpg")
    
    embed.add_field(name=":tools: | ?moderation", value="Lists all moderation commands.", inline=False)
    embed.add_field(name=":joy: | ?fun", value="Lists all fun commands.", inline=False)
    embed.add_field(name=":bangbang: | ?utils", value="Lists all utility commands.", inline=False)
    embed.add_field(name="<a:hug:726031053193478546> | ?idle", value="Lists all roleplay commands")
    embed.add_field(name="Useful Links", value="Add me! - https://cutt.ly/getwave\nSupport Server - https://discord.gg/TRc9ZJZ", inline=False)
    embed.set_footer(text="Made by Ransomwave")

    await ctx.send(embed=embed)

#moderation list
@client.command(aliases=["mod"])
async def moderation(ctx):

    embed = discord.Embed(
        colour=discord.Colour.blue(),
    )

    embed.set_author(name="Wave Bot Moderation Command List")
    embed.add_field(name=":small_blue_diamond: | Symbology", value="**< >** = Required Argument || **( )** = Optional Argument", inline=False)
    embed.add_field(name="?kick <@user>", value="Kicks the desired user.", inline=False)
    embed.add_field(name="?ban <@user>", value="Bans the desired user.", inline=False)
    embed.add_field(name="?warn <@user> (reason)", value="Warns the desired user in their Direct Messages.", inline=False)
    embed.add_field(name="?clear (number)", value="Deletes the desired amount of messages.", inline=False)
    embed.add_field(name="?userinfo <@user or UserID>", value="Shows useful information about the desired user.", inline=False)
    embed.set_footer(text="Made by Ransomwave")

    await ctx.send(embed=embed)

#fun list
@client.command()
async def fun(ctx):

    embed = discord.Embed(
        colour=discord.Colour.blue(),
    )

    embed.set_author(name="Wave Bot Fun Command List")
    embed.add_field(name="?waifu", value="Shows a waifu!", inline=False)
    embed.add_field(name="?meme", value="Shows a meme from r/memes!", inline=False)
    embed.add_field(name="?8ball <Question>", value="Answers a question.", inline=False)
    embed.add_field(name="?animememe", value="Shows a meme anime from r/AnimeMemes!", inline=False)
    embed.add_field(name="?slot", value="Roll a slot machine.", inline=False)
    embed.add_field(name="?howhot <@user>", value="Returns the percent of how hot is a user.", inline=False)
    embed.add_field(name="?reverse <text>", value="Reverse a text!", inline=False)
    embed.set_footer(text="Made by Ransomwave")

    await ctx.send(embed=embed)

#other commands list
@client.command()
async def utils(ctx):

    embed = discord.Embed(
        colour=discord.Colour.blue(),
    )

    embed.set_author(name="Wave Bot Utility Command List")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/652905724443361300/688321317992529929/MOSHED-2020-3-13-14-42-34.jpg")
    embed.add_field(name=":small_blue_diamond: | Symbology", value="**< >** = Required Argument || **( )** = Optional Argument", inline=False)
    embed.add_field(name="?ping", value="Shows the bot's latency (ping)", inline=False)
    embed.add_field(name="?say <message>", value="Makes the bot say the desired message.", inline=False)
    embed.add_field(name="?credits", value="Shows the owner's social media and credits.", inline=False)
    embed.add_field(name="?createchannel <name>", value="Creates a text channel with the desired name.", inline=False)
    embed.add_field(name="?createvc <name>", value="Creates a voice channel with the desired name.", inline=False)
    embed.add_field(name="?serverinfo", value="Displays useful information about the server.", inline=False)
    embed.add_field(name="?giveaway <time in seconds> <giveaway content>", value="Creates a giveaway! **(Administrator permission required!)**", inline=False)
    embed.add_field(name="?translate <text>", value="Translates a text to english.", inline=False)
    embed.add_field(name="**?invite**", value="Shows the invite link for the bot.", inline=False)
    embed.set_footer(text="Made by Ransomwave")

    await ctx.send(embed=embed)

#idle commands
@client.command()
async def idle(ctx):
    embed = discord.Embed(
        colour=discord.Colour.blue(),
    )

    embed.set_author(name="Wave Bot Idle Command List", icon_url="https://cdn.discordapp.com/attachments/652905724443361300/688321317992529929/MOSHED-2020-3-13-14-42-34.jpg")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/652905724443361300/688321317992529929/MOSHED-2020-3-13-14-42-34.jpg")
    embed.add_field(name=":small_blue_diamond: | Symbology", value="**< >** = Required Argument || **( )** = Optional Argument", inline=False)
    embed.add_field(name="?kiss <@user>", value="Makes you kiss someone o///o", inline=False)
    embed.add_field(name="?pat <@user>", value="Makes you pat someone", inline=False)
    embed.add_field(name="?hug <@user>", value="Makes you hug someone :3", inline=False)
    embed.add_field(name="?slap <@user>", value="Makes you slap someone", inline=False)
    embed.set_footer(text="Made by Ransomwave")

    await ctx.send(embed=embed)


@client.command()
async def credits(ctx):
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title="Credits",
        description="Bot's credits"
    )

    embed.set_author(name="Wave", icon_url="https://cdn.discordapp.com/attachments/652905724443361300/688321317992529929/MOSHED-2020-3-13-14-42-34.jpg")
    embed.add_field(name="**__Made by Ransomwave__**", value="Instagram: https://instagram.com/ransomwave.mp3\nTwitter: https://twitter.com/ransomwave_mp3", inline=False)
    embed.add_field(name="**Made with Python 3.8.2**", value="https://python.org", inline=False)
    embed.add_field(name="**Thanks to Ícaro Kauê for helping with the bot developement!**", value="His youtube channel: https://www.youtube.com/channel/UCbDA1i2cmpE8q5CCyky-RqA", inline=False)

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, * , reason=None):
 await member.kick(reason=reason)
 await ctx.send(f"**{member.name}** has been **kicked**!  <a:BlobBanHammer:716268575064588288>")

@client.command()
async def say(ctx, *, something):
    log = client.get_channel(736181503301648394)
    embed = discord.Embed(colour=discord.Colour.red())
    embed.description=f"{something}"
    
    await ctx.message.delete()

    await ctx.send(embed=embed)
    await log.send(f"Command:'?say'\nUser:**{ctx.author.name}** **({ctx.author.id})**\n Guild:`{ctx.guild.name}`\nMessage:")
    await log.send(embed=embed)

@client.command()
async def userinfo(ctx, member: discord.Member):

        roles = [role for role in member.roles]

        embed = discord.Embed(colour=member.color)
        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="Made by Ransomwave")

        embed.add_field(name="**ID:**", value=member.id)
        embed.add_field(name="**Server name:**", value=member.display_name, inline=False)

        embed.add_field(name="**Created at:**", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="**Joined at:**", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name=f"**Roles ({len(roles)})**", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="**Top role:**", value=member.top_role.mention)

        embed.add_field(name="**Bot?**", value=member.bot)

        embed.add_field(name="**Mobile?**", value=f"{member.is_on_mobile()}")
        embed.add_field(name="**Status:**", value=f"{member.status}")

        embed.add_field(name="**Boosting Since:**", value=f"{member.premium_since}")
        await ctx.send(embed=embed)

@client.command()
async def serverinfo(ctx):
        guild = ctx.guild

        embed = discord.Embed(colour=ctx.author.color)

        embed.set_author(name=f"Server Info - {guild.name}")
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_footer(text="Made by Ransomwave")

        embed.add_field(name="**Server ID**", value=guild.id)
        embed.add_field(name="**Server Owner:**", value=guild.owner.mention, inline=False)
        embed.add_field(name="**Verification level:**", value=guild.verification_level)
        embed.add_field(name="**Server Region:**", value=guild.region, inline=False)
        embed.add_field(name="**Member Count:**", value=guild.member_count)
        embed.add_field(name="**Emoji Count:**", value=f"{len(guild.emojis)}")
        embed.add_field(name="**Nitro Boosters:**", value=guild.premium_subscription_count)

        await ctx.send(embed=embed)



@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, * , reason=None):
 await member.ban(reason=reason)
 await ctx.send(f"**{member.name}** has been **banned**!  <a:BlobBanHammer:716268575064588288>")


@client.command(aliases=['delete','purge'])
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send('**Messages deleted succefully!** <a:verify:711183651928408184>')


@client.command()
async def invite(ctx):
    await ctx.send('Invite me to **your server** with this link! 👉 https://discord.com/oauth2/authorize?client_id=660140130454994964&scope=bot&permissions=8')

@client.command()
async def waifu(ctx):
    chosen_image = random.choice(waifulinks)

    embed = discord.Embed(colour=0xff629d)
    embed.set_image(url=chosen_image)
    embed.add_field(name="Wave Waifu Command", value="Here's your waifu!", inline=False)
    embed.set_footer(text=f"Made by Ransomwave · Requested by {ctx.author.display_name}")
    await ctx.send(embed=embed)


@client.command(aliases=["memes"])
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 20)
    for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_image(url=submission.url)
    embed.add_field(name="Wave Meme Command", value=f"Here is your meme!", inline=False)
    embed.set_footer(text=f"Made by Ransomwave · Requested by {ctx.author.display_name}")

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member : discord.Member, *, arg=None):
        await ctx.send(f"> **{member.name}**  has been warned because of reason: **'{arg}'**!")

        embed = discord.Embed()
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name="⚠️ You have been warned! ⚠️")
        embed.add_field(name="**Reason:**", value=f"{arg}", inline=False)
        embed.add_field(name="**Server:**", value=f"{ctx.guild.name}", inline=False)
        embed.add_field(name="**Moderator:**", value=f"{ctx.author.name}", inline=False)
        await member.send(embed=embed)

@client.command(aliases=["animememes", "animeme", "animemes"])
async def animememe(ctx):
    memes_submissions = reddit.subreddit('goodanimemes').hot()
    post_to_pick = random.randint(1, 20)
    for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_image(url=submission.url)
    embed.add_field(name="Wave Anime Meme Image Command", value=f"Here is you anime meme!", inline=False)
    embed.set_footer(text=f"Made by Ransomwave · Requested by {ctx.author.display_name}")

    await ctx.send(embed=embed)


@client.command(aliases=["cchanel"])
@commands.has_permissions(manage_channels=True)
async def createchannel(ctx, name, *, overwrites=None, category=None, reason=None):
        guild = ctx.guild

        await guild.create_text_channel(name=name, overwrites=overwrites, category=category)

@client.command(aliases=["8ball"])
async def eightball(ctx, *, arg):
        chosen_response = random.choice(responses)
        embed = discord.Embed(colour=discord.Colour.dark_blue())

        embed.set_author(name="Magic 8ball")
        embed.set_footer(text="Made by Ransomwave")
        embed.add_field(name="**Question:**", value=arg, inline=False)

        embed.add_field(name="**:8ball: Response: :8ball:**", value=chosen_response, inline=False)
        await ctx.send(embed=embed)

@client.command(aliases=["cvc", "createvoicechannel", "createvoicec", "createvchannel"])
@commands.has_permissions(manage_channels=True)
async def createvc(ctx, name, *, overwrites=None, category=None, reason=None):
        guild = ctx.guild

        await guild.create_voice_channel(name=name, overwrites=overwrites, category=category)

#giveaway test
@client.command()
@commands.has_permissions(administrator=True)
async def giveaway(ctx, seconds: int, *, givingaway: str):

        #embed
        giveawayembed = discord.Embed(
                title="🎉 A giveaway has appeared!",
        colour=discord.Colour(0x3b12ef)
        )

        giveawayembed.set_footer(text="Made by Ransomwave")

        giveawayembed.add_field(name=f"{givingaway}", value=f"Giveaway lasts {seconds} seconds. Hosted by {ctx.author.mention}\nReact with ':tada:' to enter!")

        #other stuff
        await asyncio.sleep(2)
        giveawaymsg = await ctx.send(embed=giveawayembed)
        await giveawaymsg.add_reaction('🎉')
        await asyncio.sleep(seconds)
        giveawaymsg = await ctx.fetch_message(giveawaymsg.id)
        users = await giveawaymsg.reactions[0].users().flatten()
        winner = random.choice(users)
        await ctx.send(f'{winner.mention} has won the giveaway!')
        
        #bot exception
        if winner.bot:
                await ctx.send("It seems like the bot has won the giveaway, rerolling... <a:loading:728963112652374048>")
                await giveawaymsg.remove_reaction('🎉', client.get_user(688783288713871428))
                rerolled = random.choice(users)
                await ctx.send(f"{rerolled.mention} has won the giveaway!")


@client.command(aliases=['slots', 'bet'])
async def slot(ctx):
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
                await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
                await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        else:
                await ctx.send(f"{slotmachine} No match, you lost 😢")

@client.command(aliases=['howhot', 'hot'])
async def hotcalc(ctx, *, user: discord.Member = None):
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        emoji = "💔"
        if hot > 25:
                emoji = "❤"
        if hot > 50:
                emoji = "💖"
        if hot > 75:
                emoji = "💞"

        await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot \{emoji}")

@client.command()
async def reverse(ctx, *, text: str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"<:reverse:737682508031852574> {t_rev}")

@client.command()
async def translate(ctx, *, text):
        trans = Translator()
        t = trans.translate(text)
        
        embed = discord.Embed(colour=discord.Colour.blue())
        
        embed.set_author(name="Wave Translator")
        embed.set_thumbnail(url='https://seeklogo.com/images/G/google-translate-logo-42DAD4AA91-seeklogo.com.png')
        embed.add_field(name="Succefully Translated!", value=f"{text} -> {t.text}")
        embed.set_footer(text=f"Requested by: {ctx.author.name}")

        await ctx.send(ctx.author.mention)
        await ctx.send(embed=embed)
        


#idle cmds
@client.command()
async def hug(ctx, member : discord.Member):
        c = aiohttp.ClientSession()
        async with c as s:
                    async with s.get("https://nekos.life/api/hug") as response:

                             restxt = await response.json()
                             neko_UwU = restxt["url"]

        embed = discord.Embed(
        title=f"Hug!",
        description=f"**{ctx.author.name}** hugs **{member.name}**! <a:hug:726031053193478546>",
        colour=0xffa8f6
)

        embed.set_image(url=neko_UwU)
        await ctx.send(embed=embed)


@client.command()
async def kiss(ctx, member : discord.Member):
        c = aiohttp.ClientSession()
        async with c as s:
                    async with s.get("https://nekos.life/api/kiss") as response:

                             restxt = await response.json()
                             response = restxt["url"]

        embed = discord.Embed(
        title=f"Kiss! o///o",
        description=f"**{ctx.author.name}** kisses **{member.name}**! :heart:",
        colour=0xffa8f6
)
        embed.set_image(url=response)

        await ctx.send(embed=embed)

@client.command()
async def pat(ctx, member : discord.Member):
        c = aiohttp.ClientSession()
        async with c as s:
                async with s.get("https://nekos.life/api/pat") as response:

                        restxt = await response.json()
                        response = restxt["url"]

        embed = discord.Embed(
        title=f"Pat! :3",
        description=f"**{ctx.author.name}** pats **{member.name}**! <:kannaPat:726456869043830784>",
        colour=0xffa8f6
)
        embed.set_image(url=response)
        await ctx.send(embed=embed)

@client.command()
async def slap(ctx, member : discord.Member):
        c = aiohttp.ClientSession()
        async with c as s:
                async with s.get("https://nekos.life/api/v2/img/slap") as response:

                        restxt = await response.json()
                        response = restxt["url"]

        embed = discord.Embed(
        title=f"Slap!",
        description=f"**{ctx.author.name}** slapped **{member.name}**! <:Reee:726036384527155210>",
        colour=0xffa8f6
)
        embed.set_image(url=response)
        await ctx.send(embed=embed)

client.run('!!! YOUR TOKEN HERE !!!')
