from flask import Flask
import asyncio
from aiohttp import web

app = Flask(name)

@app.route('/')
def thecrazybossisback():
    return 'Crazybossss'

async def run_app():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 5000)
    await site.start()

if name == "main":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_app())
    loop.run_forever()
