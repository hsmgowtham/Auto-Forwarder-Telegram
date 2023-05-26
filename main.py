from os import environ
from dotenv import load_dotenv

load_dotenv(".env")
from telethon.sync import TelegramClient, events


# Get Config from Env File
API_ID = environ.get("API_ID")
API_HASH = environ.get("API_HASH")
PHONE_NUMBER = environ.get("PHONE_NUMBER")

CHANNEL_ID = None
CONTACT_CHAT_IDS = []
for key, val in environ.items():
    if key.startswith("CONTACT_ID"):
        CONTACT_CHAT_IDS.append(int(val))
    elif key.startswith("CHANNEL_ID"):
        CHANNEL_ID = int(val)

# Create a Telegram client
client = TelegramClient("session", API_ID, API_HASH)

# Start the client and authenticate with the phone number
client.start(phone=PHONE_NUMBER)

if CHANNEL_ID:
    @client.on(events.NewMessage(chats=CHANNEL_ID))
    async def forward_message(event):
        message = event.message
        for contact_chat_id in CONTACT_CHAT_IDS:
            await client.forward_messages(
                contact_chat_id, message, from_peer=CHANNEL_ID
            )


# Run the client to start listening for new messages
client.run_until_disconnected()
