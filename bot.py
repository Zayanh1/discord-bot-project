# A simple Discord bot
import discord
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def run_bot():
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

    # Load token from environment variable
    TOKEN = os.environ.get("DISCORD_TOKEN")
    
    if not TOKEN:
        print("Error: DISCORD_TOKEN not found. Make sure to set it in your .env file.")
        return

    client.run(TOKEN)

if __name__ == '__main__':
    run_bot()
