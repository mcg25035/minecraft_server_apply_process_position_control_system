#program init
import discord
from discord.ext import commands
from discord.utils import get
from FTP import *
import os
import random
import keep_alive
REPAIR = False
topic_list = ['宇宙飛船,範例圖片:https://www.easyatm.com.tw/img/2/913/nBnauM3X1YjMxYTM1IzNykDM5ETMwADMwADMwADMwADMxAzL3IzL1YzLt92YucmbvRWdo5Cd0FmLwE2LvoDc0RHa.jpg','火星表面(包含地形),範例圖片:https://nimg.ws.126.net/?url=http%3A%2F%2Fcms-bucket.nosdn.127.net%2F140fe7c7e5cf4925b0f4527373f939ae20171221101241.jpeg&thumbnail=660x2147483647&quality=80&type=jpg','月球表面(包含地形),範例圖片:https://twgreatdaily.com/images/elastic/n5w/n5wxDm8BMH2_cNUg7nqU.jpg','太空站,範例圖片:https://hk.appledaily.com/resizer/qtHe26hBgAoEjKnnvLG_7FvWcsU=/720x405/filters:quality(100)/cloudfront-ap-northeast-1.images.arcpublishing.com/appledaily/GA4JQNIQ65EYXO5IEU5FCUUMDE.png']
job_list = ['建築師','企劃師','界面設計師']
#discord.py init
bot = commands.Bot(command_prefix='')
client = discord.Client()

@bot.event
async def on_ready():
    print(">>Bot is Online<<")
#@bot.command()
#async def admin_build_check(ctx):
@bot.command()
async def claimfile(ctx,a:str):
@bot.command()
async def 我蓋好了(ctx):
  if REPAIR == True:
    await ctx.send(':x:Sorry,bot is in maintenance,please try later.\n很抱歉，本機器人目前正在維護中，請稍後在嘗試此指令。')
  elif os.path.isfile(str(ctx.author.id)+'_DATA.botdata'):
    f = open(str(ctx.author.id)+'_DATA.botdata','r+')
    count = len(f.readlines())
    f.close()

    if count<3:
      await ctx.send(':middle_finger:不要唬爛，你根本沒有進去蓋。')
  else:
    await ctx.send(':middle_finger:不要唬爛，你根本沒有進去蓋。')
@bot.command()
async def username(ctx,a : str):
  if REPAIR == True:
    await ctx.send(':x:Sorry,bot is in maintenance,please try later.\n很抱歉，本機器人目前正在維護中，請稍後在嘗試此指令。')
  elif os.path.isfile(str(ctx.author.id)+'_DATA.botdata'):
    f = open('usernamelist','r+')
    b = f.read()
    b.split('\n')
    if a in b:
        await ctx.send(':x:你輸入的遊戲ID與他人重疊,或是你已經使用過本功能')
    elif b[0] == '建築師':
        f = open(str(ctx.author.id)+'_DATA.botdata','r+')
        c = f.read().split('\n')[0]
        f.close()
        f = open(str(ctx.author.id)+'_DATA.botdata','w')
        f.write(c+'\n'+a)
        f.close()
        f = open('usernamelist','r+')
        tt = f.read()+'\n'+a
        f.close()
        f = open('usernamelist','w')
        f.write(tt)
        f.close()
        await ctx.send(':white_check_mark:遊戲ID成功登記')
        nn = random.randint(1,2147483647)
        FTP(a,str(nn))
        user = await bot.fetch_user(ctx.author.id)
        await user.send('你的門禁密碼是'+str(nn)+'\n請牢記，進入伺服器會用到')
        await user.send('你可以在15分鐘後進入伺服器考試，ip為```qaz02546sd.servegame.com:64654```\n版本1.16.4')
        nn = random.randint(0,3)
        await user.send('你的考試題目為'+topic_list[nn])
        f = open(str(ctx.author.id)+'_DATA.botdata','r+')
        a2147483647 = f.read()
        a2147483647 = a2147483647 + '\n' + topic_list[nn]
        f.close()
        f = open(str(ctx.author.id)+'_DATA.botdata','w')
        f.write(a2147483647)
        f.close()
        await user.send('建造完成時，請回到［🔸］職位申請區 輸入```我蓋好了```')
  else:
     await ctx.send(':x:您目前的應徵流程並不支援登記遊戲ID的功能')
@bot.command()
async def clearmydata(ctx):
  if REPAIR == True:
    await ctx.send(':x:Sorry,bot is in maintenance,please try later.\n很抱歉，本機器人目前正在維護中，請稍後在嘗試此指令。')
  elif os.path.isfile(str(ctx.author.id)+'_DATA.botdata'):
    f = open(str(ctx.author.id)+'_DATA.botdata','r')
    fread = f.read()
    d = fread.split('\n')
    if len(d) >= 2:
      a = d[1]
      f.close()
      os.remove(str(ctx.author.id)+'_DATA.botdata')
      f = open('usernamelist','r+')
      fread = f.read()
      f.close()
      f = open('usernamelist','w')
      f.write(fread.replace('\n'+a,'').replace(a,''))
      f.close()
    else:
      f.close()
      os.remove(str(ctx.author.id)+'_DATA.botdata')

    await ctx.send(':white_check_mark:已重置!')
  else:
    await ctx.send(':white_check_mark:已重置!')
  
@bot.command()
async def 我要應徵(ctx,a : str):
  if REPAIR == True:
    await ctx.send(':x:Sorry,bot is in maintenance,please try later.\n很抱歉，本機器人目前正在維護中，請稍後在嘗試此指令。')
  elif os.path.isfile(str(ctx.author.id)+'_DATA.botdata'):
    await ctx.send(':x:應徵流程不可逆錯誤，請使用```clearmydata```重置跟你Discord帳戶連結的資料')
  elif a in job_list:
    f = open(str(ctx.author.id)+'_DATA.botdata','w+')
    f.write(a)
    f.close()
    await ctx.send(':thumbsup:好的,請輸入```username <你的遊戲ID>```來繼續應徵')
  else:
    await ctx.send(':x:我們目前沒有招收 '+a+' 這個職位，可以應徵的職位只有'+str(job_list).replace("'","").replace(",","、").replace("[","").replace("]",""))
keep_alive.keep_alive()
bot.run('NzYzNzYxNzA0MjIzMjQ0Mjk4.X38ahA.vMRlItu1EVjSbwmnipQRbCO3IV4')
