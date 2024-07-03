# Telegram Message Forwarder

A simple Python script that forwards messages from a Telegram channel to specified contacts within a given time range. 

**Fun Fact**: I made This quick project when I couldn't add a friend to a telegram channel.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Telegram Message Forwarder is a personal project developed in Python that automates the forwarding of messages from a Telegram channel to designated contacts. It allows you to specify a time range within which messages should be forwarded and provides an efficient way to keep your contacts updated with the latest information shared in the channel.

## Prerequisites

Before using the Telegram Message Forwarder, ensure you have the following prerequisites:

- Python 3.7 or above
- `telethon` library (install via `pip install telethon`)
- Telegram API credentials (API ID and API Hash)

## Setup

1. Clone the repository:

```
git clone https://github.com/your-username/telegram-message-forwarder.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Set up your environment variables:

Create a `.env` file and provide the following information:
```
API_ID=your_api_id
API_HASH=your_api_hash
PHONE_NUMBER=your_phone_number
MESSAGE_SINCE_HR=1
CONTACT_ID_1=contact_chat_id_1
CONTACT_ID_2=contact_chat_id_2
CHANNEL_ID=channel_id
```
Replace the placeholders with your actual API credentials, phone number, message duration (in hours), contact chat IDs, and channel ID.

4. Run the script:
```
python forward_messages.py
```

## Usage

To use the Telegram Message Forwarder, follow these steps:

1. Make sure you have completed the setup steps mentioned above.
2. Run the script using the command `python forward_messages.py`.
3. The script will connect to the Telegram API, retrieve messages from the specified channel, and forward them to the designated contacts within the defined time range.
4. The forwarded messages will appear in the chats of the specified contacts.
5. The script will print a log of the forwarded messages and any errors encountered.

## Configuration

The Telegram Message Forwarder can be configured using the environment variables defined in the `.env` file. Here's a description of the available variables:

- `API_ID`: Your Telegram API ID. Obtain this value by creating an application at the Telegram API website.
- `API_HASH`: Your Telegram API hash. Obtain this value along with the API ID.
- `PHONE_NUMBER`: Your phone number associated with the Telegram account.
- `MESSAGE_SINCE_HR`: The duration (in hours) within which messages should be forwarded.
- `CONTACT_ID_1`, `CONTACT_ID_2`, ...: The chat IDs of the contacts to which messages should be forwarded.
- `CHANNEL_ID`: The chat ID of the channel from which messages should be retrieved.

Make sure to set these variables correctly before running the script.

## Contributing

Contributions to the Telegram Message Forwarder project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the GitHub repository.

## License

The Telegram Message Forwarder is open-source and distributed under the [MIT License](LICENSE).
Feel free to modify and customize the README file as per your project requirements.
