from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU

# Create the keyboard's buttons
start_button = KeyboardButton(text=LEXICON_RU["start_button"])
help_button = KeyboardButton(text=LEXICON_RU["help_button"])
quit_button = KeyboardButton(text=LEXICON_RU["quit_button"])
scissors_button = KeyboardButton(text=LEXICON_RU["scissors"])
paper_button = KeyboardButton(text=LEXICON_RU["paper"])
rock_button = KeyboardButton(text=LEXICON_RU["rock"])

# Initial greeter keyboard
greeter_keyboard = ReplyKeyboardBuilder()

# Initial game keyboard
game_keyboard = ReplyKeyboardBuilder()

# Add buttons to greeter keyboard
greeter_keyboard.row(start_button, help_button, width=2)

# Add buttons to game keyboard
game_keyboard.row(
    rock_button, scissors_button, paper_button, quit_button, help_button, width=3
)


# Inital dictionary with created keyboards
KEYBOARDS: dict[str, ReplyKeyboardMarkup] = {
    "/start": greeter_keyboard.as_markup(resize_keyboard=True),
    "/game": game_keyboard.as_markup(resize_keyboard=True),
}
