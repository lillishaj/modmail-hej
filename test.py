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
        elif "tjo" in message.content.lower():
            await message.channel.send("Tjo!")
        elif "gm" in message.content.lower():
            await message.channel.send("God morgon")
        elif "gn" in message.content.lower():
            await message.channel.send("God natt")
        elif "god morgon" in message.content.lower():
            await message.channel.send("God morgon!")
        elif "god natt" in message.content.lower():
            await message.channel.send("God natt!")
        elif "tjena" in message.content.lower():
            await message.channel.send("Tjena!")
        elif "wtf" in message.content.lower():
            await message.channel.send("Nää, inte svära!")
        elif "support" in message.content.lower():
            await message.channel.send("Support? DMa mig så löser jag alla problem som har uppstått!")

def setup(bot):
    bot.add_cog(HelloPlugin(bot))
