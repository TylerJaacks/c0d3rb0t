import discord
import asyncio
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sympy as sympify
import requests

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

def load_keys():
    return tuple(open('token.txt', 'r'))

client = discord.Client()

token = load_keys()[0]
api = load_keys()[1]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        await client.send_message(message.channel, "!graph (expression) - To graph an expression, use np. for special functions and constansts. \n" + "\n" + "!eval (expression) - To evaluate an expression, use np. for special functions and constansts.")

    if message.content.startswith('!graph'):
        expression = message.content[7:len(message.content)]
        fileName = create_plot(expression)

        with open(fileName, 'rb') as f:
            await client.send_file(message.channel, fileName)

    if message.content.startswith('!eval'):
        expression = message.content[5:len(message.content)]

        await client.send_message(message.channel, eval(expression))

    if message.content.startswith("!wolfgram"):
        argument = message.content[9:]
        question = "+".join(argument.split())

        requestUrl = "http://api.wolframalpha.com/v1/simple?appid=" + api + "&i=" + question + "%3F"

        r = requests.get(requestUrl)
        r.status_code

        print(requestUrl)

client.run(token)
