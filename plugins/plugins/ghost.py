from telethon import events
from utils.utils import CipherElite
from utils.decorators import rishabh
from plugins.bot import add_handler

VERSION = "1.0.0"
CATEGORY = "utilities"

ghost_enabled = False


def init(client_instance):
    commands = [
        ".g - Enable Ghost Mode",
        ".gg - Disable Ghost Mode"
    ]

    add_handler(
        "ghost",
        commands,
        "👻 Ghost Mode - Automatically delete your outgoing commands"
    )


async def register_commands():

    @CipherElite.on(events.NewMessage(
        outgoing=True,
        pattern=r"^\.g\s*$"
    ))
    @rishabh()
    async def ghost_on(event):
        global ghost_enabled

        ghost_enabled = True
        await event.delete()

    @CipherElite.on(events.NewMessage(
        outgoing=True,
        pattern=r"^\.gg\s*$"
    ))
    @rishabh()
    async def ghost_off(event):
        global ghost_enabled

        ghost_enabled = False
        await event.delete()

    @CipherElite.on(events.NewMessage(
        outgoing=True,
        pattern=r"^\.(?!g{1,2}\s*$)\S+"
    ))
    @rishabh()
    async def ghost_delete(event):
        if not ghost_enabled:
            return

        try:
            await event.delete()
        except Exception as e:
            print(f"Ghost Delete Error: {e}")
