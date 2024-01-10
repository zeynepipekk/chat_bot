# Chat Bot

## Credits

This project was inspired by the tutorial available on YouTube: (https://www.youtube.com/watch?v=CkkjXTER2KE).

## Description

This chat bot is designed to provide responses to user-input questions based on a predefined knowledge base. If the bot doesn't have an answer, it prompts the user to teach it and adds the new question-answer pair to the knowledge base.

## Features

- Load and save knowledge base from/to a JSON file.
- Find the best match for user questions using difflib.
- Interact with users in a basic chat format.

## How to Use

1. Install Python (if not already installed).
   
3. Clone the repository:
    ```bash
   git clone https://github.com/zeynepipekk/chat_bot.git
   ```
4. Navigate to the project directory:
   ```bash
   cd chat-bot
   ```
6. Run the chat bot:
    ```bash
    python main.py
    ```
7. Interact with the bot by entering questions or type "quit" to exit.

## Knowledge Base
The knowledge base is stored in a JSON file named knowledge_base.json. You can manually edit this file to add or modify question-answer pairs.
