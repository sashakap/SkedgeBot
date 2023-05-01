from gettext import NullTranslations
import unittest
import discord
import os
from dotenv import load_dotenv
import time

client = discord.Bot()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

class WidgetTestCase(unittest.TestCase):
    @client.event
    async def setUp(self):
        user_message = str(self.message.content)
        assert self.message != NullTranslations
    
    @client.event
    async def tearDown(self):
        self.widget.dispose()
        self.widget = None

    @client.event
    async def testPomodoro1(self):
        assert self.message == ('!pomodoro'), 'Enter number of cycles' and self.message == ('1'); 'Invalid number of cycles'

    @client.event
    async def testPomodoro1(self):
        assert self.message == ('!pomodoro'), 'Enter number of cycles' and self.message == ('2'); 'Begin Studying'
        
    @client.event
    async def testEvents(self):
        self.widget.message = '!events'
        assert self.start == 'Here are your events'
    