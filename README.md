# Aternos Discord Bot

A simple Discord bot to control your Aternos server.

## Features

- Start your Aternos server with a Discord command
- Display a list of available commands

## Getting Started

### Prerequisites

- Python 3.x
- Discord.py library
- Requests library

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Aternos-Discord-Bot.git
    cd Aternos-Discord-Bot
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the bot:

    ```bash
    python main.py
    ```

### Usage

- Invite the bot to your Discord server.
- Use the following commands in your Discord channel:

    - `/gas`: Start your Aternos server
    - `/tolong`: Display a list of available commands

## Configuration

1. Open `main.py` and update the following variables:

    - `TOKEN`: Your Discord bot token
    - `url`, `params`, `headers`: Aternos API details

## Acknowledgments

- Inspired by [Aternos API](https://aternos.org/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
