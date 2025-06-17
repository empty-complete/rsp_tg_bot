import logging

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from keyboards.keyboard import KEYBOARDS
from lexicon.lexicon import LEXICON_RU
from services.services import rsp_get_winner

# Start module's logger
logger = logging.getLogger(__name__)

# Initalize router with module level
router = Router()


# This handler is proceed /start Command
@router.message(CommandStart())
async def process_start_command(message: Message):
    logger.info(
        f"Greeting new user {message.from_user.username}({message.from_user.id})"  # type: ignore
    )
    await message.answer(
        text=LEXICON_RU["/start"],
        reply_markup=KEYBOARDS["/start"],
    )


# This handler is proceed /help Command
@router.message(Command(commands="help"))
@router.message(F.text == "Правила игры 🐣")
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU["/help"])


@router.message(F.text == "Начать игру 🔥")
@router.message(Command(commands="game"))
async def process_game_start(message: Message):
    await message.answer(text=LEXICON_RU["/game"], reply_markup=KEYBOARDS["/game"])


@router.message(F.text == "Прервать игру ❌")
@router.message(Command(commands="exit"))
async def process_quit_game(message: Message):
    await message.answer(text=LEXICON_RU["quit_text"], reply_markup=KEYBOARDS["/start"])


@router.message(
    F.text.in_(
        [
            LEXICON_RU["rock"],
            LEXICON_RU["scissors"],
            LEXICON_RU["paper"],
        ]
    )
)
async def procces_game(message: Message):
    bot_text, winner = rsp_get_winner(message.text).values()  # type: ignore
    await message.answer(text=LEXICON_RU["bot_choice"])
    await message.answer(text=bot_text)
    await message.answer(text=winner)
