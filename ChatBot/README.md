# Chatbot "Pal" using Regular Expressions

## Overview
This project is a Python-based chatbot named "Pal" that responds to user input based on predefined patterns. The bot uses regular expressions (`re`) to match user input and provide appropriate responses. It’s a basic rule-based chatbot designed to engage users in casual conversation.

## Features
- Responds to user greetings, common questions, and conversational queries.
- Provides facts, trivia, and jokes based on user input.
- Exits the conversation when the user types "exit".
- Can be easily extended by adding more patterns and responses.

## How to Use
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/chatbot-pal.git
   cd chatbot-pal
   ```
   
2. **Run the script**:
   ```bash
   python chatbot.py
   ```

3. **Start the conversation**:
   - The chatbot will greet you and await your input.
   - Type something like "hello", "what's your name?", or "tell me a joke".
   - To exit the conversation, simply type "exit".

## Example
```
Welcome to the Chatbot named Pal. Say 'Exit' to end the conversation.
You: Hello
Pal: Hello! How can I help you today?

You: Tell me a joke
Pal: Why don't scientists trust atoms? Because they make up everything!

You: Exit
Pal: -----Chat Ended-----
```

## How it Works
- **Pattern Matching**: The bot uses regular expressions to match the user's input against a set of predefined patterns.
- **Custom Responses**: Based on the matched pattern, the bot provides a response.
- **Extendable**: You can easily add more patterns and responses by modifying the `PatternsResponses` dictionary.

## Requirements
- **Python 3.x**

## Customization
You can add your own responses by editing the `PatternsResponses` dictionary in the code. For example:
```python
PatternsResponses = {
    r"hello|hi|hey": "Hello! How can I help you today?",
    r"who are you": "I'm a chatbot named Pal, here to assist you!",
    # Add more patterns and responses here
}
```

## License
This project is open-source and free to use. Feel free to modify it to suit your needs.

Enjoy chatting with Pal!
