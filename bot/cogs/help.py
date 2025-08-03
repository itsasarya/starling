from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} is ready.")

    @commands.slash_command(name="ping")
    async def ping(self, ctx):
        try:
            await ctx.respond(f"Pong {round(self.bot.latency * 100)}ms!")
        except Exception as e:
            print(f"command execution error: {e}")


def setup(bot):
    bot.add_cog(Help(bot))
