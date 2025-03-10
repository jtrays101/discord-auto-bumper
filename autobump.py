import os
import discord
import asyncio

# Get token & channels from environment variables
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_IDS = [int(id) for id in os.getenv("DISCORD_CHANNEL_IDS").split(",")]

client = discord.Client()

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user} and ready to bump!")

    while True:
        for channel_id in CHANNEL_IDS:
            channel = client.get_channel(channel_id)
            if channel is None:
                print(f"❌ Error: Could not find channel {channel_id}. Check ID.")
                continue
            try:
                await channel.send("!d bump")
                print(f"✅ Successfully bumped in {channel.name} ({channel_id})!")
            except Exception as e:
                print(f"⚠️ Error bumping in channel {channel_id}: {e}")

        print("⏳ Waiting 2 hours before the next bump...")
        await asyncio.sleep(7200)

client.run(TOKEN)
