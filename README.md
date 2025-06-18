# 🪨📄✂️ RSP Telegram Bot

A Telegram bot for playing **Rock-Paper-Scissors**. Built with Python and `aiogram`. Easy to run with Docker.

## 🚀 Quick Start

### 🔧 Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 🛠 Installation & Run

1. Clone the repository:

```bash
git clone https://github.com/empty-complete/rsp_tg_bot.git
cd rsp_tg_bot
```

2. Create `.env` file from the example:

```bash
cp .env.example .env
```

3. Add your **Telegram Bot Token** in `.env` by using [BotFather](https://t.me/BotFather)

```.env
BOT_TOKEN=<your_token>
```

4. Build and run the bot:

```bash
docker compose up --build
```

_or detach mode_

```bash
docker compose up -d --buld
```

> 📄 **Logs:**  
> You can view real-time logs with:
>
> ```bash
> docker logs -f rsp_tg_bot
> ```

## 💡 Features

- `/start` — launches the bot
- `/help` — shows help and usage info

> 🎮 **Interactive Gameplay:**  
> The bot provides a keyboard with buttons to play the game and navigate other options.

## 📁 Project Structure

```bash
rsp_tg_bot/
├── config/             # Configuration (e.g., bot token)
├── handlers/           # Bot command handlers
├── keyboards/          # Reply keyboards
├── lexicon/            # Bot messages and responses
├── logs/               # Logs (if implemented)
├── services/           # Business logic
│   └── games/          # Game implementation
├── main.py             # Bot entry point
├── Dockerfile          # Docker build instructions
├── .dockerignore       # Docker ignore file
├── compose.yaml        # Docker Compose config
├── pyproject.toml      # Python dependencies
├── .env.example        # Example environment config
└── README.md
```

## 🧰 Tech Stack

- Python 3.13

- aiogram

- Docker + Docker Compose

- uv by Astral
