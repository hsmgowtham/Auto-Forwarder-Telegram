from os import environ
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv(".env")
from telethon.sync import TelegramClient


# Get Config from Env File
API_ID = environ.get("API_ID")
API_HASH = environ.get("API_HASH")
PHONE_NUMBER = environ.get("PHONE_NUMBER")
MESSAGE_SINCE_HR = int(environ.get("MESSAGE_SINCE_HR"))

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

async def forward_messages():
    now = datetime.now(timezone.utc)
    last_hour = now - timedelta(hours=MESSAGE_SINCE_HR)
    
    messages = await client.get_messages(CHANNEL_ID, limit=100)
    if messages:
        for message in messages:
            print(f"{message.date} - {message}")
            if message.date > last_hour:
                for contact_chat_id in CONTACT_CHAT_IDS:
                    await client.forward_messages(contact_chat_id, message, from_peer=CHANNEL_ID)
    else:
        print("No messages found in the last hour.")

# Forward messages shared in the last hour to all contacts
with client:
    client.loop.run_until_complete(forward_messages())
