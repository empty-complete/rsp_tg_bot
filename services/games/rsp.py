def rsp_proceed(player1_choice: int, player2_choice: int) -> int:
    """Simulate a rock-paper-scissors game and determine the winner.
    The function implements standatr rock-paper-scissors rules with the following mapping
        0: Paper
        1: Rock
        2: Scissors
    Args:
        player1_choice: Choice of player 1 (must be 0, 1, or 2)
        player2_choice: Choice of player 2 (must be 0, 1, or 2)
    Returns:
        int: 0 if draw, 1 if player 1 wins, 2 if player 2 wins
    Raises:
        ValueError: If any choice is not in [0, 1, 2]
    """
    if not all(c in {0, 1, 2} for c in (player1_choice, player2_choice)):
        raise ValueError("Choices must be 0 (Paper), 1 (Rock), or 2 (Scissors)")
    if player1_choice == player2_choice:
        return 0
    if (player1_choice - player2_choice) % 3 == 1:
        return 2
    return 1
