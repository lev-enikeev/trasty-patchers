# redis://default:redispw@localhost:32768
import redis
import discord
from discord.ext import commands
from bot_token import API_TOKEN
from db import create_user, get_games_list


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
r = redis.Redis(host='localhost', 
                port=32768, 
                db=0, 
                username='default', 
                password='redispw',
                decode_responses=True,
                charset="utf-8")


r.delete('state')
@bot.command(name='sell')
async def test(ctx):
    r.set('state', 'sell-description')
    nikname = ctx.author.name + '#' + ctx.author.discriminator
    create_user(nikname, 1)
    await ctx.send('В какой игре вы хотите продать аккаунт?')
    

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if r.get('state') == 'sell-description':
        accounts = get_games_list()
        for account in accounts:
            if message.content == account:
                await message.channel.send('Введите описание')   
                return
            r.set('state', 'sell-price')
        await message.channel.send('Такой игры я не знаю')   
        return
    if r.get('state') == 'sell-price':
        await message.channel.send('Введите цену')   
        return

    await message.channel.send('Через меня можно продавать и покупать аккаунты в играх')   
    await bot.process_commands(message)


bot.run(API_TOKEN)