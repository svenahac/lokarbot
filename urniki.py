import discord
from discord.ext import commands

async def ponedeljek(ctx):
    embedVar = discord.Embed(title="Ponedeljek", description="Urnik za ponedeljek", color=0xFF0000)
    embedVar.add_field(name="8.00", value="Programiranje 1", inline=False)
    embedVar.add_field(name="9.00", value="Programiranje 1", inline=False)

    embedVar.add_field(name="10.00", value="Matematika v praksi", inline=False)
    embedVar.add_field(name="11.00", value="Matematika v praksi", inline=False)

    embedVar.add_field(name="12.00", value="Programiranje 1", inline=False)
    embedVar.add_field(name="13.00", value="Programiranje 1", inline=False)

    embedVar.add_field(name="16.00", value="Kolokviji 1P", inline=False)
    embedVar.add_field(name="17.00", value="Kolokviji 1P", inline=False)

    await ctx.send(embed=embedVar)

async def torek(ctx):
    embedVar = discord.Embed(title="Torek", description="Urnik za torek", color=0xFF0000)
    embedVar.add_field(name="8.00", value="Programiranje 1", inline=False)
    embedVar.add_field(name="9.00", value="Programiranje 1", inline=False)

    embedVar.add_field(name="11.00", value="Linearna algebra", inline=False)
    embedVar.add_field(name="12.00", value="Linearna algebra", inline=False)
    embedVar.add_field(name="13.00", value="Linearna algebra", inline=False)

    embedVar.add_field(name="14.00", value="Matematika I", inline=False)
    embedVar.add_field(name="15.00", value="Matematika I", inline=False)

    await ctx.send(embed=embedVar)

async def sreda(ctx):
    embedVar = discord.Embed(title="Sreda", description="Urnik za sredo", color=0xFF0000)
    embedVar.add_field(name="8.00", value="Matematika I", inline=False)
    embedVar.add_field(name="9.00", value="Matematika I", inline=False)

    embedVar.add_field(name="10.00", value="Matematično izražanje v angleščini", inline=False)
    embedVar.add_field(name="11.00", value="Matematično izražanje v angleščini", inline=False)
    embedVar.add_field(name="12.00", value="Matematično izražanje v angleščini", inline=False)
    embedVar.add_field(name="13.00", value="Matematično izražanje v angleščini", inline=False)

    await ctx.send(embed=embedVar)

async def cetrtek(ctx):
    embedVar = discord.Embed(title="Četrtek", description="Urnik za četrtek", color=0xFF0000)
    embedVar.add_field(name="8.00", value="Matematika v praksi", inline=False)
    embedVar.add_field(name="9.00", value="Matematika v praksi", inline=False)

    embedVar.add_field(name="10.00", value="Linearna algebra", inline=False)
    embedVar.add_field(name="11.00", value="Linearna algebra", inline=False)
    embedVar.add_field(name="12.00", value="Linearna algebra", inline=False)

    embedVar.add_field(name="13.00", value="Matematika I", inline=False)
    embedVar.add_field(name="14.00", value="Matematika I", inline=False)

    embedVar.add_field(name="18.00", value="RP PRA", inline=False)
    embedVar.add_field(name="19.00", value="RP PRA", inline=False)

    await ctx.send(embed=embedVar)

async def petek(ctx):
    embedVar = discord.Embed(title="Petek", description="Urnik za petek", color=0xFF0000)
    embedVar.add_field(name="9.00", value="Matematika I", inline=False)
    embedVar.add_field(name="10.00", value="Matematika I", inline=False)

    embedVar.add_field(name="11.00", value="Računalniški praktikum", inline=False)

    await ctx.send(embed=embedVar)