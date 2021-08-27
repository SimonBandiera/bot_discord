import discord
from discord.message import Message
from tokens import secret_token
from discord.ext import commands

bot = commands.Bot(description ='My bot', command_prefix = "/")
@bot.event
async def on_ready():
    print("Ready")

async def main(ctx, extensions):
    messages = await ctx.channel.history(limit = 100).flatten()
    cs = 0
    for i in range(100):
        if messages[i].author == ctx.message.author and cs < 1:
            cs += 1
            await messages[i].delete()
        elif messages[i].author == ctx.message.author and cs == 1:
            await messages[i].delete()
            await ctx.send(f"```{extensions}\n{messages[i].content}```")
            break


@bot.command()
async def py(ctx):
    await main(ctx, "py")
        
@bot.command()
async def c(ctx):
    await main(ctx, "c")

@bot.command()
async def js(ctx):
    await main(ctx, "js")

@bot.command()
async def html(ctx):
    await main(ctx, "html")

@bot.command()
async def css(ctx):
    await main(ctx, "css")
        
    

bot.run(secret_token)