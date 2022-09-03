# bot discord
import discord
from discord.ext import commands
import random
import string

client = commands.Bot(command_prefix=".", help_command=None, intents = discord.Intents.all())

@client.event
async def on_ready():
    print("Bot online")

@client.command()
async def github(ctx):
    await ctx.reply("Hello user there is the github of the communiy : `https://github.com/lilkeep214`")


@client.command()
async def horza(ctx):
    await ctx.reply("Hello user there is the github of the communiy : `https://github.com/lilkeep214`")



@client.command()
async def support(ctx):
    embed = discord.Embed(title="Get support role", description="`discord.gg/2EqU3h8x`\n\n put this link in your " + '"about me"' + "\nand ask to <@905931030626697216>\nto get the role !")
    
    await ctx.reply(embed=embed)

@client.command()
async def invite(ctx):
    await ctx.reply("__DRS Shop__\n**join us here :**\nhttps://discord.gg/2EqU3h8x\nINVITE ME **https://discord.com/api/oauth2/authorize?client_id=1014538368887029892&permissions=8&scope=bot**")


@client.command()
async def gen(ctx):
    
    nitro = "" + "".join(random.choices(string.digits + string.ascii_letters, k=24))
    
    message = f"Hi user i tried to gen you a nitro !\nhttps://discord.gift/{nitro}"
    await ctx.reply(message)

@client.command()
async def help(ctx):
    embed = discord.Embed(title="👹 HELP 👹", description="__*This is just the alpha of the bot*__\n1- `.github` : get the github of the community\n2- `.gen` : try to get a nitro\n3- `.support` : put the link of the server in your bio and get the role **😈・SUPPORT**\n3- `.invite` : join the server\nBot code made by horza team.")
    await ctx.reply(embed=embed)
    
    
    

client.run("")
