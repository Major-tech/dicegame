# Dice Game CLI 🎲

A simple command-line dice game with multiple modes: **roll**, **play**, and **guess the number**.  
Designed for fun, quick gameplay, and testing your luck and prediction skills.

---

## Interactive Mode

DiceGame supports an **interactive mode**, letting you run commands step by step without typing full CLI commands every time.

```bash
python -m dicegame


## Version and Features

## [0.4.0] – 2026-01-21

**Key updates in this release:**

### Added
- Introduced a new `play` command for the Win/Lose dice game mode.

### Changed
- Renamed the `display` command to `roll` to improve clarity and consistency across the CLI.

### Fixed
- Prevented deletion of the currently active account.
- Added password confirmation for account deletion in both CLI and interactive modes to enhance security.


## [0.3.0] – 2026-01-20

**Key updates in this release:**

### Added
- Formatted leaderboard table for clear and structured score display
- Formatted players table for improved readability of the player list

### Changed
- Renamed CLI commands for better semantics and consistency:
  - `view users` → `player list`
  - `view scores` → `leaderboard`
  - `delete user` → `player delete`
- Improved overall CLI user experience and command clarity

### Fixed
- Resolved issue where delete success/error message was displayed after three failed delete attempts


## [0.2.0] – 2026-01-20

**Key updates in this release:**

- Introduced colorful console messages using [Rich](https://rich.readthedocs.io/en/stable/) for better UI/UX.
- Added an interactive session panel to make gameplay more engaging.
- Added a progress bar animation for the dice roll to enhance visual feedback.


## [0.1.0] 2026-01-17
- User registration/login
- Secure password hashing (Argon2)
- SQLite persistence
- CLI interface using argparse


## Tech stack
- python 3.13
- argon2
- sqlite3
- argparse


## Usage

| Command | Description |
|---------|-------------|
| login   | user login |
| signup   | user signup |
| roll    | Simple dice roll |
| play    | Win/Lose dice game |
| guess <number> | Guess the dice number |
| player list | List all players |
| leaderboard | Show leaderboard |
| player delete | Delete an account (requires password) |


## Installation
```bash
pip install -e .

