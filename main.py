import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

random_user_agent = ua.random

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
        'TOKEN': 'WLsPUPPtcRBecW21QwPM',
        'SEC': 'jikkmpcxill00000:offxohtbgv000000',
        'SERVER': 'oajGrITI32TEZnJk'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Referer': 'https://aternos.org/server/',
        'Cookie': 'ATERNOS_SEC_r4sqh5kefaj00000=n7lzzaahppg00000; ATERNOS_SEC_6qh1ad308ob00000=ox8qkl6oeib00000; ATERNOS_SEC_s4qtnho5r1000000=xtq57uoz8r000000; ATERNOS_SEC_27n5e3m1y0u00000=vcnu2kt3yph00000; ATERNOS_SEC_cvaubuahorn00000=7pqmbipslio00000; ATERNOS_SEC_vtqp0pxtinb00000=vd9wl3eocrf00000; ATERNOS_SEC_tkmozjg8l5000000=0hfzpjw4s1nq0000; ATERNOS_SEC_sqfbnqu4g6o00000=uf0e4ta2fsr00000; ATERNOS_SEC_e7ubsxn6v1900000=w9vmzo2vwrd00000; ATERNOS_SEC_qg7ciecqolr00000=mrwjvd92xr000000; ATERNOS_SEC_yhc20g9sj6900000=8gzkpvt9yef00000; ATERNOS_SEC_euz65wem8b600000=027huame3z1b0000; ATERNOS_SEC_rr9ifw4ti6000000=x92lvcrar8r00000; ATERNOS_SEC_0elmtkoexhq00000=r095uqpqjp000000; ATERNOS_SEC_nepuukqc40000000=v080ng3w1j000000; ATERNOS_SEC_lfvn3eisn6h00000=di4amh2ydnb00000; ATERNOS_SEC_2xfwcef17dl00000=fljstw9ep6p00000; ATERNOS_SEC_jikkmpcxill00000=offxohtbgv000000; ATERNOS_SEC_o6tzzuseh3m00000=jfwr0n018rh00000; ATERNOS_LANGUAGE=en; ATERNOS_SESSION=2UNfovJ2584S0psXH6SM8QiHXudbANrE9F048yZAYIvXeaTC7oNMLpK5baoNG18c1c7r0BxZHwCxOdn8MGseHb7jmtfHTYFw2bDI; ATERNOS_SERVER=oajGrITI32TEZnJk; cf_clearance=.HS6rJsMMb1vRX2blZpkFYjN_Njtcq5ZTUSAVRh6TZA-1709220755-1.0-AVt4Dm9A6xUrEFepv1v+wdrPHhKZcO+W9PhCmefsJow/jl5VtxUAdd1SIxB2URGDStBjdmcUP2yUhmucXDhB3Mk='
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
