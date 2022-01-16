import discord
import requests
import shutil
import os

'''

rsync -avz --exclude node_modules . pi@192.168.4.150:~/memebot

'''
activation = '.pepe'

def getMessage(message):
    return  message.content[5:]

def getMessageP(message):
    return  message.content[6:]
def saveIMG(url, name):
    r = requests.get(url, stream = True)

    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        #r.apparent_encoding

        # Open a local file with wb ( write binary ) permission.
        with open(name+'.gif', 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        return True
    else:
        return False
def saveIMGP(url, name, user):
    r = requests.get(url, stream = True)

    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        #r.apparent_encoding

        # Open a local file with wb ( write binary ) permission.
        with open(user+'/'+name+'.gif', 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        return True
    else:
        return False

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    channel = message.channel

    #print(message.author)
    if message.content.startswith('.ppepe'):
        user = str(message.author)
        if (os.path.exists(user)):
            pass
        else:
            os.makedirs(user)
        if message.content.startswith('.ppepe make'):
            sub = message.content.split()

            if saveIMGP(sub[3],sub[2],user):
                await channel.send('This gif is now known as |' + sub[2]+'| to the user |'+user+'|')
            else:
                await channel.send("Unable to download gif")
        elif message.content.startswith('.ppepe list'):
            ans=""
            for i in os.listdir(user):
                if i.endswith('.gif'):
                    ans+= (i[:-4]+', ')
                    
            await channel.send(ans)
        elif message.content=='.ppepe':
            pass
        elif message.content.startswith('.ppepe'):

            mes = getMessageP(message)

            #saveIMG(mes, "tester1", channel)
            #print(message.content)
            await channel.send(file=discord.File(user+'/'+mes+'.gif'))
            #await channel.send(".test")

    elif message.content.startswith('.pepe'):
        if message.content.startswith('.pepe make'):
            sub = message.content.split()

            if saveIMG(sub[3],sub[2]):
                await channel.send('This gif is now known as |' + sub[2]+'|')
            else:
                await channel.send("Unable to download gif")
        elif message.content.startswith('.pepe list'):
            ans=""
            for i in os.listdir():
                if i.endswith('.gif'):
                    ans+= (i[:-4]+', ')
            await channel.send(ans)
        elif message.content==activation:
            pass
        elif message.content.startswith(activation):

            mes = getMessage(message)

            #saveIMG(mes, "tester1", channel)
            #print(message.content)
            await channel.send(file=discord.File(mes+'.gif'))
            #await channel.send(".test")




client.run('OTI5MDg4MTY5OTYwNDE1MjYy.YdiOyQ.p4vZBL6hc0fc3EhrmD0xAlIOFdM')