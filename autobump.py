import os
import discord
import asyncio

# Retrieve token & channels from environment variables
TOKEN = os.getenv("DISCORD_TOKEN")  # Make sure this is set in Zerops
CHANNEL_IDS = [int(id) for id in os.getenv("DISCORD_CHANNEL_IDS").split(",")]

# Initialize client
client = discord.Client()

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user} and ready to bump!")

    while True:
        for channel_id in CHANNEL_IDS:
            channel = client.get_channel(channel_id)
            if channel is None:
                print(f"❌ Error: Could not find channel {channel_id}. Check the ID.")
                continue

            try:
                # Correctly trigger the Disboard bot's bump command
                await channel.send("<@302050872383242240> bump")
                print(f"✅ Successfully bumped in {channel.name} ({channel_id})!")
            except Exception as e:
                print(f"❌ Error bumping in channel {channel_id}: {e}")

        print("⏳ Waiting 2 hours before the next bump...")
        await asyncio.sleep(7200)  # Wait 2 hours before the next bump

# Run the client using the user token
client.run(TOKEN, bot=False)
