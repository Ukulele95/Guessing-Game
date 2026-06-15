# Guessing Game

This is a little number guessing game.
The game will run in the terminal.
It leads you through straight forward, you got 3 attempts.
If you guess wrong, it gives you a hint.

## Installation

### Requirements
- Python 3.7 or higher

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Ukulele95/Guessing-Game.git
   cd Guessing-Game
   ```

2. Run the game:
   ```bash
   python guessing_game.py
   ```

## How to Play

- The game will ask you to guess a number
- You have 3 attempts to guess correctly
- After each wrong guess, you'll receive a hint (higher or lower)
- Try to guess the secret number before running out of attempts!

## Changes

### Version 2.0 Updates

1. **Restructured code into functions** — Refactored the entire script from a single linear flow into four functions: `main()`, `guess()`, `evaluate()`, and `again()`.

2. **Added game loop functionality** — Implemented a play-again feature that lets users repeat the game multiple times instead of ending after one round.

3. **Added input range validation** — Added validation in `guess()` to check if the guess is between 1 and 10. The old version didn't validate the range.

4. **Separated game logic** — Split win/loss/continue logic into a dedicated `evaluate()` function instead of having it inline.

5. **Added pause after win/loss** — Added `input("Press any button to continue.")` after both win and lose messages.

6. **Improved user prompts** — Changed generic messages like "Try again!" to more specific feedback ("Your guess is too small" vs "Your guess is too large").

7. **Better attempt messaging** — Changed from "You are about to do attempt number" to "This is attempt number".

8. **Fixed return values** — Ensured all code paths in `evaluate()` return consistent values.

9. **Eliminated redundant logic** — The win and lose conditions now share common exit code instead of duplicating logic.

## Future ideas:
- Allow to adjust number of guesses
- Allow to change secret number range
- Implement multiplayer
