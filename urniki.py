import discord
from discord.ext import commands

async def ponedeljek(ctx):
    embedVar = discord.Embed(title="Ponedeljek", description="Urnik za ponedeljek", color=0xFF0000)
    embedVar.add_field(name="8.00", value="Programiranje 1 - Vaje", inline=False)
    embedVar.add_field(name="9.00", value="Programiranje 1 - Vaje", inline=False)

    embedVar.add_field(name="10.00", value="Matematika v praksi - Predavanje", inline=False)
    embedVar.add_field(name="11.00", value="Matematika v praksi - Predavanje", inline=False)

    embedVar.add_field(name="12.00", value="Programiranje 1 - Predavanje", inline=False)
    embedVar.add_field(name="13.00", value="Programiranje 1 - Predavanje", inline=False)

    await ctx.send(embed=embedVar)

async def torek(ctx):
    embedVar = discord.Embed(title="Torek", description="Urnik za torek", color=0xFF0000)
    embedVar.add_field(name="8.00", value="Programiranje 1 - Vaje", inline=False)
    embedVar.add_field(name="9.00", value="Programiranje 1 - Vaje", inline=False)

    embedVar.add_field(name="11.00", value="Linearna algebra - Vaje", inline=False)
    embedVar.add_field(name="12.00", value="Linearna algebra - Vaje", inline=False)
    embedVar.add_field(name="13.00", value="Linearna algebra - Vaje", inline=False)

    embedVar.add_field(name="14.00", value="Matematika I - Predavanje", inline=False)
    embedVar.add_field(name="15.00", value="Matematika I - Predavanje", inline=False)

    await ctx.send(embed=embedVar)

async def sreda(ctx):
    embedVar = discord.Embed(title="Sreda", description="Urnik za sredo", color=0xFF0000)
    embedVar.add_field(name="8.00", value="Matematika I - Vaje", inline=False)
    embedVar.add_field(name="9.00", value="Matematika I - Vaje", inline=False)

    embedVar.add_field(name="10.00", value="Matematično izražanje v angleščini - Predavanje", inline=False)
    embedVar.add_field(name="11.00", value="Matematično izražanje v angleščini - Predavanje", inline=False)
    embedVar.add_field(name="12.00", value="Matematično izražanje v angleščini - Vaje", inline=False)
    embedVar.add_field(name="13.00", value="Matematično izražanje v angleščini - Vaje", inline=False)

    await ctx.send(embed=embedVar)

async def cetrtek(ctx):
    embedVar = discord.Embed(title="Četrtek", description="Urnik za četrtek", color=0xFF0000)
    embedVar.add_field(name="8.00", value="Matematika v praksi - Vaje", inline=False)
    embedVar.add_field(name="9.00", value="Matematika v praksi - Vaje", inline=False)

    embedVar.add_field(name="10.00", value="Linearna algebra - Predavanje", inline=False)
    embedVar.add_field(name="11.00", value="Linearna algebra - Predavanje", inline=False)
    embedVar.add_field(name="12.00", value="Linearna algebra - Predavanje", inline=False)

    embedVar.add_field(name="13.00", value="Matematika I - Vaje", inline=False)
    embedVar.add_field(name="14.00", value="Matematika I - Vaje", inline=False)

    embedVar.add_field(name="18.00", value="RP PRA - Vaje", inline=False)
    embedVar.add_field(name="19.00", value="RP PRA - Vaje", inline=False)

    await ctx.send(embed=embedVar)

async def petek(ctx):
    embedVar = discord.Embed(title="Petek", description="Urnik za petek", color=0xFF0000)
    embedVar.add_field(name="9.00", value="Matematika I - Predavanje", inline=False)
    embedVar.add_field(name="10.00", value="Matematika I - Predavanje", inline=False)

    embedVar.add_field(name="11.00", value="Računalniški praktikum - Predavanje", inline=False)

    await ctx.send(embed=embedVar)
