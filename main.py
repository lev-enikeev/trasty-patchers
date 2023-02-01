import discord
from bot_token import API_TOKEN
from discord.ext import commands
    
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

accounts = [' ', 'Minecraft', 'brawl stars']
state = None

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    if state == 'sell':
        for account in accounts:
            if message.content == account:
                await message.channel.send('Введите описание')   
                return
        await message.channel.send('Такой игры я не знаю')   

    await message.channel.send('Через меня можно продавать и покупать аккаунты в играх')   


@bot.command(name='sell')
async def test(ctx):
    global state
    state = 'sell'
    await ctx.send('В какой игре вы хотите продать аккаунт?')
    




bot.run(API_TOKEN)