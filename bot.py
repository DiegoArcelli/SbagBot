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
            
client.run('NDA0NjM2NDgwNTM1Nzg5NTg4.DUYvdw.XtucHpd7H7RTsSg9dWvx66JwZ6k')
