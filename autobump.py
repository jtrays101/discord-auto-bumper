import os
import discord
import asyncio
from discord.ext import commands

# Load token and channel IDs from environment variables
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_IDS = [int(id) for id in os.getenv("DISCORD_CHANNEL_IDS").split(",")]

# Enable bot with message sending permissions
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} and ready to bump!")
    await bump_loop()

async def bump_loop():
    while True:
        for channel_id in CHANNEL_IDS:
            channel = bot.get_channel(channel_id)
            if channel is None:
                print(f"❌ Error: Could not find channel {channel_id}. Check ID.")
                continue

            try:
                # Sending the /bump command as a raw message
                await channel.send("/bump")
                print(f"✅ Successfully sent `/bump` in channel {channel.name} ({channel_id})!")
            except Exception as e:
                print(f"⚠️ Error bumping in channel {channel_id}: {e}")

        print("⏳ Waiting 2 hours before the next bump...")
        await asyncio.sleep(7200)  # Wait 2 hours

# Run the bot
bot.run(TOKEN)
