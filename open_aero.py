import discord, os, requests, time, subprocess, sys, datetime, random, platform, hashlib
from os import remove
import discord.ext.commands
from subprocess import PIPE, run;from io import StringIO
from random import randint, choice
print("\nStarting Service - Standby For Login Message!")
def get_logs():
    with open(settings.update_log, 'w+') as file:
        logs = str(file.read())
        logs = str(f"```css\n{logs}\n```")
    return logs

#############################       EDIT Below >  
admin_file = "admins.txt"
t_key = "dbd726df4beeac82be8c210f5b216ea9"
class settings:
    update_log = "new_updates.txt" # UPDATE LOG FILENAME HERE
    Token = ""# TOKEN HERE
    rp = "^help | https://aero-bot.pro/"# RICH PRESENCE STATUS HERE
    update_log = get_logs()
class channels:#EDIT CHANNEL ID'S Below - Make Sure Bot Has Correct Perms! > 
    bot_announcements = 0000000000000
    security_log = 0000000000000
    tickets = 0000000000000
    applications = 0000000000000
###########################################################################################################################    
    
class url:
    class mean:
        freeze_gif="https://i.imgur.com/ehxMcVy.gif"
        
    class hello:
        other_kinda_hot = "https://giphy.com/gifs/yevbel-l0K4mVlNMmr3Bj6V2"
        toof_dude = "https://giphy.com/gifs/lakings-hello-kyle-clifford-says-3o6Ztl7oraKm4ZJ9mw"
        waving_girl_gif="https://giphy.com/gifs/vspink-26vUTlnHulTgAU7le"
        sup_gif = "https://giphy.com/gifs/eldusty-el-dusty-l0IybIP1xUDwcY7Kw"
        meet_again_gif = "https://giphy.com/gifs/hyperrpg-twitch-kollok-kollok1991-2ywMwSsEFKu6HuxWrg"

class strings:
    
    null_ = ""
    strip_1=str("""   
    IS VALID?: """)
    strip_2=str("""

    NUMBER: """)
    strip_3=str("""

    LOCAL FORMAT: """)
    strip_4=str("""

    INTERNATIONAL FORMAT: """)
    strip_5=str("""

    COUNTRY (PRFX): """)
    strip_6=str("""

    COUNTRY CODE: """)
    strip_7=str("""

    COUNTRY NAME: """)
    strip_8=str("""

    LOCATION: """)
    strip_9=str("""

    LINE TYPE: """)
    strip_10=str("""

    CARRIER: """)
    strip_11=str("""
    
>>>: """)
    code_help = str("""
Code/Text Editor/Make File:
'^editor <format>
<text>'

// Example:
'^code python
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")'

""")
    dev_help = str("""

""")
    info_help = str("""
**__Information: (NEW):__**
```css
'^check.date SNOWFLAKE_ID' or '^id.date SNOWFLAKE_ID' - Get Creation Date Of ID.
'^user.info @USER' - Get some user info of a profile.
'^uptime' - Get System Info.
```
""")
    other_help = str("""
**__Other:__**
```css
'^curr2btc' or '^money2btc' or 'convert.btc' <SYM> <amount>
'^math 6 * 6' or '^math 6 / 6' or '^math 6 + 6' or '^math 6 - 6'
'^insult' or '^destroy' <user> - Insult Another User
'^music.<genre>' or '^music.help' - Music Player
'^meme' - Send Meme
'^hello' - Say Hello

Support Ticket To Dev:  
'^ticket <message>'

```
""")
    resolver_help = str("""
**__Resolver:__**
```css
'^phonelookup <number>' or ^phone <number> - Get Info
'^resolve.skype' <skype-user>
'^ip.skype' <IP> or '^ip2skype' <IP>
'^cloudflare.resolve <Url>'
```
""")
    
    network_help = str("""
**__Network Tools:__**
```css
'^ping <Host>' - Pings Host
'^lookup <Host>' - Lookup Host
'^scan <Host>' - Portscan Host
'^traceroute <Host>' - Traceroute To Host
'^scrape <Url>'
'^hack <Host>' - Little Vuln. Check
```
""")

    help_text="""
『ヅ』 『H』『e』『l』『p』 『ヅ』
|| || https://aero-bot.pro/ || ||

```yaml
https://aero-bot.pro/ - @aero#7331 Is My Creator :)

DOCUMENTATION
--------------------------------------------------------------------------
Help:
'^help' - General Help Text

Log:
'^updates' or '^log' - Updates & Info

Network:
`^network` - Info About Network Tools

Resolver:
'^resolver' - Info About Resolver Tools

Other:
'^other' - Info About Other Tools

Admins:
'^admin.help' - Admin Help

Information: (NEW):
'^info' - Info about ... well..getting info!

Developer(NEW):
'^programming' - Info About Built-In Code Editor etc [Impractical But Fun :)] 

News: 
(Adding Soon!)
--------------------------------------------------------------------------

```
"""
class admins:
    help_text=str(f"""\n```css\n----------------------------------------\n```**__Welcome To AeroFile[ADMIN]__**\n```css\n----------------------------------------\n```\nhttps://cdn.discordapp.com/attachments/611039806918623268/612839905122582538/8299_Loading.gif\n
```css
ONLY USE IN ADMIN CHATS!!!

^admin.help - Admin Help

^admin.announcement - make post in #bot-announcements < 

^prune 100 False - [prune - 'Delete Oldest First' is the True/False Statement]

^gettickets - Get tickets from cloud server < 

^getapps - Get application file from cloud server < 

^getlogs - Gets our chat log file from cloud server
```
""")


##################
def is_admin(idd):
    admin = False
    listed = [line.rstrip('\n') for line in open(admin_file)]
    if str(idd) in listed:
        admin = True
    return admin   

    
class insults:
    aa = "**Lol,** ";ab = " **is as useless as a traffic light in GTA.**"
    ba = "";bb = " **has 500gigs of child porn @ BitchUgotDestroyed.onion! Ping The IC!!!**"
    ca = "**Hey**";cb = ", **you've got something on your Chin...No, the 3rd one down..**"
    da = "";db = " **is the main reason the gene pool needs a lifeguard..**"
    ea = "";eb = "! **Lol really??? This ones too easy...**"
    
class lists:
    useragents = [
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/57.0.2987.110 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.79 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
     'Gecko/20100101 '
     'Firefox/55.0'),  # firefox
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.91 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/62.0.3202.89 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/63.0.3239.108 '
     'Safari/537.36'),  # chrome
    ]

