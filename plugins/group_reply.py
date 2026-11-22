from telethon import events
from utils.utils import CipherElite
from utils.decorators import authorized_users_only
from plugins.bot import add_handler

VERSION = "1.0.0"
CATEGORY = "admin"

def init(client_instance):
    commands = [
        ".replyall <text> - Reply to all members in the group",
    ]
    description = "🎭 Group Reply - Reply to all members in the group"
    add_handler("group_reply", commands, description)

async def register_commands():
    @CipherElite.on(events.NewMessage(pattern=r"\.replyall\s+(.*)"))
    @authorized_users_only()
    async def reply_all(event):
        try:
            text = event.pattern_match.group(1).strip()
            chat = await event.get_chat()
            for user in chat.participants:
                if user.id != event.client.uid:
                    await event.client.send_message(user, text)
            await event.reply("🎭 **Replied to all members**")
        except Exception as e:
            await event.reply(f"❌ **Error:** {str(e)}")

# ============ METADATA ============
# PLUGIN_NAME: group_reply
# COMMANDS:
# .replyall <text> - Reply to all members in the group
# REQUIREMENTS:
# none
# ===================================