import discord
import asyncio
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sympy as sympify

from discord.ext.commands import Bot
from datetime import datetime
from math import sin, cos, tan

def create_plot(expression):
    fileName = "graphs/" + datetime.now().strftime('%H%M%S') + ".png"

    x = np.array(range(-50, 50))
    y = eval(expression)

    fig = plt.figure(1)

    fig.suptitle("The graph of " + expression, fontsize=20)

    plt.xlabel('X', fontsize=18)
    plt.ylabel('Y', fontsize=18)

    plt.plot(x, y)
    plt.savefig(fileName)
    plt.clf()

    return fileName

def str_to_int(s):
    ctr = i = 0
    for c in reversed(s):
        i += (ord(c) - 48) * (10 ** ctr)
        ctr += 1
    return i

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

    if message.content.startswith('!eval'):
        expression = message.content[5:len(message.content)]

        await client.send_message(message.channel, eval(expression))

client.run('MjczODc1NDcwMDM3MTU1ODQx.DBoTzQ.q5XaH1YAeSVnREqitLK2Qsqneoo')
