import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

ATERNOS_TOKEN = os.getenv("ATERNOS_TOKEN")
SEC = os.getenv("SEC")
SERVER = os.getenv("SERVER")
BOT_DISCORD_TOKEN = os.getenv("BOT_DISCORD_TOKEN")
USER_AGENT = os.getenv("USER_AGENT")
COOKIE = os.getenv("COOKIE")

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='gas')
async def start_server(ctx):
    url = "https://aternos.org/ajax/server/start"
    params = {
        'access-credits': 'false',
        'TOKEN': ATERNOS_TOKEN,
        'SEC': SEC,
        'SERVER': SERVER
    }

    headers = {
        'User-Agent': USER_AGENT,
        'Referer': 'https://aternos.org/server/',
        'Cookie': COOKIE
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        if response.status_code == 200:
            message = "Sabar... server otewe di nyalain!\nTunggu sampe ada notif server nyala (3 - 5 menit), kalau kelamaan coba nyalain lagi."
            print(f"Length of message: {len(message)}")
            await ctx.send(message)
        else:
            await ctx.send(f"Ups, ada masalah. Status Code: {response.status_code}: {response.text}")
    except requests.exceptions.HTTPError as e:
        await ctx.send(f"Terjadi kesalahan HTTP: {e.response.status_code}: {e.response.text}")
    except Exception as e:
        await ctx.send(f"Terjadi kesalahan: {str(e)}")

@bot.command(name='tolong')
async def help_server(ctx):
    embed = discord.Embed(
        title="List Perintah",
        description="Berikut adalah beberapa perintah yang tersedia:",
        color=0x3498db
    )
    embed.add_field(name="/gas", value="Memulai server", inline=False)
    embed.add_field(name="/tolong", value="Menampilkan bantuan", inline=False)
    await ctx.send(embed=embed)

# Jalankan bot dan Flask (harus dijalankan secara bersamaan)
if __name__ == '__main__':
    import os
    from threading import Thread

    def run():
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

    Thread(target=run).start()
    bot.run(BOT_DISCORD_TOKEN)
