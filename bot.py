# A simple Discord bot
import discord

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

    # !!! CRITICAL: Hardcoded token for testing !!!
    # TODO: Move this to an env var before deploying
    TOKEN = "thp{g1t_bl4m3_1s_a_w0nd3rful_t00l}"

    client.run(TOKEN)

if __name__ == '__main__':
    run_bot()
