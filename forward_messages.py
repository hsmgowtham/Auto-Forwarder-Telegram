from os import environ
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from telethon.tl.types import PeerChannel
from telethon.sync import TelegramClient

load_dotenv(".env")

# Get Config from Env File
API_ID = environ.get("API_ID")
API_HASH = environ.get("API_HASH")
PHONE_NUMBER = environ.get("PHONE_NUMBER")
MESSAGE_SINCE_HR = int(environ.get("MESSAGE_SINCE_HR"))


# Create a Telegram client
client = TelegramClient("session", API_ID, API_HASH)

# Start the client and authenticate with the phone number
client.start(phone=PHONE_NUMBER)

async def forward_messages():
    async with TelegramClient("session_name", API_ID, API_HASH) as client:
        CONTACT_CHAT_IDS = []
        CHANNEL_ID = None

        for key, val in environ.items():
            if key.startswith("CONTACT_ID"):
                CONTACT_CHAT_IDS.append(int(val))
            elif key.startswith("CHANNEL_ID"):
                CHANNEL_ID = await client.get_entity(PeerChannel(int(val)))
                print(CHANNEL_ID)

        now = datetime.now(timezone.utc)
        specified_hours = now - timedelta(hours=MESSAGE_SINCE_HR)

        message_forwarded_count = 0
        messages = await client.get_messages(CHANNEL_ID, limit=100)
        print("-" * 50)
        if messages:
            for message in messages:
                if message.date > specified_hours:
                    message_forwarded_count += 1
                    for contact_chat_id in CONTACT_CHAT_IDS:
                        await client.forward_messages(
                            contact_chat_id, message, from_peer=CHANNEL_ID
                        )
            with open("./logs.txt", "a") as file:
                file.write(f"\n{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Total Messages Forwarded in the last {MESSAGE_SINCE_HR} hr's = {message_forwarded_count}")
        else:
            print("No messages found in the last hour.")


# Forward messages shared in the last hour to all contacts
with client:
    client.loop.run_until_complete(forward_messages())
