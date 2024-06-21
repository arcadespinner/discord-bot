import discord
from discord.ext import commands
import os

from dotenv import load_dotenv

class Bot(commands.Bot):
    # Initializes this bot
    def __init__(self):
        super().__init__(
            # Bot will listen for commands with the '!' prefix
            command_prefix='!',
            # Run this bot with the default permissions
            intents = discord.Intents.default()
        )
    
    # Called when bot is being setup
    async def setup_hook(self):
        # Load the administration extension to register bot commands/listeners
        await self.load_extension('administration')

# Loads environment variables
# NOTE: These are defined in a file named '.env' in the CURRENT directory
load_dotenv()

# Get the authentication token
TOKEN = os.getenv('DISCORD_TOKEN')

# Have the bot start listening for incoming commands using the Discord token
Bot().run(TOKEN)