import os
import sys
from pyrogram import Client
def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "PyroUserBot"])
async def join(client):
    try:
        await client.join_chat("PyroUserBot")
    except BaseException:
        pass

