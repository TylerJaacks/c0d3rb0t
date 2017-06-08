import discord
import asyncio
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sympy as sympify

from discord.ext.commands import Bot
from datetime import datetime

def create_plot(expression):
    fileName = datetime.now().strftime('%H%M%S') + ".png"

    x = np.array(range(0, 10))
    y = eval(expression)

    fig = plt.figure(1)
    plt.plot(x, y)

    plt.savefig("graphs\" + fileName)

    return fileName

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith('!graph'):
        expression = message.content[7:len(message.content)]
        fileName = create_plot(expression)

        with open(fileName, 'rb') as f:
            await client.send_file(message.channel, fileName)

client.run('MjczODc1NDcwMDM3MTU1ODQx.DBoTzQ.q5XaH1YAeSVnREqitLK2Qsqneoo')