class music:
    class favorites:
        a = "https://soundcloud.com/itsgladez/gladez-favela";b = "https://soundcloud.com/reaperdubstep/reaper-buried-feat-micah-byrnesbuy-for-free-dl";c = "https://soundcloud.com/misogi/lunar";d = "https://soundcloud.com/tisoki-treats/heartbroken";e = "https://soundcloud.com/bighitterburt/outcast"
        f = "https://soundcloud.com/andem01/getter-colorblind";g = "https://soundcloud.com/warnedstep/shadowcloneanthemvip";h = "*https://soundcloud.com/christravis/chris-travis-beam"
        i = "https://soundcloud.com/bitbird/taska-black-where-we-go";j = "https://soundcloud.com/convolk/swan-dive";k = "https://soundcloud.com/comethazine/findhim"
    class country:
        a = "https://soundcloud.com/drugstorecowboy-1/coward-of-the-county-kenny?in=user-410239506/sets/country-music-2019"
        b = "https://soundcloud.com/sugar-hill-records/talk-is-cheap-1?in=user-410239506/sets/country-music-2019"
        c = "https://soundcloud.com/marshmellomusic/one-thing-right-feat-kane?in=diehansa/sets/country-songs"
        d = "https://soundcloud.com/danandshay/all-to-myself?in=diehansa/sets/country-songs"
        e = "https://soundcloud.com/keith_urban/we-were?in=diehansa/sets/country-songs"
        f = "https://soundcloud.com/blakeshelton/boys-round-here-feat-pistol-annies?in=pam-robinson-338577353/sets/mixed-country"
        g = "https://soundcloud.com/thecollectivesounds/aaron-lewis-country-boy"
        h = "https://soundcloud.com/cole-swindell/middle-of-a-memory?in=pam-robinson-338577353/sets/cole-swindell"
        i = "https://soundcloud.com/blakeshelton/kiss-my-country-ass-2"
        j = "https://soundcloud.com/chris-janson-official/buy-me-a-boat?in=pam-robinson-338577353/sets/chris-jansen"
        k = "https://soundcloud.com/jon-pardi-music/heartache-on-the-dance-floor?in=pam-robinson-338577353/sets/jon-pardimusic"
    class rap_hip_hop:
        a = "https://soundcloud.com/rapsc/ybn-nahmir-opp-stoppa"
        b = "https://soundcloud.com/hip-hop/strybo-plan-feat-latro"
        c = "https://soundcloud.com/gxx/gxx-run-my-faxe"
        d = "https://soundcloud.com/bigsean-1/overtime"
        e = "https://soundcloud.com/migosatl/slippery-feat-gucci-mane"
        f = "https://soundcloud.com/lilpump/lil-pump-gucci-gang-prod-bighead-gnealz"
        g = "https://soundcloud.com/ybncordae/we-gon-make-it-feat-meek-mill"
        h = "https://soundcloud.com/comethazine/findhim"
        i = "https://soundcloud.com/secret-service-862007284/old-town-road"
        j = "https://soundcloud.com/chancetherapper/slide-around"
        k = "https://soundcloud.com/trapgod1017bricksquad/gucci-mane-both-ft-drake-1"
        l = "https://soundcloud.com/brokenheartedhours/shiloh-dynasty-downtown-prod-mikaro2k14-not-mine"
        m = "https://soundcloud.com/user-207375672/ski-mask-the-slump-god-babywipe-lofi-version"
        n = "https://soundcloud.com/ambjaay/uno"
        o = "https://soundcloud.com/nlechoppa/shotta-flow-3?in=soundcloud-hustle/sets/rap-new-hot"
    class rock:
        a = "https://soundcloud.com/atlanticrecords/skillet-rise?in=user-919362863/sets/rock"
        b = "https://soundcloud.com/roadrunner-usa/nickelback-how-you-remind-me?in=user-730670180/sets/rock"
        c = "https://soundcloud.com/patrick-drummer/system-of-a-down-chop-suey?in=vargas-jose-annabelle/sets/rock"
        d = "https://soundcloud.com/jhon-agudelo-1/slipknot-before-i-forget"
        e = "https://soundcloud.com/officialmetallica/metallica-master-of-puppets?in=francisco-segovia-564442040/sets/rock"
        f = "https://soundcloud.com/blink-182/i-miss-you-album-version"
        g = "https://soundcloud.com/red-hot-chili-peppers-official/californication"
        h = "https://soundcloud.com/red-hot-chili-peppers-official/californication"
        i = "https://soundcloud.com/victoryrecords/dead-girls-academy-ill-find-a-way"
        j = "https://soundcloud.com/xx-reika-xx/30-second-to-mars-the-kill"
        k = "https://soundcloud.com/victoryrecords"
              

class application:
    def make(message, author):
        nig = str(author);ran=str(randint(1000, 9999));content = str(message.replace("apply",'').replace("^apply",'').replace("!apply",''));t_d=str(datetime.datetime.now())
        print(f"\n----------------------\n[{t_d}] - [TICKET: {ran}]\nTicket From {nig}\nBODY:\n{content}\n----------------------\n")
        f=open(f"applications.txt","a");stuff = str(f"\n[{t_d}] - [APPLICATION: {ran}]\nApplication From {nig}\n------------------------\nBODY:\n{content}\n----------------------------\n");f.write(stuff);f.close()
        result = str(f"**Thank You For Submitting An Application, {nig}!\nYour Inquiry Has Been Received, Someone Will Review It And An Admin/Owner Will Get Back To You Shortly!**\n\n```css\nClient ID: {nig}\nTicket Number: {ran}\n```\n\n**We Value Your Application <3**")
        return result
    
class ticket:
    def make(message, author):
        nig = str(author);ran=str(randint(1000, 9999));content = str(message);t_d=str(datetime.datetime.now())
        print(f"\n----------------------\n[{t_d}] - [TICKET: {ran}]\nTicket From {nig}\nBODY:\n{content}\n----------------------\n")
        f=open(f"tickets.txt","a+");stuff = str(f"\n[{t_d}] - [TICKET: {ran}]\nTicket From {nig}\n------------------------\nBODY:\n{content}\n----------------------------\n");f.write(stuff);f.close()
        result = str(f"**Thank You For Submitting Your Ticket Correctly, {nig}!\nYour Ticket Has Been Received, Someone Will Review It And Get Back To You Shortly!**\n\n```css\nClient ID: {nig}\nTicket Number: {ran}\n```\n\n**We Value Your Input <3**")
        return result



#class md5:
#    def make_hash(self, thing):
#        thing = str(thing)
#        result = hashlib.md5(thing.encode())
#        return str(result.hexdigest()) 
#  
#        
#class hexx:
#    def decode(self, hexx):
#        hexx = str(hexx)
#        this = str(hexx.decode("hex"))
#        return this
#    
#    def encode(self, stringg):
#        string = str(stringg)
#        this = str(string.hex())
#        return this
        
        
    
    
    
class languages:
    def get_extension(stuff):
        if stuff == "html":
            extension = "html"
        if stuff =="python":
            extension = "py"
        if stuff == "python":
            extension = "py"
        if stuff == "javascript":
            extension = "js"
        if stuff == "c":
            extension = "c"
        if stuff == "c++":
            extension = "cpp"
        if stuff == "cpp":
            extension = "cpp"    
        if stuff == "perl":
            extension = "pl"
        if stuff == "css":
            extension = "css"
        if stuff == "text":
            extension = "txt"
        if stuff == "batch":
            extension = "bat"
        if stuff == "null":
            extension = ""
        return extension
    
    
