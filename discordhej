from discord.ext import commands
class HelloPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if "hej" in message.content.lower():
            await message.channel.send("Hej")
        elif "tja" in message.content.lower():
            await message.channel.send("Tjena!")
        elif "gm" in message.content.lower():
            await message.channel.send("God morgon")
        elif "gn" in message.content.lower():
            await message.channel.send("God natt")
        elif "god morgon" in message.content.lower():
            await message.channel.send("God morgon!")
        elif "god natt" in message.content.lower():
            await message.channel.send("God natt!")
        elif "hejsan" in message.content.lower():
            await message.channel.send("Hejsan!")
        elif "tjo" in message.content.lower():
            await message.channel.send("Tja")
        elif "wtf" in message.content.lower():
            await message.channel.send("Inte svära!")

def setup(bot):
    bot.add_cog(HelloPlugin(bot))
