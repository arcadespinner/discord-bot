from discord.ext import commands

from dotenv import load_dotenv
import os

# Loads environment variables
load_dotenv()

class Administration(commands.Cog):
    # Initializes this class using a new instance of the running bot
    def __init__(self, bot):
        self.bot = bot

    # Called when the bot is logged in
    @commands.Cog.listener()
    async def on_ready(self):
        # Message that the bot sends each time it's online
        readyMsg = f'Hi! {self.bot.user.display_name} is now online!'

        # Retrieve the 'General' channel ID from the .env config file
        channelID = int(os.getenv('GENERAL_CHANNEL_ID'))

        # Send the message to the channel
        await self.bot.get_channel(channelID).send(readyMsg)

# Entry point of the bot's extension
async def setup(bot):
    # Add the administration cog to the bot to register listeners and commands
    await bot.add_cog(Administration(bot))