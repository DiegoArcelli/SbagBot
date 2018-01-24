import discord
import asyncio
import random
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!calc'):
        calc = message.content[6:]
        if "*" in calc:
            i = calc.index('*')
            calc = calc[:i-1] + " '*'" + calc[i+1:]
        x = os.popen("expr " + calc)
        ris = x.read()
        if(int(ris)>0):
            err = random.randint(-int(ris),int(ris));
        else:
            err = random.randint(int(ris),-int(ris));
        print(err)
        await client.send_message(message.channel,int(ris)+int(err))
    elif message.content.lower() == "ciao sbag":
        x = os.popen("wc -l < saluti")
        n = x.read()
        num = random.randint(1,int(n))
        file = open("saluti","r")
        cont = 0;
        for line in file:
            if cont == int(num):
                await client.send_message(message.channel, line)
            cont+=1
        file.close()
            
client.run('token')
