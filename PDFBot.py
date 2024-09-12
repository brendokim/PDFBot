import discord
from discord.ext import commands
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from dotenv import load_dotenv
from typing import Final
import io
import os

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.command(name='convert')
async def convert(ctx):
    if not ctx.message.attachments:
        print('No file attached')
        await ctx.send("Please attach an image.")
        return

    images = []
    for attachment in ctx.message.attachments:
        img_data = await attachment.read()
        try:
            img = Image.open(io.BytesIO(img_data))
        except Exception:
            await ctx.send(f"Failed to process {attachment.filename}. Make sure it's a valid image file.")
            return
        images.append(img)

    pdf_buffer = io.BytesIO()
    c = canvas.Canvas(pdf_buffer)

    for img in images:
        img_buffer = io.BytesIO()
        img.save(img_buffer, format="PNG")
        img_buffer.seek(0)
        c.setPageSize(img.size)
        image_reader = ImageReader(img_buffer)
        c.drawImage(image_reader, 0, 0, width=img.width, height=img.height)
        c.showPage()

    c.save()
    pdf_buffer.seek(0)

    await ctx.send(file=discord.File(fp=pdf_buffer, filename="output.pdf"))

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')

def runDiscordBot():
    bot.run(TOKEN)