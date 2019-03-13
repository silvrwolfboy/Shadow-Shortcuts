from discord.ext import commands
import discord


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.general = self
        bot.logger.info("Initialized General Cog")

    @commands.command(description="Send instructions on how to get Verified")
    async def verify(self, ctx, *, user: discord.Member = None):
        """How to get verified command."""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Verify command received from {author.name} with argument of {user}".format(author=ctx.author,
                                                                                            user=user))
            if user is not None:
                await ctx.send(
                    "From: {author.name}\n{user} To get verified Please DM a Shadow Guru or a Moderator a screenshot of https://account.shadow.tech/subscription to get your Shadower role".format(
                        author=ctx.message.author, user=user.mention))
            else:
                await ctx.send(
                    "From: {author.name}\nTo get verified Please DM a Shadow Guru or a Moderator a screenshot of https://account.shadow.tech/subscription to get your Shadower role".format(
                        author=ctx.message.author))
        await ctx.message.delete()

    @commands.command(description="800x600 instructions", name="800x600")
    async def _800x600(self, ctx, *, user: discord.Member = None):
        """800x600 Information (red square)"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info("Waiting for video command received from {author.name} with argument of {user}".format(
                author=ctx.message.author, user=user))
            if user is not None:
                await ctx.send(
                    "From {author.name}\n{user} Please see the following to fix issues with 800x600 resolution http://core.stavlor.net/800x600.png".format(
                        author=ctx.message.author, user=user.mention))
            else:
                await ctx.send(
                    "From {author.name}\nPlease see the following to fix issues with 800x600 resolution http://core.stavlor.net/800x600.png".format(
                        author=ctx.message.author))
        else:
            self.bot.logger.info(
                "Waiting for video command received from unauthorized user {author.name}, replied via PM. ".format(
                    author=ctx.message.author,
                    user=user))
            await ctx.author.send(
                content="""{user} Please see the following to fix issues with 800x600 resolution http://core.stavlor.net/800x600.png""".format(
                    user=ctx.author.mention))
        await ctx.message.delete()

    @commands.command(description="Waiting for video instructions", aliases=['waitingforvideo', 'wfv'])
    async def waitingvideo(self, ctx, *, user: discord.Member = None):
        """Waiting for Video information"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info("Waiting for video command received from {author.name} with argument of {user}".format(
                author=ctx.message.author, user=user))
            if user is not None:
                await ctx.send(
                    "From {author.name}\n{user} Please see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png".format(
                        author=ctx.message.author, user=user.mention))
            else:
                await ctx.send(
                    "From {author.name}\nPlease see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png".format(
                        author=ctx.message.author))
        else:
            self.bot.logger.info(
                "Waiting for video command received from unauthorized user {author.name}, replied via PM. ".format(
                    author=ctx.message.author,
                    user=user))
            await ctx.author.send(
                content="""{user}  Please see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png""".format(
                    user=ctx.author.mention))
        await ctx.message.delete()

    @commands.command(description="Error 102 Fix.", aliases=['error102'])
    async def fix102(self, ctx, *, user: discord.Member = None):
        """Error 102 Information"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "102 command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                         user=user))
            if user is not None:
                await ctx.send(
                    "From: {author.name}\n{user} Please follow the following instructions to resolve error 102: http://core.stavlor.net/fix_102.png".format(
                        author=ctx.message.author, user=user.mention))
            else:
                await ctx.send(
                    "From: {author.name}\nPlease follow the following instructions to resolve error 102: http://core.stavlor.net/fix_102.png".format(
                        author=ctx.message.author))
        else:
            self.bot.logger.info("Error 102 Fix command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.message.author,
                user=user))
            await ctx.author.send(
                content="""{user} Please follow the following instructions to resolve error 102: http://core.stavlor.net/fix_102.png""".format(
                    user=ctx.author.mention))
        await ctx.message.delete()

    @commands.command(description="Default pass")
    async def password(self, ctx, user: discord.Member = None):
        """Default Password help for Ready-to-Go Shadow Images"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Password command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                              user=user))
            if user is not None:
                await ctx.send(
                    "From: {author.name}\n{user} Please see the following for expired password messages http://core.stavlor.net/password.png".format(
                        author=ctx.message.author, user=user.mention))
            else:
                await ctx.send(
                    "From: {author.name}\nPlease see the following for expired password messages http://core.stavlor.net/password.png".format(
                        author=ctx.message.author))
        else:
            self.bot.logger.info("Password command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.message.author))
            await ctx.author.send(
                content="{user} Please see the following for expired password messages http://core.stavlor.net/password.png".format(
                    user=ctx.message.author.mention))
        await ctx.message.delete()

    @commands.command(description="microphone fix")
    async def micfix(self, ctx, *, user: discord.Member = None):
        """Microphone fix information."""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Mic Fix command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                             user=user))
            if user is not None:
                await ctx.send(
                    "From: {author.name}\n{user.mention} To get your microphone working in Shadow please follow this guide: "
                    "https://wiki.shadow.pink/index.php/Using_a_Microphone".format(author=ctx.author,
                                                                                   user=user))
            else:
                await ctx.send(
                    "From: {author.name}\nTo get your microphone working in Shadow please follow this guide: "
                    "https://wiki.shadow.pink/index.php/Using_a_Microphone".format(author=ctx.author,
                                                                                   user=user))
        else:
            self.bot.logger.info("Mic Fix command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.author,
                user=user))
            await ctx.author.send(content="""{user} To get your microphone working in Shadow please follow this guide: "
                          "https://wiki.shadow.pink/index.php/Using_a_Microphone""".format(user=ctx.author.mention))
        await ctx.message.delete()

    @commands.command()
    async def ghostmanual(self, ctx, *, user: discord.Member = None):
        """Send Link to Ghost Manual"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Ghost manual command received from {author.name} with argument of {user}".format(
                    author=ctx.message.author,
                    user=user))
            if user is not None:
                await ctx.send(
                    "From: {author.name}\n{user} Ghost Manual: http://core.stavlor.net/Ghost_Manual.pdf".format(
                        author=ctx.message.author, user=user))
            else:
                await ctx.send("From: {author.name}\nGhost Manual: http://core.stavlor.net/Ghost_Manual.pdf".format(
                    author=ctx.message.author))
        else:
            self.bot.logger.info("Ghost Manual command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.author,
                user=user))
            await ctx.author.send("""{user} Shadow Ghost Manual http://core.stavlor.net/Ghost_Manual.pdf""".format(
                user=ctx.author.mention))
        await ctx.message.delete()

    @commands.command(description="Latency command")
    async def latency(self, ctx, *, user: discord.Member = None):
        """Input lag/Latency Information"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Latency command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                             user=user))
            if user is not None:
                await ctx.send(
                    """From {author.name}\n{user} Common steps for fixing input latency http://core.stavlor.net/inputlag.png""".format(
                        author=ctx.author, user=user.mention))
            else:
                await ctx.send(
                    """From {author.name}\nCommon steps for fixing input latency http://core.stavlor.net/inputlag.png""".format(
                        author=ctx.author))
        else:
            await ctx.author.send(
                """{user} Common steps for fixing input latency http://core.stavlor.net/inputlag.png""".format(
                    user=ctx.author.mention))
            self.bot.logger.info("Latency command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.author,
                user=user))
        await ctx.message.delete()

    @commands.command(description="Speedtest-Links")
    async def speedtest(self, ctx, *, user: discord.Member = None):
        """Speedtest Links"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info("Speedtest command received from {author.name} with argument of {user}".format(
                author=ctx.message.author,
                user=user))
            if user is not None:
                await ctx.send("""From {author.name}\n{user} Speedtest.net links
    NORTH AMERICA
    Midwest DC(Chicago): <http://www.speedtest.net/server/14489>
    Central DC(Texas): <http://www.speedtest.net/server/12190>
    East DC(NY): <http://www.speedtest.net/server/22774>
    West DC(CA): <http://www.speedtest.net/server/11599>""".format(author=ctx.author, user=user.mention))
            else:
                await ctx.send("""From {author.name}\nSpeedtest.net links
                NORTH AMERICA
                Midwest DC(Chicago): <http://www.speedtest.net/server/14489>
                Central DC(Texas): <http://www.speedtest.net/server/12190>
                East DC(NY): <http://www.speedtest.net/server/22774>
                West DC(CA): <http://www.speedtest.net/server/11599>""".format(author=ctx.author))
        else:
            await ctx.author.send("""{user} Speedtest.net links
    NORTH AMERICA
    Midwest DC(Chicago): <http://www.speedtest.net/server/14489>
    Central DC(Texas): <http://www.speedtest.net/server/12190>
    East DC(NY): <http://www.speedtest.net/server/22774>
    West DC(CA): <http://www.speedtest.net/server/11599>""".format(user=ctx.author.mention))
            self.bot.logger.info("Speedtest command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.message.author,
                user=user))
        await ctx.message.delete()

    @commands.command()
    async def tos(self, ctx, *, user: discord.Member = None):
        """Send Terms of Service information"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "TOS command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                         user=user))
            if user is not None:
                await ctx.send("""From: {author.name}\n{user}  **__whether it's in the ToS or not__**, **we ask that you respect other's intellectual properties while using Shadow, and that covers piracy and cheating.**
    __READ THE TOS__
    https://shadow.tech/usen/terms
    https://help.shadow.tech/hc/en-gb/articles/360000455174-Not-allowed-on-Shadow""".format(author=ctx.author,
                                                                                            user=user.mention))
            else:
                await ctx.send("""From: {author.name}\n**__whether it's in the ToS or not__**, **we ask that you respect other's intellectual properties while using Shadow, and that covers piracy and cheating.**
                __READ THE TOS__
                https://shadow.tech/usen/terms
                https://help.shadow.tech/hc/en-gb/articles/360000455174-Not-allowed-on-Shadow""".format(
                    author=ctx.author))
        await ctx.message.delete()

    @commands.command(aliases=['drivers'])
    async def nvidiadrivers(self, ctx, *, user: discord.Member = None):
        """Send current NVidia Drivers Info."""
        text = """**Current Nvidia Drivers for P5000** -- [__*US has only P5000s*__] [__*Non-US users may have GTX1080*__]
          - Stable Drivers *(**Recommended**)*:  <https://www.nvidia.com/Download/driverResults.aspx/143118/en-us>
          - Vulkan Drivers *(**Optional**)*: <https://developer.nvidia.com/vulkan-beta-41934-windows-10>

        **Notes:**
          - Vulkan drivers will generally have the best performance but may have issues.
          - Driver installation can potentially glitch the streamer, so __***prior to installation***__ ensure you have an alternate way to access Shadow. Chrome Remote Desktop is recommended for this <https://remotedesktop.google.com/access/>
          - If the stream cuts out, your first attempt to fix the issue should be to restart streaming from the launcher."""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Nvidia Drivers command received from {author.name} with argument of {user}".format(
                    author=ctx.author,
                    user=user))
            if user is not None:
                text = """From: {author.name}\n{user}\n""" + text
                await ctx.send(
                    text.format(
                        author=ctx.author, user=user.mention))
            else:
                text = """From: {author.name}\n""" + text
                await ctx.send(text.format(author=ctx.author))
        else:
            self.bot.logger.info(
                "NVidia Drivers command received from un-privileged user {ctx.author.name} Responding Via PM".format(
                    ctx=ctx))
            text = """{user}\n""" + text
            await ctx.author.send(
                text.format(
                    user=ctx.author.mention))
        await ctx.message.delete()

    @commands.command(aliases=['purchaseghost'])
    async def buyghost(self, ctx, *, user: discord.Member = None):
        """Ghost Purchase information."""
        if user is None:
            self.bot.logger.info("Ghost purchase info command processed for {author.name}".format(author=ctx.message.author))
            await ctx.send(
                "{author.mention} you can purchase ghost from your account page, https://account.shadow.tech/subscription".format(
                    author=ctx.author))
            await ctx.message.delete()
        else:
            if await self.bot.admin.can_run_command(ctx.author.roles):
                self.bot.logger.info("Ghost purchase info command processed for {author.name} and args {user}".format(
                    author=ctx.author, user=user))
                await ctx.send(
                    """From: {author.name}\n{user} you can purchase Shadow Ghost from your account page,  https://account.shadow.tech/subscription""".format(
                        author=ctx.author, user=user.mention))
                await ctx.message.delete()

    @commands.command(description="Send ghost informational link")
    async def ghostinfo(self, ctx, *, user: discord.Member = None):
        """Give Ghost information link."""
        if user is None:
            self.bot.logger.info("Ghost info command processed for {author.name}.".format(author=ctx.author))
            await ctx.send(
                "{author.mention} Ghost information can be found here, https://shadow.tech/usen/discover/shadow-ghost".format(
                    author=ctx.author))
            await ctx.message.delete()
        else:
            if await self.bot.admin.can_run_command(ctx.author.roles):
                self.bot.logger.info(
                    "Ghost info command processed for {author.name} with args {user}".format(author=ctx.author,
                                                                                             user=user))
                await ctx.send(
                    """From: {author.name}\n{user.mention} Ghost information can be found here, https://shadow.tech/usen/discover/shadow-ghost""".format(
                        author=ctx.author, user=user))
                await ctx.message.delete()

    @commands.command(description="Status command")
    async def status(self, ctx, *, user: discord.Member = None):
        """Reports current shadow status"""
        if user is None:
            self.bot.logger.info("Status command processed for {author.name}.".format(author=ctx.message.author))
            if await self.bot.admin.get_status() == "All Systems Operational":
                embed = discord.Embed(title="Shadow Status", url="https://status.shadow.tech", color=0x00ff00)
                embed.add_field(name="All Systems Normal",
                                value="For additional status information please see the status page", inline=True)
                await ctx.send(embed=embed)
                await ctx.message.delete()
            else:
                status = await self.bot.admin.get_status()
                embed = discord.Embed(title="Shadow Status", url="https://status.shadow.tech", color=0xff8040)
                embed.add_field(name=status,
                                value="For additional status information please see the status page", inline=True)
                await ctx.send(embed=embed)
                await ctx.message.delete()
        else:
            if await self.bot.admin.can_run_command(ctx.author.roles):
                self.bot.logger.info("Status command processed for {author.name} with args {user}".format(author=ctx.author,
                                                                                                 user=user))
                await ctx.send(
                    "From {author.name}\n{user.mention} Current Shadow network status is {status}. For more info see https://status.shadow.tech".format(
                        author=ctx.author, user=user, status=await self.bot.admin.get_status()))
                await ctx.message.delete()

    @commands.command(description="Bot Logs")
    async def logs(self, ctx):
        """Logs Command"""
        if await self.bot.admin.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            fname = 'discord.log'
            lines = await self.bot.admin.tail(filename=fname, lines=50)
            lines = lines.split("\n")
            paginator = commands.Paginator(prefix="```python")
            for line in lines:
                paginator.add_line(line)
            if not (ctx.channel.name == 'gurus-lab') and not (ctx.channel.name == 'bot-talk'):
                await ctx.author.send("Here is the last few lines of the log:")
                for page in paginator.pages:
                    await ctx.author.send(page)
                self.bot.logger.info(
                    "Sending last few log entries to {ctx.author.name} via PM as its not in gurus-lab channel was {ctx.channel.name}".format(ctx=ctx))
            else:
                await ctx.send("Here is the last few lines of the log:")
                for page in paginator.pages:
                    await ctx.send(page)
                await ctx.message.delete()
                self.bot.logger.info("Sending last few log entries to Channel Requestor:{ctx.author}.".format(ctx=ctx))
        else:
            await ctx.send("Sorry {ctx.author.mention} your not authorized to do this.".format(ctx=ctx))
            await ctx.message.delete()
            self.bot.logger.info("Unauthorized log request from {ctx.author}".format(ctx=ctx))

    @commands.command(description="PM test")
    async def pmtest(self, ctx):
        """PM Debug command"""
        if await self.bot.admin.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            await ctx.author.send("Test")
            await ctx.message.delete()
        else:
            await ctx.send("Sorry {ctx.author.mention} your not authorized to do this.".format(ctx=ctx))
            await ctx.message.delete()
            self.bot.logger.info("Unauthorized pmtest request from {ctx.author}".format(ctx=ctx))

    @commands.command()
    async def userinfo(self, ctx, *, user: discord.Member):
        """Look up general user info."""
        rolelist = ""
        if not await self.bot.admin.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            await ctx.send("{ctx.author.mention} your not authorized to do that.".format(ctx=ctx))
            return
        paginator = discord.ext.commands.Paginator(prefix='```css', suffix='```')
        paginator.add_line("User-ID: {user.id}".format(user=user))
        for role in user.roles:
            rolelist += "{role.name}({role.id}) ".format(role=role)
        paginator.add_line("Has roles: {roles}".format(roles=rolelist))
        joinedat = user.joined_at.strftime('%Y-%m-%d %H:%M:%S')
        createdat = user.created_at.strftime('%Y-%m-%d %H:%M:%S')
        paginator.add_line("Joined on: {joinedat}".format(joinedat=joinedat))
        paginator.add_line("Created at {createdat}".format(createdat=createdat))
        paginator.add_line("Username+discriminator: {user}".format(user=user))
        paginator.add_line("Display name: {user.display_name}".format(user=user))
        paginator.add_line("Status: {user.status}".format(user=user))
        for page in paginator.pages:
            await ctx.send(page)

    @commands.command()
    async def minreq(self, ctx, *, user=None):
        """Give Shadow Minimum requirements"""
        self.bot.logger.info(
            "Minreq received from {author.name} with argument of {user}".format(
                author=ctx.author,
                user=user))
        text = """:warning:  MINIMUM REQUIREMENTS :warning: 

        **Windows**
        - Windows 7 - 32 bits or above
        - Processor from 2011-2012 or more recent
        - Integrated GPU recommended
        - AMD GPU from 2013 or more recent (to disable if older)
        - Nvidia GPU from 2011 and more recent (to disable if older)
        
        **Mac**
        - Mac OS 10.10 Yosemite or above
        - Mac device from 2012 or more recent"""
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = "From {ctx.author.name}\n{user.mention} " + text
            await ctx.send(text.format(ctx=ctx, user=user))
            await ctx.message.delete()
        elif user is None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = "From {ctx.author.name}\n"+ text
            await ctx.send(text.format(ctx=ctx))
            await ctx.message.delete()
        else:
            ctx.author.send(text)
            await ctx.message.delete()

    @commands.command()
    async def ping(self, ctx):
        """Ping command"""
        import datetime
        now = datetime.datetime.now()
        delta = (now - ctx.message.created_at).total_seconds()*1000
        await ctx.send('Pong! Server ping {:.3f}ms API ping: {:.3f}ms :ping_pong:'.format(delta, self.bot.latency*1000))

    @commands.command(aliases=['apps', 'beta'])
    async def applications(self, ctx, *, user: discord.Member = None):
        """Link to Shadow Applications download."""
        text = """You can find the Shadow Applications, both stable and beta versions in your account page: https://account.shadow.tech/apps"""
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = """From {ctx.author.name}\n{user.mention} """ + text
            await ctx.send(text.format(ctx=ctx, user=user))
            await ctx.message.delete()
        elif await self.bot.admin.can_run_command(ctx.author.roles):
            text = """From {ctx.author.name}\n""" +text
            await ctx.send(text.format(ctx=ctx, user=user))
            await ctx.message.delete()
        else:
            text = """{ctx.author.mention} """ + text
            await ctx.author.send(text.format(ctx=ctx))
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(General(bot))
