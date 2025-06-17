from random import choice

from lexicon.lexicon import LEXICON_RU
from services.games.rsp import rsp_proceed

# Options for rsp game
OPTIONS_RSP: dict[str, int] = {
    LEXICON_RU["paper"]: 0,
    LEXICON_RU["rock"]: 1,
    LEXICON_RU["scissors"]: 2,
}

# Winner table for rsp game
WINNER_TABLE_RSP: dict[int, str] = {
    0: LEXICON_RU["draw"],
    1: LEXICON_RU["bot_won"],
    2: LEXICON_RU["user_won"],
}


def rsp_get_winner(user_text: str) -> dict[str, str]:
    """This function determine the winner in game rock-scissors-paper
    Args:
        user_text: User text, message.text
    Returns:
        int: see rsp.py
    """

    bot_text: str = choice(tuple(OPTIONS_RSP.keys()))
    bot_choice: int = OPTIONS_RSP[bot_text]

    user_choice: int = OPTIONS_RSP[user_text]

    winner = WINNER_TABLE_RSP[
        rsp_proceed(player1_choice=bot_choice, player2_choice=user_choice)
    ]

    return {"bot_text": bot_text, "winner": winner}
