from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON_RU

# Initalize router with module level
router = Router()


# This handler is proceed any messages
# without "/start" and "/help"
@router.message()
async def send_echo(message: Message):
    await message.reply(text=LEXICON_RU["trash"])
