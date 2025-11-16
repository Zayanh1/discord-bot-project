# Utility functions for Discord bot
# Various helper functions used throughout the bot

import re
import datetime
from typing import Optional, List


def format_timestamp(dt: datetime.datetime) -> str:
    """Format a datetime object into a readable string."""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def parse_mention(mention_str: str) -> Optional[int]:
    """Extract user ID from a mention string."""
    match = re.match(r'<@!?(\d+)>', mention_str)
    return int(match.group(1)) if match else None


def clean_content(content: str) -> str:
    """Remove mentions and clean message content."""
    # Remove user mentions
    content = re.sub(r'<@!?\d+>', '', content)
    # Remove channel mentions
    content = re.sub(r'<#\d+>', '', content)
    # Remove role mentions
    content = re.sub(r'<@&\d+>', '', content)
    return content.strip()


def split_message(message: str, max_length: int = 2000) -> List[str]:
    """Split a long message into chunks that fit Discord's limit."""
    if len(message) <= max_length:
        return [message]
    
    chunks = []
    while message:
        if len(message) <= max_length:
            chunks.append(message)
            break
        
        # Find the last space within limit
        split_pos = message.rfind(' ', 0, max_length)
        if split_pos == -1:
            split_pos = max_length
        
        chunks.append(message[:split_pos])
        message = message[split_pos:].lstrip()
    
    return chunks


def get_avatar_url(user_id: int, avatar_hash: str) -> str:
    """Generate avatar URL for a user."""
    return f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_hash}.png"
