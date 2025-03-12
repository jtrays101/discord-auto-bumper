import discord
from discord.ext import commands
from discord.utils import get

client = discord.Client()

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user} and ready to bump!")

    # Get the channel where bumping happens
    for channel_id in CHANNEL_IDS:
        channel = client.get_channel(int(channel_id))
        if channel:
            try:
                # Send a simulated interaction (slash command)
                await channel.send("<@302050872383242240> bump")
                print(f"✅ Successfully bumped in {channel.name} ({channel_id})!")
            except Exception as e:
                print(f"❌ Error bumping in channel {channel_id}: {e}")

    print("⏳ Waiting 2 hours before the next bump...")
    await asyncio.sleep(7200)  # Wait 2 hours before next bump

client.run(TOKEN, bot=False)
