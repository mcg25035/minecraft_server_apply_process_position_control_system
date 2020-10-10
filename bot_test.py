import discord
from discord.ext import commands
from discord.utils import get
import os
import random
bot = commands.Bot(command_prefix='')
client = discord.Client()
@bot.event

async def on_ready():
    print(">>Bot is Online<<")

@bot.command()
async def test(ctx,a: str):
    if a == '1':
        await ctx.send('你好 ， 應徵建築師的話，什麼時候有空進服應徵呢?')
    if a == '2':
        await ctx.send('你好 ， 應徵企劃員的話請把```題目```指定的內容上傳至__link__')
@bot.command()
async def 考試資料(ctx,a:int,b:int,c:int,e:str,f:str):
    if (b <= 0) or (b >= 13):
        await ctx.send(':x:輸入月份錯誤，可填的月份只有(1/2/3/4/5/6/7/8/9/10/11/12)')
    elif (b == 1) or (b == 3) or (b == 5) or (b == 7) or (b == 8) or (b == 10) or (b == 12)
        if (c <= 0) or (c >=32):
            await ctx.send(':x:輸入日期錯誤，(1/3/5/7/8/10)月可填的日期只有(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31)')
        else:
            if not os.path.isfile(ctx.message.author.id):
                await ctx.send(':x:你必須先輸入\n```我要應徵 <建築師/企劃師/材質包繪畫師>```')
            else:
                f = open('BotData/ctx.message.author.id'):
                temp_str = f.readline()
                if not temp_str == 'builder':
                    await ctx.send(':x:你目前的應徵階段不適用這類型的考試資料的填寫。')
                else:
                    
    elif (b == 2) or (b == 4) or (b == 6) or (b == 9) or (b == 11)
        if (c <= 0) or (c >=32):
            await ctx.send(':x:輸入日期錯誤，(2/4/6/9/11)月可填的日期只有(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31)')
        else:

@bot.command()
async def 我要應徵(ctx,a: str):
    if a == '建築師':
        if os.path.isfile('BotData/'+str(ctx.message.author.id)):
            await ctx.send(':x:你已經應徵通過或是已經在執行應徵過程，請先辭職或取消目前應徵後，在試一次。')
        else:
            f = open('BotData/'+str(ctx.message.author.id),'w+')
            f.write('builder\n')
            f.close()
            await ctx.send('請輸入可進服考試的時間及遊戲ID\n輸入格式: 考試資料 <年> <月> <日> <時段(早/下午/晚)> <遊戲ID>\n輸入範例:```考試資料 2020 8 7 早 coolshing```')
    elif a == '企劃師':
        if os.path.isfile('BotData/'+str(ctx.message.author.id)):
            await ctx.send(':x:你已經應徵通過或是已經在執行應徵過程，請先辭職或取消目前應徵後，在試一次。')
        else:
            f = open('BotData/'+str(ctx.message.author.id),'w+')
            f.write('planer\n')
            f.close()
            role = get(ctx.message.guild.roles, name="應徵中企劃師")
            await ctx.message.author.add_roles(role)
            temp_ranint = random.randint(1,5)
            if temp_ranint == 1:
                await ctx.send('請依照以下題目製作企劃文件，並提交於 <#764005024573423616> ```題目1```')
            elif temp_ranint == 2:
                await ctx.send('請依照以下題目製作企劃文件，並提交於 <#764005024573423616> ```題目2```')
            elif temp_ranint == 3:
                await ctx.send('請依照以下題目製作企劃文件，並提交於 <#764005024573423616> ```題目3```')
            elif temp_ranint == 4:
                await ctx.send('請依照以下題目製作企劃文件，並提交於 <#764005024573423616> ```題目4```')
            elif temp_ranint == 5:
                await ctx.send('請依照以下題目製作企劃文件，並提交於 <#764005024573423616> ```題目5```')
    elif a == '材質包繪畫師':
        if os.path.isfile('BotData/'+str(ctx.message.author.id)):
            await ctx.send(':x:你已經應徵通過或是已經在執行應徵過程，請先辭職或取消目前應徵後，在試一次。')
        else:
            f = open('BotData/'+str(ctx.message.author.id),'w+')
            f.write('texture_drawer\n')
            f.close()
    else:
        await ctx.send(':x:輸入的格式錯誤，可應徵的類型只有(建築師/企劃師/材質包繪畫師)\n輸入範例:```我要應徵 企劃師```')

@bot.command()
async def set(ctx,a: int):
    if os.path.isfile('BotData/'+str(a)):
        await ctx.author.send('很抱歉，這組ID已經被用過了，請換一個')
    else:
        f = open('BotData/'+str(a),'w+')
        temp_password=random.randint(0,2147483647)
        f.write(str(temp_password))
        await ctx.author.send('```您的應徵ID是'+str(a)+'\n您的應徵密碼是'+str(temp_password)+'\n在應徵過程中會頻繁用到，請熟記。```')
        
    

@bot.command()
async def a(ctx):
    await ctx.send('對')
bot.run('my bot token')