class ide:
    def format(message, author):
        erro = False
        try:
            lang = message.split()[1]
        except Exception:
            erro = True
        if erro == False:
            ext = str(languages.get_extension(lang))
            filename = str(f"AeroFilecode{lang}.{ext}")
            file = open(filename, "w+")
            body = message.replace("^code ", '').replace(lang,"")
            file.write(f"\n{body}\n");file.close()
        if erro == True:
            result = str("Correct Format Example:\n^code python\n#!/usr/bin/python\nfrom time import sleep\nchar2 = 'Farewell for now!'\nchar1='Hello World, brb!'\nfor x in range(0, 10):\n    if x == 9:\n        print(char2)\n        sleep(1)\n    else:\n        print(char1)\n\n")
        elif erro != True:
            result = str(f"""
```{lang}
{body}
```
*-Formatting requested by {author}!-*

*-AeroFile By Aerospace_Dev <3 -*
""")
        return {'result' : result,'filename' : filename }

count = 0
bot_count = 0    
#######################################################################################################################################################################    
#client = discord.AutoShardedClient(shard_count=2)
client = discord.Client()   
@client.event
async def on_ready():
    print('-\n[Ok] - Succesfully logged in as {0.user}'.format(client))
    activity = discord.Activity(name=settings.rp, type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
   
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    global count, bot_count
    count += 1
    if message.author.bot == True:
        bot_count += 1
        return    
    try:
        a = open("User_dialog.txt", "a", encoding="utf8");a.write(f'{message.content}\n');a.close()
    except Exception as f1:
        print("First write to mem. failed!\n"+str(f1))

        
#    if message.content.startswith('^md5.encode'):
#        this = hexx.encode(message.content.split()[1])
#        await message.channel.send(f"```css\n{this}```")
#        
#    if message.content.startswith('^hex.encode'):
#        this = hexx.encode(message.content.split().replcace("^hex.", "").replace("encode", "").replace("Encode", ""))
#        await message.channel.send(f"```css\n{this}```")
#            
#    if message.content.startswith('^hex.decode'):
#        this = hexx.decode(message.content.split()[1])
#        await message.channel.send(f"```css\n{this}```")
            
    if message.content.startswith('^network'):
        await message.channel.send(strings.network_help)
    if message.content.startswith('^resolver'):
        await message.channel.send(strings.resolver_help)            
    if message.content.startswith('^other'):
        await message.channel.send(strings.other_help)              
    if message.content.startswith('^info'):
        await message.channel.send(strings.info_help)            
    if message.content.startswith('^programming'):
        await message.channel.send(strings.code_help)
    if message.content.startswith('^admin.help'):
        await message.channel.send(admins.help_text)            
        
        
        
    #Warning! - (line below) LOGS ALL INPUT IF ENABLED(uncommented.hashtagged)!!!!
    #print("\n["+str(datetime.datetime.now())+"] - [LOG]\nUsed by "+str(message.author)+"\n"+"Their input:\n"+str(message.content)+"\n\n")
            
            
        
                
                              
                                       
                
    if message.content.startswith("^uptime") or message.content.startswith("^system"):
        try:
            uptime = subprocess.check_output("uptime")
            uptime1 = uptime.decode("utf-8")
            up = uptime1.replace(",", " |")
        except Exception:
            up = "Oops! I'm running on a Windows test machine!"
        embed = discord.Embed(title=f"AeroTools Uptime", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="AeroTools", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/610035652112810024/620167625774727178/1_h4YRd-tMvBGSVhAXtzYbKA_1.png")
        embed.add_field(name="__Current Uptime:__", value=f"{up}", inline=False)
        embed.add_field(name="__Requests Since Boot:__", value=str(count), inline=False)
        embed.add_field(name="__Self Bots Detected:__", value=str(bot_count), inline=False)
        embed.add_field(name="__Active Shards:__", value="`3` Rated @ 1k Servers Per Shard.", inline=False)
        embed.add_field(name="__System:__", value=str(platform.system()), inline=False)
        embed.add_field(name="__Release:__", value=str(platform.release()), inline=False)
        embed.add_field(name="__Version:__", value=str(platform.version()), inline=False)
        embed.add_field(name="__Machine:__", value=str(platform.machine()), inline=False)
        embed.add_field(name="__Proccessor:__", value=str(platform.processor()), inline=False)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        await message.channel.send("**__System Info__**", embed=embed)

        
        
    if message.content.startswith("^math") or message.content.startswith("^calculator"):
        fuck = message.content.split()
        eroz = False
        try:
            var1 = int(fuck[1])
            sign = fuck[2]
            var2 = str(fuck[3])
        except Exception:
            eroz = True
        if eroz == False:
            try:
                if sign == "+":
                    answer = int(int(var1) + int(var2))
                    await message.channel.send(f"```css\n{str(answer)}\n```")
                if sign == "-":
                    answer = int(int(var1) - int(var2))
                    await message.channel.send(f"```css\n{str(answer)}\n```")
                if sign == "*":
                    answer = int(int(var1) * int(var2))
                    await message.channel.send(f"```css\n{str(answer)}\n```")
                if sign == "/":
                    answer = int(int(var1) / int(var2))
                    await message.channel.send(f"```css\n{str(answer)}\n```")
            except Exception as g:
                await message.channel.send(f"```css\n{str(g)}\n```")
        else:
            await message.channel.send("Incorrect Usage!\nTry: `^math 6 * 6 or ^math 6 / 6 or ^math 6 + 6 or ^math 6 - 6`")
        
        
        
    if message.content.startswith('^prune') or message.content.startswith('^purge'):
        if is_admin(message.author.id) == True:
            try:
                amount = int(message.content.split()[1])
                boldest = bool(message.content.split()[2])
                await message.channel.purge(limit=amount, check=None, before=None, after=None, around=None, oldest_first=False, bulk=True)
            except Exception as e:
                await message.channel.send(f"Correct Useage: ^prune 100 True/False\n[T/F = Oldest First]ERROR:\n{str(e)}")
                pass
        else:
            channel = client.get_channel(channels.security_log)
            dt = str(datetime.datetime.now())
            await channel.send(f"**__Security Alert:__**\n{message.author} Attempted to `purge chat` in Channel # {message.channel} Without Clearance.\n\n Raw Event: {message.content}\n\nOccured: (Time):\n{dt}")
            await message.channel.send(f"!warn {message.author} *You've attempted to use an Adminstrators option without clearance*\n\n **__Attention Administrators:__** `1` warning Has been issued to {message.author}!")
        
    if message.content.startswith('^announce') or message.content.startswith('^admin.announce'):
        saddmin = False
        if is_admin(int(message.author.id)) == True:
            saddmin = True          
        if saddmin == True:
            channel = client.get_channel(channels.bot_announcements) ###
            content = message.content.replace("^admin.announce", "").replace("^announce", "")
            await channel.send(f'**__Announcement By {message.author}:__**\n```css\n{content}\n```\n')
            await message.channel.send(f'** {message.author}, Your announcement has been posted! | Channel: <#{channel.name}> **')
            await message.delete()
        elif saddmin == False:
            channel = client.get_channel(channels.security_log)
            dt = str(datetime.datetime.now())
            await channel.send(f"**__Security Alert:__**\n{message.author} Attempted to `Make Announcement` in Channel # {message.channel} Without Clearance.\n\n Raw Event: {message.content}\n\nOccured: (Time):\n{dt}")
            await message.channel.send(f"!warn {message.author} *You've attempted to use an Adminstrators option without clearance*\n\n **__Attention Administrators:__** `1` warning Has been issued to {message.author}!")
        
    if message.content.startswith('^check.date') or message.content.startswith('^id.date'):
        try:
            berr = False
            p = int(message.content.split()[1])
            pstr = str(p)
            create_date = str(discord.utils.snowflake_time(int(p)))
        except Exception as er:
            berr = True
            print(str(er))
        if berr == False:
            await message.channel.send(f"**This Profile, Message, DM, Server or OTHER, `[{pstr}]` Was Created** `[{create_date}]`")
        
        
    if message.content.startswith('^admin.help'):
        if is_admin(int(message.author.id)) == True:
            await message.channel.send(admins.help_text)
            
        
    if message.content.startswith('^ticket') or message.content.startswith('$ticket'):
        op = str(message.author)
        await message.channel.send(ticket.make(message.content, op))
        await message.delete()
        channel = client.get_channel(channels.tickets)
        nig = str(message.author);ran=str(randint(1000, 9999));content = str(message.content.replace("^ticket",''));t_d=str(datetime.datetime.now())
        stuff = str(f"```css\n[{t_d}] - [__**TICKET**__: {ran}]\nTicket From {nig}\n------------------------\nBODY:\n{content}\n----------------------------\n```\n")
        await channel.send(stuff)

    if message.content.startswith("^spam"):
        if is_admin(message.author.id) == True:
            try:
                str_target = int(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", ""))
                exx = False
            except Exception:
                await message.channel.send(str(bold("Error - Needs To Be: "))+str(css("^spam @valid_user_mention")))
            target = int(str_target)
            worked = True
            if exx == False:
                user = client.get_user(target)
                if user is not None and user.bot != True:
                    count = 0
                    try:
                        for x in range(0, 24):
                            count += 1
                            await user.send(f"**Hey <@{str(user.id)}> !\n{message.author} Asked Me To Send You A Message![or 25]\n[Message Count: {str(count)} / 25]**\n")
                    except Exception as poop:
                        worked = False
                        await message.channel.send(f"**__Warning:__ - Could Not Send Spam To {member.name}!\n```css\n{str(poop)}\n```**")
                    if worked == True:
                        await message.channel.send(f"**{message.author} Successfully Sent Some Spam To {member.name}**")
                else:
                    await message.channel.send(f"**__Warning:__ - Could Not Find Member In Our Server!**")
        else:
            await message.channel.send(f"**__Warning:__ - Must be Admin Or Have A Spam Token!!!**")                

                
    if message.content.startswith('^user.info'):
        p1 = message.content.replace("^user.info","").replace(" ", "").replace("<", "").replace("@", "").replace(">", "").replace("!", "")
        exx = False
        try:
            p1 = int(p1)
        except Exception:
            exx = True
            pass
        if exx == False:
            member = discord.utils.get(message.guild.members, id=p1)
            if member is not None and member.bot != True:
                name = str(member.display_name)
                start_date = str(discord.utils.snowflake_time(member.id))
                block_char = str(bool(member.is_blocked()))
                avatar = str(member.avatar_url)
                mutual_guild = str(member.guild.name)
                join_date = str(member.joined_at)
                try:
                    current_act = str(member.activities)
                except Exception:
                    current_act = str("**Possible Self-Bot!!!**")
                role = str(member.roles)
                role = role.replace("[", "").replace("]", "").replace("<", "").replace(">", "")
                role = role.replace("@", "")
                if len(role) > 800:
                    role = "Too Many Roles To Display!!!!"
                embed = discord.Embed(title=f"User Info For\n{name}", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
                embed.set_author(name="AeroTools", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
                embed.set_thumbnail(url=avatar)
                embed.add_field(name="__User:__", value=name, inline=False)
                embed.add_field(name="__Nickname:__", value=str(member.nick), inline=False)#
                embed.add_field(name="__ID:__", value=f"{str(p1)}", inline=False)
                embed.add_field(name="__Creation Date:__", value=start_date, inline=False)
                embed.add_field(name="__Mutual Server:__", value=mutual_guild, inline=False)
                embed.add_field(name="__Joined Server:__", value=join_date, inline=False)
                embed.add_field(name="__Current Status:__", value=f"{member.status}", inline=False)
                embed.add_field(name="__Blocked:__", value=str(block_char+"\n---------------------------\n"), inline=False)
                embed.add_field(name="__Current Activity:__", value=current_act, inline=False)
                embed.add_field(name="__Current Roles:__", value=str(role), inline=False)
                embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
                await message.channel.send("**__User Info__**", embed=embed)
        else:
            await message.channel.send(f"Member [{p1}] Not Found In Guild(Not Accessible)!")


            
        
    if message.content.startswith('^code') or message.content.startswith('^file') or message.content.startswith('^editor') or message.content.startswith('^text'):
        result = ide.format(message.content, message.author)
        body = str(result['result']);filename = result['filename']
        print(filename+"\n"+body)
        await message.channel.send(body, file=discord.File(filename))
        remove(filename)
        
    if message.content.startswith('^apply') or message.content.startswith('!apply'): 
        await message.channel.send(application.make(message.content, message.author))
        channel = client.get_channel(channels.applications)
        nig = str(message.author);ran=str(randint(1000, 9999));content = str(message.content.replace("apply",'').replace("^apply",'').replace("!apply",''));t_d=str(datetime.datetime.now())
        stuff = str(f"```css\n[{t_d}] - [APPLICATION: {ran}]\nApplication From {nig}\n------------------------\nBODY:\n{content}\n----------------------------\n```\n")
        await channel.send(stuff)
        await message.delete()
        
    if message.content.startswith('^gettickets') or message.content.startswith('^dev.tickets'):
        op1 = str(message.author);bAdmin = False
        if op1 in admins.admins:
            bAdmin = True          
        if bAdmin == True:
            await message.channel.send(f'Here is your tickets file {message.author}', file=discord.File('tickets.txt'));await message.delete()
        else:
            channel = client.get_channel(channels.security_log)
            dt = str(datetime.datetime.now())
            await channel.send(f"**__Security Alert:__**\n{message.author} Attempted to `View Tickets` in Channel # {message.channel} Without Clearance.\n\n Raw Event: {message.content}\n\nOccured: (Time):\n{dt}")
            await message.channel.send(f"!warn {message.author} *You've attempted to use an Adminstrators option without clearance*\n\n **__Attention Administrators:__** `1` warning Has been issued to {message.author}!")

    if message.content.startswith('^getapps') or message.content.startswith('^dev.tickets'):
        op2 = str(message.author);bAdmin = False
        if op2 in admins.admins:
            bAdmin = True          
        if bAdmin == True:
            await message.channel.send(f'Here is your applications file {message.author}', file=discord.File('applications.txt'));await message.delete()
        else:
            channel = client.get_channel(channels.security_log)
            dt = str(datetime.datetime.now())
            await channel.send(f"**__Security Alert:__**\n{message.author} Attempted to `View Applications` in Channel # {message.channel} Without Clearance.\n\n Raw Event: {message.content}\n\nOccured: (Time):\n{dt}")
            await message.channel.send(f"!warn {message.author} *You've attempted to use an Adminstrators option without clearance*\n\n **__Attention Administrators:__** `1` warning Has been issued to {message.author}!")

        
    if message.content.startswith('^getchatlogs') or message.content.startswith('^dev.logs'):
        bAdmin = False
        if is_admin(int(message.author.id)) == True:
            bAdmin = True          
        if bAdmin == True:
            await message.channel.send(f'Here is Aero-Tool"s log file {message.author}', file=discord.File('User_dialog.txt'));await message.delete()
        else:
            channel = client.get_channel(channels.security_log)
            dt = str(datetime.datetime.now())
            await channel.send(f"**__Security Alert:__**\n{message.author} Attempted to `Retrieve Lixxards Log` in Channel # {message.channel} Without Clearance.\n\n Raw Event: {message.content}\n\nOccured: (Time):\n{dt}")
            await message.channel.send(f"!warn {message.author} *You've attempted to use an Adminstrators option without clearance*\n\n **__Attention Administrators:__** `1` warning Has been issued to {message.author}!")

    
     
    if message.content.startswith('^meme') or message.content.startswith('$meme') or message.content.startswith('!meme') or message.content.startswith('^memes') or message.content.startswith('$memes') or message.content.startswith('!memes'):
        meme = requests.get("https://meme-api.herokuapp.com/gimme/dankmemes")
        memes = meme.json()
        mem = memes['url']
        await message.channel.send(mem)
        
    if message.content.startswith('^scrape'):
        gass=message.content.split();uurl = str(gass[1])
        await message.channel.send("**Sweeping "+uurl+", brb...**")
        myurl = ('https://webresolver.nl/api.php?'
                 'key=7JWS0-JJ5ZY-DK613-2PHB7&'
                 'html=0&'
                 'action=header&string='+str(uurl))
        loadboi = requests.get(myurl);jboi=loadboi.text
        await message.channel.send(str('**Header Sweep For **'+uurl+"\n```yaml\n"+jboi+"\n```\n*Requested By* **"+str(message.author)+"**."))
        
    if message.content.startswith('^changelog') or message.content.startswith('^updates') or message.content.startswith('^log') or message.content.startswith('^logs'):##Logs
        await message.channel.send(strings.log)
        
            
    if message.content.startswith('^hello') or message.content.startswith('@here'):#Greetings
        dice = randint(1, 5)
        if dice == 1: msg = str("**Ayy Its "+str(message.author)+"!**\n\n**Asuhhhh!!!**\n"+"\n\n"+url.hello.sup_gif)
        if dice == 2: msg = str("**Look, its "+str(message.author)+"!**\n\n*Hello There q-t-π!!!*\n"+"\n\n"+url.hello.waving_girl_gif)
        if dice == 3: msg = str("**Greetings "+str(message.author)+"!\n\nKeep It Spoopy;)\n\n**"+"\n\n"+url.hello.meet_again_gif)
        if dice == 4: msg = str("**"+str(message.author)+"!\n\nHey There Friend!\n\n**"+"\n\n"+url.hello.toof_dude)
        if dice == 5: msg = str("**Hey "+str(message.author)+"!**"+"\n\n"+url.hello.other_kinda_hot)
        await message.channel.send(str(msg))
        #help
    if message.content.startswith('^help') or message.content.startswith('$help') or message.content.startswith('!help') or message.content.startswith('&help'):
        await message.channel.send(f"\n**Here You Go, {message.author}!\n{strings.help_text}**")
        #test
    if message.content.startswith('^test') or message.content.startswith('^slam') or message.content.startswith('^hit') or message.content.startswith('^smack') or message.content.startswith('^slap') or message.content.startswith('^ddos'):
        #try:
        #    mylist = message.content.split();host=str(mylist[1]);port = str(mylist[2])
        #except Exception:
        #    await message.channel.send("*Error! - Invalid Format,\nNeeds to be as such: '^test <host> <port>*\n\nTry Again, Skiddo!'")
        #try:
        #    await message.channel.send("**Requested By** **"+str(message.author)+"**.")
        #    os.system(str("ssh -o PasswordAuthentication=no "+rem_host.user+rem_host.sym+rem_host.host1+" StrictHostKeyChecking=no screen -d -m 'perl udp.pl "+host+" "+port+" 4096 30'"))
        #    await message.channel.send("**Testing Sent!!!**\n\n\n"+str(message.author)+" Is Testing "+host+" for 30 Seconds @ Port "+port+'!!!\n\n')
        await message.channel.send("**Feature Unavailable For Now!!**\n**Purchase premium for unlimited testing!**")
        #except Exception as Error:
            #await message.channel.send("Dev-Mode Enabled\n\nERROR:\n"+str(Error))
            ##########################################PORTSCANNER
    if message.content.startswith('^portscan') or message.content.startswith('^scan'):
        m1 = message.content.split();ppp=str(m1[1])
        await message.channel.send("**Scanning "+ppp+"...**")
        link = str('https://api.hackertarget.com/nmap/?q={}'.format(ppp));r = requests.get(link)
        await message.channel.send("```yaml\n"+r.text+"\n```\n*Requested By* **"+str(message.author)+"**.")  
            
    if message.content.startswith('^psnresolve'):#Psn-Res
        mylist3 = message.content.split();inp3 = str(mylist3[1]);
        await message.channel.send("**Attempting To Resolve "+inp3+"...**")
        try:
            s = requests.get("https://psnresolver.org/resolve/"+inp3);html_str = s.text
            start = "<td>"
            end = "</td>"
            ips=str((html_str.split(start))[1].split(end)[0])
            re=requests.get('https://json.geoiplookup.io/' + ips)
            data=re.json();re_ip1 = data['ip'];re_isp1 = data['isp'];re_org1 = data['org'];re_hostname1 = data['hostname'];re_city1 = data['city'];re_country1 = data['country_name'];re_asn1 = data['asn'];re_integ1 = data['success']
            re_is_cached1 = data['cached'];re_curr1 = data['currency_code']
            if re_is_cached1 == True:
                integ_char1 = 'True'
            elif re_is_cached1 == False:
                integ_char1 = 'False'
            if re_is_cached1 == True:
                cache_char1 = 'True'
            elif re_is_cached1 == False:
                cache_char1 = 'False'
            thingy = str(re_hostname1)    
            goods1=str("""

                *Heres Those Results You Ordered:*

                ```yaml
    ||AeroTools - PSN Resolver||

    
    GAMERTAG: ["""+inp3+"""]


    IP: """ + re_ip1+ """

    ISP: """ + re_isp1 + """

    ORG: """ + re_org1 + """

    HOSTNAME: """ + re_hostname1 + """

    CITY: """ + re_city1 + """

    COUNTRY: """ + re_country1 + """

    ASN: """ + re_asn1 + """

    SUCCESS: """ + integ_char1 + """

    CACHED: """ + cache_char1 + """

    CURRENCY: """ + re_curr1 + """

    INFO: Coming Soon!

    *Powered By psn-resolver.org
                ```
                """+"\n*Requested By* **"+str(message.author)+"**.")
        except Exception as poo:
            await message.channel.send(poo)
        try:
            await message.channel.send(goods1)
        except Exception: pass




        
    if message.content.startswith('^trace') or message.content.startswith('^bypass') or message.content.startswith('^traceroute') or message.content.startswith('^tracert') or message.content.startswith('^ovhbypass'):
        mylist01 = message.content.split();poopie01=str(mylist01[1])
        await message.channel.send("**\nSending Probes To "+poopie01+"...\n**")
        command1 = ["traceroute", poopie01]
        try:
            out1=run(command1, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        except Exception as ooof:
            await message.channel.send("Error! \n"+str(ooof))
            pass
        await message.channel.send("**Traceroute Results**\n\n```yaml\n"+str(out1.stdout)+"\n```\n*Requested By* **"+str(message.author)+"**.")    

        
    if message.content.startswith('^ping') or message.content.startswith('^check'):
        mylist33 = message.content.split();poopie=str(mylist33[1])
        await message.channel.send("**\nPinging "+poopie+"...\n**")
        command = ["ping","-c","6",poopie]
        try:
            out=run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        except Exception as oooof:
            await message.channel.send("Error! \n"+str(oooof))
            pass
        await message.channel.send("**Pong!**\n\n```yaml\n"+str(out.stdout)+"\n```\n*Requested By* **"+str(message.author)+"**.")
        
    if message.content.startswith('^lookup'):
        mylist1 = message.content.split();inp = str(mylist1[1])
        await message.channel.send("**Looking Up "+inp+"...\n**")
        try:
            re=requests.get('https://json.geoiplookup.io/' + inp)
            data=re.json();re_ip = data['ip'];re_isp = data['isp'];re_org = data['org'];re_hostname = data['hostname'];re_city = data['city']
            re_country = data['country_name'];re_asn = data['asn'];re_integ = data['success'];re_is_cached = data['cached'];re_curr = data['currency_code']
            if re_is_cached == True: integ_char = 'True'
            elif re_is_cached == False: integ_char = 'False'
            if re_is_cached == True: cache_char = 'True'
            elif re_is_cached == False: cache_char = 'False'
            goods=str("""

            *Heres Those Results You Ordered:*

            ```yaml
||AeroTools Geo - Ip Lookup||

Results For """+re_hostname+""":


IP: """ + re_ip + """

ISP: """ + re_isp + """

ORG: """ + re_org + """

HOSTNAME: """ + re_hostname + """

CITY: """ + re_city + """

COUNTRY: """ + re_country + """

ASN: """ + re_asn + """

SUCCESS: """ + integ_char + """

CACHED: """ + cache_char + """

CURRENCY: """ + re_curr + """

INFO: Coming Soon!
            ```
            """+"\n*Requested By* **"+str(message.author)+"**.")
        except Exception:
            await message.channel.send("Error! - Invalid Host...")
        try:
            await message.channel.send(goods)
        except Exception: pass
        
    if message.content.startswith('^currency.help') or message.content.startswith('^curr.help'):
        await message.channel.send("**"+str(message.author)+", I've Recieved Your Beacon:** *^currency.help*\n\n\n**Example Of Correct Format: '^cash <USD> <10>'\n\n**\nThere we're pretty much asking to convert $10USD to BTC.\n\n**Currency Symbols(i/e): USD,GBP,RUB,EUR**");pass
#####          Insults
    if message.content.startswith('^destroy') or message.content.startswith('^insult') or message.content.startswith('^shame'):
        mylist215 = message.content.split();person215 = str(mylist215[1])
        dice215 = randint(1, 5)
        if dice215 == 1: msg = str(insults.aa+person215+insults.ab)
        if dice215 == 2: msg = str(insults.ba+person215+insults.bb)
        if dice215 == 3: msg = str(insults.ca+person215+insults.cb)
        if dice215 == 4: msg = str(insults.da+person215+insults.db)
        if dice215 == 5: msg = str(insults.ea+person215+insults.eb)
        await message.channel.send(msg)
    if message.content.startswith("^site") or message.content.startswith("^website"):
        strrr = str("""
**"    Automate your Discord!"**

    https://aero-bot.pro/
""")
        await message.channel.send(strrr)
        
    if message.content.startswith('^curr2btc') or message.content.startswith('^money2btc') or message.content.startswith('convert.btc') or message.content.startswith('^convert2btc'):
        try:
            mylist44 = message.content.split();SYM=str(mylist44[1]);amount = str(mylist44[2])
        except Exception:
            await message.channel.send("**Invalid Symbol - Try '^currency.help' For More Info!**")
        r=requests.get("https://blockchain.info/tobtc?currency="+SYM+"&value="+amount);nu=r.text
        await message.channel.send("*Approximate Comparison Of* **"+amount+SYM+"** *To* **BTC** *Is:*\n ```yaml\n"+nu+"\n ```")

    if message.content.startswith('^music.help') or message.content.startswith('^play.help'):
        await message.channel.send("**Usage (i/e):*** \n\n`^music.country`\nor\n`^play.country`\nor\n`^music.random`\nor\n`^play.random`\nor\n`^music.help`\n\n**Genres(so far):**\n*favorites*, *rap*, *hip-hop*, *dubstep*, *country*\n")

    if message.content.startswith('^music.favorites') or message.content.startswith('^music.favorite') or message.content.startswith('^music.random'):                           
        check = randint(0,10)
        if check == 1: msgg1 = music.favorites.a
        if check == 2: msgg1 = music.favorites.b
        if check == 2: msgg1 = music.favorites.c
        if check == 3: msgg1 = music.favorites.d
        if check == 4: msgg1 = music.favorites.e
        if check == 5: msgg1 = music.favorites.f
        if check == 6: msgg1 = music.favorites.g
        if check == 7: msgg1 = music.favorites.h
        if check == 8: msgg1 = music.favorites.i
        if check == 9: msgg1 = music.favorites.j
        if check == 10: msgg1 = music.favorites.k
        await message.channel.send(msgg1+"\n>>>*Requested By* **"+str(message.author)+"**.<<<")

    if message.content.startswith('^music.country') or message.content.startswith('^music.Country') or message.content.startswith('^play.Country') or message.content.startswith('^play.country'):
        check = randint(0,10)
        if check == 1: msgg2 = music.country.a
        if check == 2: msgg2 = music.country.b
        if check == 2: msgg2 = music.country.c
        if check == 3: msgg2 = music.country.d
        if check == 4: msgg2 = music.country.e
        if check == 5: msgg2 = music.country.f
        if check == 6: msgg2 = music.country.g
        if check == 7: msgg2 = music.country.h
        if check == 8: msgg2 = music.country.i
        if check == 9: msgg2 = music.country.j
        if check == 10: msgg2 = music.country.k
        await message.channel.send(msgg2+"\n>>>*Requested By* **"+str(message.author)+"**.<<<")

    if message.content.startswith('^music.rap') or message.content.startswith('^music.hiphop') or message.content.startswith('^play.hiphop') or message.content.startswith('^play.rap') or message.content.startswith('^music.hip') or message.content.startswith('^music.Rap') or message.content.startswith('^play.hip-hop') or message.content.startswith('^play.rap'):
        check = randint(0,14)
        if check == 1: msgg3 = music.rap_hip_hop.a
        if check == 2: msgg3 = music.rap_hip_hop.b
        if check == 2: msgg3 = music.rap_hip_hop.c
        if check == 3: msgg3 = music.rap_hip_hop.d
        if check == 4: msgg3 = music.rap_hip_hop.e
        if check == 5: msgg3 = music.rap_hip_hop.f
        if check == 6: msgg3 = music.rap_hip_hop.g
        if check == 7: msgg3 = music.rap_hip_hop.h
        if check == 8: msgg3 = music.rap_hip_hop.i
        if check == 9: msgg3 = music.rap_hip_hop.j
        if check == 10: msgg3 = music.rap_hip_hop.k
        if check == 11: msgg3 = music.rap_hip_hop.l
        if check == 12: msgg3 = music.rap_hip_hop.m
        if check == 13: msgg3 = music.rap_hip_hop.n
        if check == 14: msgg3 = music.rap_hip_hop.o
        await message.channel.send(msgg3+"\n>>>*Requested By* **"+str(message.author)+"**.<<<")

    if message.content.startswith('^music.rock') or message.content.startswith('^music.rockandroll') or message.content.startswith('^play.metal') or message.content.startswith('^play.Rock') or message.content.startswith('^music.american') or message.content.startswith('^music.roc') or message.content.startswith('^play.rock') or message.content.startswith('^play.rap'):
        check = randint(0,10)
        if check == 1: msgg4 = music.rock.a
        if check == 2: msgg4 = music.rock.b
        if check == 2: msgg4 = music.rock.c
        if check == 3: msgg4 = music.rock.d
        if check == 4: msgg4 = music.rock.e
        if check == 5: msgg4 = music.rock.f
        if check == 6: msgg4 = music.rock.g
        if check == 7: msgg4 = music.rock.h
        if check == 8: msgg4 = music.rock.i
        if check == 9: msgg4 = music.rock.j
        if check == 10: msgg4 = music.rock.k
        #if check == 11: msgg4 = music.rock.l
        #if check == 12: msgg4 = music.rock.m
        #if check == 13: msgg4 = music.rock.n
        #if check == 14: msgg4 = music.rock.o
        else: msgg4 = music.rock.h

        await message.channel.send(msgg4+"\n>>>*Requested By* **"+str(message.author)+"**.<<<")



        
    if message.content.startswith('^cloudflare.resolve') or message.content.startswith('^resolvecloudflare') or message.content.startswith('^resolve.cloudflare'):
        noot = message.content.split();clout=str(noot[1])
        await message.channel.send("**Attempting To Resolve"+clout+"...**")
        url2 = ('https://webresolver.nl/api.php?'
        'key=7JWS0-JJ5ZY-DK613-2PHB7&json&'
        'action=cloudflare&string='+clout);response = requests.get(url2);r = response.json();success = r['success']
        if success == True:
            old_stdout1 = sys.stdout;result1 = StringIO();sys.stdout = result1
            for r['domain'] in r['domains']:
                print(str(r['domain']))
                print()        
        elif success != True:
            await message.channel.send("**Host Could Not Be Resolved!**")    
        await message.channel.send("**Cloudflare Resolver**\n**Resolved Addresses For **"+clout+":\n```yaml\n"+str(result1.getvalue())+"\n```\n")
    if message.content.startswith('^skype') or message.content.startswith('^skyperesolver') or message.content.startswith('^resolve.skype') or message.content.startswith('^skyperesolve'):
        bleh1 = message.content.split();blehh1=str(bleh1[1])
        await message.channel.send("**Attempting To Resolve IP From **"+blehh1+"**!**\n")
        url2 = ('https://webresolver.nl/api.php?'
        'key=7JWS0-JJ5ZY-DK613-2PHB7&'
        f'json&action=resolve&string={blehh1}')
        response = requests.get(url2);r = response.json();success = r['success'];user = r['username'];error = r['error']
        if success == True:
            skype1 = str("""
**Skype Resolver Results For """+blehh1+"""**:**
```yaml

[Success]
USERNAME: """+str(user)+"""
IP: """+str(r)+"""
```
"""+str(error)+"\n")

        elif success != True:
            await message.channel.send("**IP Not Found In Database...**\n"+str(error))
        await message.channel.send(skype1)
        
    if message.content.startswith('^ip2skype') or message.content.startswith('^ip.skype') or message.content.startswith('^reverse.skype'):
        bleh = message.content.split();blehh=str(bleh[1])
        await message.channel.send("**Attempting To Resolve Username From **"+blehh+"**!**\n")
        url2 = ('https://webresolver.nl/api.php?'
        'key=7JWS0-JJ5ZY-DK613-2PHB7&'
        f'json&action=resolvedb&string={blehh}')
        response = requests.get(url2);r = response.json();success = r['success'];user = r['username'];error = r['error']
        if success == True:
            skype1 = str("""
**Skype Resolver Results For """+blehh+"""**:**
```yaml

[Success]
IP: """+str(blehh)+"""
USERNAME: """+str(user)+"""
```
"""+str(error)+"\n")

        elif success != True:
            await message.channel.send("**IP Not Found In Database...**")
        await message.channel.send(skype1)    

                
    if message.content.startswith('^evil.freeze') or message.content.startswith('^lag.gif') or message.content.startswith('!fuckthis') or message.content.startswith('^freeze'):
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif);time.sleep(.1)
        
    if message.content.startswith('^phonelookup') or message.content.startswith('^number') or message.content.startswith('^phone'):
        await message.channel.send("**Getting That For You...**")
        try:
            myliststrip1 = message.content.split();poop16=str(myliststrip1[1])
            if len(poop16) > 7:
                cc=str(poop16[(len(poop16) - 7)])
            else:
                cc = strings.null
            r=requests.get("http://apilayer.net/api/validate?access_key="+t_key+"&number="+poop16+"&country_code="+strings.null_+"&format="+cc+"")
            data = r.json();re_is_valid=data['valid'];re_num=data['number'];re_local_fmt=data['local_format'];re_int_fmt=data['international_format'];re_country_prfx=data['country_prefix'];re_country_code=data['country_code'];re_country_name=data['country_name']
            re_location=data['location'];re_carrier=str(data['carrier']);re_line_type=data['line_type']
            if re_is_valid == True:
                re_is_valid_char = "YES"
            elif re_is_valid == False:
                re_is_valid_char = "NO"
            load=str(strings.strip_1+re_is_valid_char+strings.strip_2+re_num+strings.strip_3+re_local_fmt+strings.strip_4+re_int_fmt+strings.strip_5)
            load2=str(re_country_prfx+strings.strip_6+re_country_code+strings.strip_7+re_country_name+strings.strip_8+re_location+strings.strip_9+re_line_type+strings.strip_10+re_carrier+strings.strip_11)
            await message.channel.send(str("**Phone Number Lookup For "+re_num+"/"+re_carrier+":**\n```yaml\n"+load+load2+"\n```\n>*Requested By* **"+str(message.author)+"**.<"))
        except Exception as ErE:
            #await message.channel.send("Debug: \n"+str(ErE))
            await message.channel.send("Error - Foreign Number Could Not Be Resolved!!!")
            
    if message.content.startswith('^hack') or message.content.startswith('^vuln') or message.content.startswith('^baby.vuln'):
                moop = message.content.split();tar = str(moop[1])
                await message.channel.send(f"**Hacking {tar}... ;)\n**")
                try:
                    re=requests.get('https://json.geoiplookup.io/' + tar)
                    data=re.json();re_ip = data['ip'];re_isp = data['isp'];re_org = data['org'];re_hostname = data['hostname'];re_city = data['city']
                    re_country = data['country_name'];re_asn = data['asn'];re_integ = data['success'];re_is_cached = data['cached'];re_curr = data['currency_code']
                    if re_is_cached == True: integ_char = 'True'
                    elif re_is_cached == False: integ_char = 'False'
                    if re_is_cached == True: cache_char = 'True'
                    elif re_is_cached == False: cache_char = 'False'
                    goods=str("""

                    *Getting Things Together For Your Testing....*

                    ```yaml
        ||Lixxard Bot Geo - Ip Lookup||

        Results For """+re_hostname+""":


        IP: """ + re_ip + """

        ISP: """ + re_isp + """

        ORG: """ + re_org + """

        HOSTNAME: """ + re_hostname + """

        CITY: """ + re_city + """

        COUNTRY: """ + re_country + """

        ASN: """ + re_asn + """

        SUCCESS: """ + integ_char + """

        CACHED: """ + cache_char + """

        CURRENCY: """ + re_curr + """

        INFO: Coming Soon!
                    ```
                    """+"\n*Requested By* **"+str(message.author)+"**.")
                except Exception:
                    await message.channel.send("Error! - Invalid Host...")
                try:
                    await message.channel.send(goods)
                except Exception: pass
                await message.channel.send(f"**Attempting To Resolve {tar}...**")
                url22 = ('https://webresolver.nl/api.php?'
                'key=7JWS0-JJ5ZY-DK613-2PHB7&json&'
                f'action=cloudflare&string={tar}');response1 = requests.get(url22);r1 = response1.json();success1 = r1['success']
                if success1 == True:
                    old_stdout11 = sys.stdout;result11 = StringIO();sys.stdout = result11
                    for r1['domain'] in r1['domains']:
                        print(str(r1['domain']))
                        print()
                    yeet = str(result11.getvalue())    
                    await message.channel.send(f"**Cloudflare Resolver**\n**Resolved Addresses For **{tar}:\n```yaml\n{yeet}\n```\n");time.sleep(2)  
                elif success1 != True:
                    await message.channel.send("*No Cloudflare Aliases Found, Moving On...*");time.sleep(2)    
                await message.channel.send(f"**Scanning Open Ports For {tar}...**")
                link12 = str('https://api.hackertarget.com/nmap/?q={}'.format(tar));rd1 = requests.get(link12)
                await message.channel.send("```yaml\n"+rd1.text+"\n```\n*Ok* **"+str(message.author)+"**!\n**Now Attempting http/https Vulns.!**\n")
                try:
                    user_agent0 = random.choice(lists.useragents)
                    headers0 = {'User-Agent' : user_agent0};url0=f"http://{tar}/js/"
                    t1 = requests.get(url0,headers=headers0);got=t1.text
                    await message.channel.send(f"**HTTP Check:**\n```html\n"+got+"\n```\n**Our User-Agent:** *"+str(user_agent0)+"*")
                except Exception:
                    await message.channel.send(f"**Failed Dump-Attempt @ http://{tar}/js/**\n**Our User-Agent:** *"+str(user_agent0)+"*")
                    pass
                time.sleep(2)
                try:
                    user_agent1 = random.choice(lists.useragents)
                    headers1 = {'User-Agent' : user_agent1};url1=f"https://{tar}/js/"
                    t2 = requests.get(url1,headers=headers1);got1=t2.text
                    await message.channel.send(f"**HTTPS Check:**\n```html\n"+got1+"\n```\n**Our User-Agent:** *"+str(user_agent1)+"*")
                except Exception:
                    await message.channel.send(f"Failed Dump-Attempt @ https://{tar}/['/?=1/or 1=1/?/html/bridge.html/auth0]\n**Our User-Agent:** *"+str(user_agent1)+"*")
                    pass
                await message.channel.send(f"\n**Possible Vuln @ http://{tar}/js/**\n**Possible Vuln @ https://{tar}/js/**");time.sleep(1)
                await message.channel.send("\n**Sweeping "+tar+", brb...**")
                myurl = ('https://webresolver.nl/api.php?'
                         'key=7JWS0-JJ5ZY-DK613-2PHB7&'
                         'html=0&'
                         'action=header&string='+str(tar))
                loadboi = requests.get(myurl);jboi=loadboi.text
                await message.channel.send(str(f'**Header Sweep For **{tar}\n```yaml\n{jboi}\n```\n')+str(f'\n\n**Standard Vulnerability Test Complete For {tar}!**\n*Requested By* **'+str(message.author)+"**."));time.sleep(1)
                
    #^proxies socks5            
#^proxies https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=7200&country=all
    if message.content.startswith('^list') or message.content.startswith('^proxies'):
        alist = message.content.split()
        bEE = False
        try:
            proxy_type = str(alist[1])
            proxy_timeout = str(alist[2])
            proxy_country = str(alist[3])
        except Exception as EEEE:
            #print(str(f"Debug\n```python\n{str(EEEE)}\n```\n"))
            await message.channel.send(str(f"Debug\n```python\n{str(EEEE)}\n```\n"))
            #(f"'**Correct Usage:** `^proxies <proxytype> <timeout> <country>` - Get Proxy List\n**Use ^proxy.help For More Info.**\n{outt}")
            bEE = True
            pass
        if bEE == False:
            try:
                usr_string = f"https://api.proxyscrape.com/?request=getproxies&proxytype={proxy_type}&timeout={proxy_timeout}&country={proxy_country}"
                shneef = requests.get(usr_string, allow_redirects=True, headers=user_agent.get_headers())
                print(shneef.text)
            except Exception as Ere:
                await message.channel.send(str(f"Debug\n```python\n{str(Ere)}\n```\n"))
                bEE == True
                
        if bEE == False:
            try:
                await message.channel.send(shneef.text)
            except Exception:
                pass

                
                
### Text Bold/Italic FORMAT

def bold_u(thing):#
    stuff = str(f"**__{thing}__**")
    return stuff

def bold(thing):#
    stuff = str(f"**{thing}**")
    return stuff

def italic(thing):
    stuff = str(f"*{thing}*")
    return stuff

def css(thing):
    stuff = str(f"```css\n{thing}```")
    return stuff
############################################

 
        
      
        
    
class user_agent:
    def get_headers():
        useragents = [
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/57.0.2987.110 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/61.0.3163.79 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
         'Gecko/20100101 '
         'Firefox/55.0'),  # firefox
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/61.0.3163.91 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/62.0.3202.89 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/63.0.3239.108 '
         'Safari/537.36'),  # chrome
        ]
        user_agent = choice(useragents)
        headers = {'User-Agent' : user_agent}
        return headers
    
client.run(settings.Token)
