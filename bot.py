import discord
from discord.ext import commands
import os
import json
from datetime import date
import urniki as urniki


directory = os.path.dirname(__file__)

# Token import
f = open("./config.json".format(directory))

# For some fucking reason the upper code doesn't on Aiken's server so here we fucking go
# f = open("/home/aiken/lokarbot/config.json".format(directory))

config = json.loads(f.read())
f.close()

bot_token = config["token"]

bot_prefix = '!'
client = commands.Bot(command_prefix=bot_prefix)

async def getSchedule(ctx):
    if date.today().weekday() == 0:
        await urniki.ponedeljek(ctx)

    elif date.today().weekday() == 1:
        await urniki.torek(ctx)

    elif date.today().weekday() == 2:
        await urniki.sreda(ctx)
    
    elif date.today().weekday() == 3:
        await urniki.cetrtek(ctx)
    
    elif date.today().weekday() == 4:
        await urniki.petek(ctx)
    
    elif date.today().weekday() == 5:
        await ctx.send("Sobota je, nimaš pouka!")

    elif date.today().weekday() == 6:
        await ctx.send("Ker je nedelja, nimaš pouka. Pošiljam ti urnik za jutri, da se lahko pripraviš.")
        await urniki.ponedeljek(ctx)
    
    else:
        await ctx.send("Nevem kako je prišlo do tega, ampak ni noben dan v tednu")

async def urnikjutri(ctx):
    if date.today().weekday() == 0:
        await urniki.torek(ctx)

    elif date.today().weekday() == 1:
        await urniki.sreda(ctx)

    elif date.today().weekday() == 2:
        await urniki.cetrtek(ctx)
    
    elif date.today().weekday() == 3:
        await urniki.petek(ctx)
    
    elif date.today().weekday() == 4:
        await ctx.send("Jutri ni pouka KEKW")
    
    elif date.today().weekday() == 5:
        await ctx.send("Jutri ni pouka KEKW")

    elif date.today().weekday() == 6:
        await urniki.ponedeljek(ctx)
    
    else:
        await ctx.send("Nevem kako je prišlo do tega, ampak ni noben dan v tednu")


game = discord.Game('!pomoč')

@client.event
async def on_ready():
    await client.change_presence(activity=game)
    print('Locked and loaded')

#Kode za vsa predavanja posebaj  
      
#ROM
@client.command(aliases=['rp-p'])
async def rom(ctx):
    await ctx.send('``` Zoom koda za ROM je: ``` \n https://uni-lj-si.zoom.us/j/91758346929')
#LAP
@client.command()
async def lap(ctx):
    await ctx.send('``` Zoom koda za Linearno Algebro PREDAVANJE je: ``` \n https://uni-lj-si.zoom.us/j/197280368?pwd=UngrYmRjWHAxOEFoUjRmdU9GeDZOUT09')
#LAV
@client.command()
async def lav(ctx):
    await ctx.send('``` Zoom koda za Linearno Algebro VAJE je: ``` \n https://uni-lj-si.zoom.us/j/3838491224')
#MANGP
@client.command()
async def mangp(ctx):
    await ctx.send('``` Zoom koda za Matematično izražanje v angleškem jeziku PREDAVANJE je: ``` \n https://uni-lj-si.zoom.us/j/94943695256?pwd=M2dTZEZMV1BOZGxrNCtMTkYvV0JJQT09')
#MANGV
@client.command()
async def mangv(ctx):
    await ctx.send('``` Zoom koda za Matematično izražanje v angleškem jeziku VAJE je: ``` \n https://uni-lj-si.zoom.us/j/92869941735?pwd=WmpKdnNKcGlNTk5wQnJQOFpUdXNvZz09')
#MAT1P
@client.command()
async def mat1p(ctx):
    await ctx.send('``` Saksida ne uporablja stalne kode za zoom, ker je boomer. Kodo vsakič znova pošlje na mail. ```')
#MAT1V
@client.command()
async def mat1v(ctx):
    await ctx.send('``` Zoom koda za Matematiko 1 VAJE je: ``` \n https://fmf-uni-lj-si.zoom.us/j/96182315459?pwd=WUpiTmFFVzV6aEpoUHd0N1FPeEQ5QT09')
#FIZP
@client.command()
async def fizp(ctx):
    await ctx.send('``` Zoom koda za Uvod v fiziko PREDAVANJE je: ``` \n https://uni-lj-si.zoom.us/j/98398601616?pwd=bzdRNmpBQ0orMWZTV1o5cmw4WmVSQT09')
#FIZV
@client.command()
async def fizv(ctx):
    await ctx.send('``` Zoom koda za Uvod v fiziko VAJE je: ``` \n https://uni-lj-si.zoom.us/j/8605032776')
#PRO1P
@client.command()
async def pro1p(ctx):
    await ctx.send('``` Zoom koda za Programiranje 1 PREDAVANJE je: ``` \n https://uni-lj-si.zoom.us/j/95925502324?pwd=b2doU1h2YnVSa2F1STlMeU9PUEREZz09')
#PRO1V
@client.command()
async def pro1v(ctx):
    await ctx.send('``` Zoom koda za Programiranje 1 VAJE je: ``` \n https://uni-lj-si.zoom.us/j/98807101299?pwd=b1lxODM0aDdOZTdBYzhvMFk1WVhKQT09 ')



# Seznam vseh kod

rovm = 'Računalniški praktikum preadavanje: !rom'
ap = 'Linearna algebra predavanje: !lap'
av = 'Linearna algebra vaje: !lav'
angp = 'Mat. izražanje v Ang. jeziku predavanje: !mangp'
angv = 'Mat. izražanje v Ang. jeziku vaje: !mangv'
matp = 'Matematika 1 predavanje: !mat1p'
matv = 'Matematika 1 vaje: !mat1v'
uvfp = 'Matematika v praksi predavanje: !fizp'
uvfv = 'Matematika v praksi predavanje: !fizv'
prop = 'Programiranje 1 predavanje: !pro1p'
prov = 'Programiranje 1 vaje: !pro1v'

@client.command()
async def kode(ctx):
    await ctx.send('``` Izberi med: \n Predavanja - !predavanja \n Ali \n Vaje - !vaje ```') 

@client.command()
async def predavanja(ctx):
    await ctx.send('``` Računalniška ordoja v matematiki preadavanje: !rom \n Linearna algebra predavanje: !lap \n Mat. izražanje v Ang. jeziku predavanje: !mangp \n Matematika 1 predavanje: !mat1p \n Uvod v fiziko predavanje: !fizp \n Programiranje 1 predavanje: !pro1p```')

@client.command()
async def vaje(ctx):
    await ctx.send('``` Računalniška ordoja v matematiki vaje: !rom \n Linearna algebra vaje: !lav \n Mat. izražanje v Ang. jeziku vaje: !mangv \n Matematika 1 vaje: !mat1v \n Uvod v fiziko vaje: !fizv \n Programiranje 1 vaje: !pro1v ```')

#Urnik
@client.command()
async def udanes(ctx):
    await getSchedule(ctx)

@client.command()
async def ujutri(ctx):
    await urnikjutri(ctx)

@client.command()
async def urnik(ctx):
    await ctx.send('https://imgur.com/pi0YeXh')

@client.command()
async def cleanup(ctx):
    await ctx.send('\n.'* 50)
#Pomoč
@client.command()
async def pomoč(ctx):
    await ctx.send('``` Urnik za danes: !udanes \n Urnik za jutri: !ujutri \n Slika urnika: !urnik \n Zoom kode: !kode```')

client.run(bot_token)
