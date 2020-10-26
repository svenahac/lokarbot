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
      
#RPP
@client.command(aliases=['rp-p'])
async def rpp(ctx):
    await ctx.send('``` Zoom koda za Računalniški praktikum PREDAVANJE je: ``` \n https://uni-lj-si.zoom.us/j/97775158275')
#RPVL
@client.command()
async def rpvl(ctx):
    await ctx.send('``` Zoom koda za Računalniški praktikum VAJE-LIHI je: ``` \n https://uni-lj-si.zoom.us/j/99119331635')
#RPVS
@client.command()
async def rpvs(ctx):
    await ctx.send('``` Zoom koda za Računalniški praktikum VAJE-SODI je: ``` \n https://uni-lj-si.zoom.us/j/91777367872')
#LAP
@client.command()
async def lap(ctx):
    await ctx.send('``` Zoom koda za Linearno Algebro PREDAVANJE je: ``` \n https://uni-lj-si.zoom.us/j/197280368?pwd=UngrYmRjWHAxOEFoUjRmdU9GeDZOUT09')
#LAV
@client.command()
async def lav(ctx):
    await ctx.send('``` Zoom koda za Linearno Algebro VAJE je: ``` \n https://uni-lj-si.zoom.us/j/92420125807?pwd=TzZPM3MxeExBbFczRkp1R201ZEZyUT09')
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
#MVPP
@client.command()
async def mvpp(ctx):
    await ctx.send('``` Zoom koda za Matematiko v praksi PREDAVANJE je: ``` \n https://fmf-uni-lj-si.zoom.us/j/99734392447')
#MVPV
@client.command()
async def mvpv(ctx):
    await ctx.send('``` Zoom koda za Matematiko v praksi VAJE je: ``` \n https://fmf-uni-lj-si.zoom.us/j/99734392447')
#PRO1P
@client.command()
async def pro1p(ctx):
    await ctx.send('``` Zoom koda za Programiranje 1 PREDAVANJE je: ``` \n https://uni-lj-si.zoom.us/j/95925502324?pwd=b2doU1h2YnVSa2F1STlMeU9PUEREZz09')
#PRO1V
@client.command()
async def pro1v(ctx):
    await ctx.send('``` Zoom koda za Programiranje 1 VAJE je: ``` \n https://uni-lj-si.zoom.us/j/98807101299?pwd=b1lxODM0aDdOZTdBYzhvMFk1WVhKQT09 ')



# Seznam vseh kod

prakp = 'Računalniški praktikum preadavanje: !rpp'
prakvl = 'Računalniški praktikum vaje-lihi: !rpvl'
prakvs = 'Računalniški praktikum vaje-sodi: !rpvs'
ap = 'Linearna algebra predavanje: !lap'
av = 'Linearna algebra vaje: !lav'
angp = 'Mat. izražanje v Ang. jeziku predavanje: !mangp'
angv = 'Mat. izražanje v Ang. jeziku vaje: !mangv'
matp = 'Matematika 1 predavanje: !mat1p'
matv = 'Matematika 1 vaje: !mat1v'
mpp = 'Matematika v praksi predavanje: !mvpp'
mpv = 'Matematika v praksi vaje: !mvpv'
prop = 'Programiranje 1 predavanje: !pro1p'
prov = 'Programiranje 1 vaje: !pro1v'

@client.command()
async def kode(ctx):
    await ctx.send('``` Izberi med: \n Predavanja - !predavanja \n Ali \n Vaje - !vaje ```') 

@client.command()
async def predavanja(ctx):
    await ctx.send('``` Računalniški praktikum preadavanje: !rpp \n Linearna algebra predavanje: !lap \n Mat. izražanje v Ang. jeziku predavanje: !mangp \n Matematika 1 predavanje: !mat1p \n Matematika v praksi predavanje: !mvpp \n Programiranje 1 predavanje: !pro1p```')

@client.command()
async def vaje(ctx):
    await ctx.send('``` Računalniški praktikum vaje-lihi: !rpvl \n Računalniški praktikum vaje-sodi: !rpvs \n Linearna algebra vaje: !lav \n Mat. izražanje v Ang. jeziku vaje: !mangv \n Matematika 1 vaje: !mat1v \n Matematika v praksi vaje: !mvpv \n Programiranje 1 vaje: !pro1v ```')

#Urnik
@client.command()
async def udanes(ctx):
    await getSchedule(ctx)

@client.command()
async def ujutri(ctx):
    await urnikjutri(ctx)

@client.command()
async def urnik(ctx):
    await ctx.send('https://imgur.com/V4drmFy')

@client.command()
async def cleanup(ctx):
    await ctx.send('\n.'* 50)
#Pomoč
@client.command()
async def pomoč(ctx):
    await ctx.send('``` Urnik za danes: !udanes \n Urnik za jutri: !ujutri \n Slika urnika: !urnik \n Zoom kode: !kode```')

client.run(bot_token)
