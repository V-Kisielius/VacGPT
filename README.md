# Telegram Chatbot using OpenAI GPT-3.5-Turbo API

This is a Telegram chatbot that uses the OpenAI GPT-3.5-Turbo API to chat with users. It's a fun project that demonstrates the capabilities of GPT-3.5-Turbo. 

## Getting Started

To use this chatbot, you'll need to do the following:

1. Create a Telegram bot and get its API key.
2. Create an OpenAI account and get your API key.
3. Install the necessary packages: `pip install -r requirements.txt`
4. Set the following environment variables:
   - `TELEGRAM_TOKEN`: The API key for your Telegram bot.
   - `OPENAI_TOKEN`: The API key for your OpenAI account.
   - `SECRET_WORD`: Password required for start chatting.
   - `ADMINS`: A comma-separated list of Telegram user IDs who have admin access to your bot.
5. Run `python3 bot.py`

## Bot Commands

This chatbot supports the following commands:

- `/login password`: Allows user to login with password (`SECRET_WORD`).
- `/restart`: Clear message history.
- `/password pass`: Change `SECRET_WORD` to `pass`.
- `/password`: Show current password.
- `/users`: Get a list of all users.
- `/history id`: Get chat history with a specific user ID.

## Issues and Contributions

If you encounter any issues or bugs while using this chatbot, please open an issue here on Github.

If you'd like to contribute to this project, feel free to fork this repository and submit a pull request. We welcome any and all contributions!

## Fun fact: *this readme file was created by a bot!*

If you're interested in trying out the bot yourself, you can find it here: [@supervac_bot](https://t.me/supervac_bot).
