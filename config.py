config.py# Configuration file for Discord bot
# Contains all bot configuration settings

import os

# Bot configuration
BOT_PREFIX = "$"
BOT_DESCRIPTION = "A simple Discord bot for server management"

# Feature flags
ENABLE_LOGGING = True
ENABLE_AUTO_RESPONSES = True
ENABLE_MODERATION = False

# Channel IDs (replace with your channel IDs)
WELCOME_CHANNEL_ID = None
LOG_CHANNEL_ID = None
MOD_CHANNEL_ID = None

# Role IDs (replace with your role IDs)
ADMIN_ROLE_ID = None
MOD_ROLE_ID = None
MEMBER_ROLE_ID = None

# Command cooldowns (in seconds)
COMMAND_COOLDOWN = 3
SPAM_THRESHOLD = 5

# Bot status messages
STATUS_MESSAGES = [
    "Watching the server",
    "Ready to help!",
    "Type $help for commands"
]

# Database configuration
DB_ENABLED = False
DB_PATH = "bot_data.db"
