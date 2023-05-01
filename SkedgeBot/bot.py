import discord
import os
from dotenv import load_dotenv
import time
import random

load_dotenv()

client = discord.Client()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

client = discord.Client(intents=intents)
events = {("Test", "10:30am - 12:00pm", "CS 4384"), ("Group Project Due", "11:59pm - 11:59pm", "CS 3354"), ("Homework 4", "11:59pm - 11:59pm", "CS 3345")}
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_message(message):
	username = str(message.author).split("#")[0]
	channel = str(message.channel.name)
	user_message = str(message.content)
	
	print(f'Message {str(message.content)} by {username} on {channel}')
	
	if (message.author.bot):
		return

	if channel == 'bot':
		if user_message.lower() == "hello" or user_message.lower() == "hi":
			await message.channel.send(f'Hello {username}! Welcome to SkedgeBot. To know your daily events, please type `events` For a pomodoro timer, please type `pomodoro`')
			return
		elif user_message.lower() == "pomodoro":
			print("pomodoro")
			#await message.channel.send("How Many Cycles?")
			user_message = str(message.content)
			#num_cycles = int(float(user_message.lower()))
			print(user_message.lower())
			await message.channel.send("Begin Studying")
			time.sleep(18000) #actually 18000 for 30 minutes
			await message.channel.send("Begin Break")
			time.sleep(300) #actually 300 for 5 minutes
			await message.channel.send("Break Over")
		elif user_message.lower() == "events":
			event_string = "Here are your events\n"
			for i in (events):
				event_string += str(i) + '\n'
			await message.channel.send(event_string)

                
client.run(token)