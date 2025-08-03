import os
import random
import discord
import asyncio

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("No `Discord Token` environment variable found")

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

activities = [
    discord.Game("Assistant"),
    discord.Streaming(name="Help", url="https://starling.app"),
    discord.Activity(type=discord.ActivityType.watching, name="Over Server"),
    discord.Activity(type=discord.ActivityType.listening, name="Commands"),
    discord.Activity(type=discord.ActivityType.competing, name="With Others"),
]


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    bot.loop.create_task(change_status())


async def change_status():
    while True:
        activity = random.choice(activities)
        await bot.change_presence(activity=activity)
        delay = random.randint(30 * 60, 300 * 60)  # 30–300 minutes
        print(
            f"Changed status to {activity.name}, next change in {delay // 60} minutes"
        )
        await asyncio.sleep(delay)


def load_cogs():
    """Dynamically loads all cog"""
    cogs = [
        f"cogs.{filename[:-3]}"
        for filename in os.listdir("./bot/cogs/")
        if filename.endswith(".py")
    ]
    for cog in cogs:
        try:
            bot.load_extension(cog)
        except Exception as e:
            print(f"Failed to load extension {cog}. Error: {e}")


def run():
    try:
        load_cogs()
        bot.run(TOKEN)
    except Exception as e:
        print(f"Unable to run bot: {e}")


run()
