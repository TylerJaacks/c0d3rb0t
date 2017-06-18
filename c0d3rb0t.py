import discord
import asyncio
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sympy as sympify
import wolframalpha

from discord.ext.commands import Bot
from datetime import datetime
from math import sin, cos, tan

def load_keys():
    return tuple(open('tokens.txt', 'r'))

# TODO Add more np.* replaces
def npReplace(message):
    return message.replace("sin", "np.sin").replace("cos", "np.cos").replace("tan", "np.tan").replace("pi", "np.pi")

# TODO Fix Trig Functions
def create_plot(expression, xMin, xMax, xStep, title, xLabel, yLabel):
    fileName = "graphs/" + datetime.now().strftime('%H%M%S') + ".png"

    x = np.array(np.arange(xMin, xMax, xStep))
    y = eval(expression)

    fig = plt.figure(1)

    fig.suptitle(title, fontsize=20)

    plt.xlabel(xLabel, fontsize=18)
    plt.ylabel(yLabel, fontsize=18)

    plt.plot(x, y)
    plt.savefig(fileName)
    plt.clf()

    return fileName

token = load_keys()[0].replace("\n", "")
api_key = load_keys()[1].replace("\n", "")

discord = discord.Client()
#TODO Load key from a file.
wolframalpha = wolframalpha.Client('23643R-YHA7P9UH8R')

@discord.event
async def on_ready():
    print('Logged in as')
    print('Discord User Name: ' + discord.user.name)
    print('Discord User Id: ' + discord.user.id)
    print('Discord Bot Token: ' + token)
    print('Wolfram Alpha API Key: ' + api_key)

@discord.event
async def on_message(message):
    messageSplit = message.content.split()

    if message.content.startswith('!help'):
        graph = "!graph (expression) xMin xMax xStep Title xLabel yLabel - To graph an expression, use np. for special functions and constansts.\n"
        eval = "!eval (expression) - To evaluate an expression, use np. for special functions and constansts.\n"
        wolfram = "!wolframalpha question to answer any question using Wolfram Alpha.\n"
        help = graph + "\n" + eval + "\n" + wolfram

        await discord.send_message(message.channel, help)

    if message.content.startswith('!graph'):
        expression = messageSplit[1]
        simpified_expression = npReplace(messageSplit[1])
        print(simpified_expression)
        xMin = int(messageSplit[2])
        xMax = int(messageSplit[3])
        xStep = int(messageSplit[4])
        title = "The graph of " + expression #str(messageSplit[5])
        xLabel = "X" #int(messageSplit[6])
        yLabel = "Y" #int(messageSplit[7])

        fileName = create_plot(simpified_expression, xMin, xMax, xStep, title, xLabel, yLabel)

        with open(fileName, 'rb') as f:
            await discord.send_file(message.channel, fileName)

    if message.content.startswith('!eval'):
        expression = message.content[5:len(message.content)]

        await discord.send_message(message.channel, eval(expression))

    if message.content.startswith("!wolframalpha"):
        argument = message.content[9:]

        res = wolframalpha.query(argument)

        await discord.send_message(message.channel, next(res.results).text)

discord.run(str(token))