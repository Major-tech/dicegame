# Dice Game CLI 🎲

- A simple cli dicegame where a player rolls the dice while participating in different game modes and it can be played by anyone



## TABLE OF CONTENTS
- Overview
- Installation
- Usage
- Motivation
- Version and Features 
- Versioning
- Configuration
- Project structure
- Roadmap
- License


## Overview
- A simple command-line dice game with multiple modes: **roll**, **play**, and **guess the number**.
- Designed for fun, quick gameplay, and testing your luck and prediction skills.
- Players create accounts, roll dice,
track scores, and compete on a leaderboard.


## Installation
```bash

### clone repository
git clone https://github.com/Major-tech/dicegame-cli.git

### Install in editable mode
pip install -e . 

### Run the project
python -m dicegame

## Development Setup (Recommended)

This project requires **Python 3.10+**

## Optional dependencies

1. Create a virtual environment
2. Run `pip install .[dev]`
3. Run tests with `pytest`

If you use `pyenv`, you can install and activate the correct version:

```bash
pyenv install 3.11.7
pyenv local 3.11.7


## Running Tests

This project includes minimal tests using pytest:

```bash
pip install pytest
pytest -v


## Usage
- prefix 'dicegame' before each command in non-interactive/cli mode
- In interactive mode,simply type the commamd name and run it


| Command | Description |
|---------|-------------|
| log list | Shows all available log files |
| log clear | Clears all application logs |
| whoami | Displays the currently logged in user |
| report-bug | Packages application logs into a ZIP file|
| reset password  | reset player password
| login   | user login |
| signup   | user signup | 
| roll    | Simple dice roll |
| play    | Win/Lose dice game |
| guess <number> | Guess the dice number |
| player list | List all players |
| leaderboard | Show leaderboard |
| reset score  | reset player score |
| player delete | Delete an account (requires password) |


| Flag   | Description |
|------------------------
| -i | --interactive | Enter interactive mode |
| -V | --version | View dicegame-cli version |
| --debug | Enable debug mode |


### Practical Examples
## Usage

Below are example commands demonstrating how to use each feature of the application.

```bash
## FLAGS

# Enter interactive mode
dicegame -i | dicegame --interactive 

# View current dicegame version
dicegame -V | dicegame --version

## In interactive mode:
- Type the command 'version'

# Enable debug mode
dicegame --debug


## COMMANDS
# See a list of all log files
dicegame log list

# Clear all the application's log files
dicegame log clear

# Display the currently ligged in user
dicegame whoami

# Create a bug report and email it to the developer in case an issue arises
dicegame report-bug

# Create a new user account
dicegame signup
- You'll be prompted for a usernmae and password

dicegame signup --username new_user
- You'll be prompted for a password

# Log in to an existing account
dicegame login
- You'll be prompted for a usernmae and password

dicegame login --username testuser
- You'll be prompted for a password

# Roll a dice once and display the result
dicegame roll

# Play the win/lose dice game
dicegame play

# Guess the dice number (replace <number> with your guess, e.g. 4)
dicegame guess 4

## In interactive mode:
- Type the command 'guess'
- You'll be prompted for your guess

# Display a list of all registered players
dicegame player list

# Display the leaderboard sorted by score
dicegame leaderboard

# Reset the currently logged-in player's score to zero
dicegame reset score

- You'll gwt a password prompt for verification

# Reset a player's password
dicegame reset password

- You'll get a password prompt for verification

# Delete the currently logged-in player's account (password required)
dicegame player delete

- You'll get a password prompt for verification


### **Note**
- If you did not install the app system-wide, replace `dicegame` with:
- `python -m dicegame`
- or `python main.py`

- In interactive mode you only type the command without the APP_NAME('dicegame')


## 📦 DiceGame is now on PyPI!

I’m excited to announce that **DiceGame** is officially published on PyPI.  
You can install it using:

```bash
pip install dicegame

Check out the PyPI page here: https://pypi.org/project/dicegame/
 
 
## Motivation

This project was born from the desire to **explore Python, CLI design, and application state management** in a hands-on way.  

While small in scope, it serves multiple purposes:  
- **Experimentation and learning**: Testing out interactive and non-interactive workflows, persistent sessions, and secure user handling.  
- **Practical tool-building**: Creating a usable CLI for games with score tracking, authentication, and logging.  
- **Structured development practice**: Applying versioning, releases, and incremental improvements to learn disciplined software evolution.  
- **Emphasis on reliability and privacy**: Implementing logging, debug flags, and per-user actions with attention to security and user experience.  

In short, this project is as much about **growing as a developer** as it is about providing a functional command-line application.


## VERSION AND FEATURES

## [0.7.0] - 2026-02-17

**Key updates in this release:**

## Added Features
- Informative command help.
- Automatic help if no arguments are provided.
- Redaction of sensitive information in logs for privacy


---------------------------------------------

## [0.6.0] - 2026-01-30

**Key updates in this release:**

## Added Features

### Authentication & Accounts
- User **signup** with automatic login after successful registration
- **Login / Logout** with session persistence on local disk for cli and interactive modes
- **Guest mode** included (Now supported also in interactive mode)
- **whoami** command
  - Displays `Not logged in` if no user is authenticated
  - Displays the current username if logged in
- **player delete**
  - Only the account currently logged in can be deleted
- **reset password**
  - Only allowed for the currently logged-in account

---

### Gameplay
- **reset score** command
  - Only allowed for the logged-in user
  - Aborts if the score is already `0`

---

### Interactive Mode
- Full feature parity with non-interactive mode
- Uses **local disk persistence** (not in-memory state)
- Guest users can interact without logging in

---

### Logging & Debugging
- Structured application logging
- `--debug` flag enables verbose/debug output
- **log list**
  - Shows all available log files
- **log clear**
  - Clears all application logs

---

### Privacy-Respecting Bug Reporting
- **report-bug** command
  - Requests explicit user consent
  - Packages all application logs into a ZIP file
  - User manually sends the ZIP to the developer via email
  - No automatic data transmission

---

## Commands Overview

### Authentication
- `whoami`
- `reset password`
- `player delete`

### Game
- `reset score`

### Logs & Diagnostics
- `log list`
- `log clear`
- `report-bug`

### Global Flags
- `--debug` — Enable debug mode

---

## Design Principles

- Clear **command / service separation**
- Explicit session management via a `Session` domain object
- Fail-fast validation (authentication, state checks)
- Privacy-first logging and diagnostics
- CLI-friendly error handling (no silent failures)


---------------------------------------

## [0.5.0] - 2026-01-22

**Key updates in this release:**

This release introduces **session persistence**, **improved score management**, and a **clean separation between interactive and non-interactive gameplay**.

Version **0.5.0** focuses on making the CLI more realistic, user-friendly, and aligned with production-grade CLI design.

### Added

### 🔐 Session Persistence for CLI
- Added **database-backed session handling**
- Session token is **saved locally** to persist login across runs
- Only **one active user session** is stored at a time
- Logout clears the local session

---

### 💾 Score Persistence in CLI/Non-interactive mode
- Scores are stored in the **database**
- Leaderboard updates automatically
- Score persistence now works in:
  - Interactive mode (since v0.1.0)
  - Non-interactive mode (Added in v0.5.0)
  - Both `play` and `guess` commands

---

### 👤 Guest vs Authenticated Play
- Users may **play without logging in** in CLI only not in interactive mode
- Guest gameplay:
  - Uses in-memory state only
  - Scores are **not saved**
- Authenticated users:
  - Have scores persisted
  - Appear on the leaderboard

---

### 🔄 Reset Score Capability
- Added **reset score to zero** option (reset)
- Includes **confirmation prompt** to prevent accidental resets
- Applies only to the currently logged-in user

---

## 🧩 Architectural Improvements

- Clear separation between:
  - **Interactive** (in-memory) flows
  - **Non-interactive** (persistent) flows
- Authentication-aware score handling
- Clean boundaries between gameplay, persistence, and session logic


---------------------------------------

## [0.4.0] – 2026-01-21

**Key updates in this release:**

### Added
- Introduced a new `play` command for the Win/Lose dice game mode.

### Changed
- Renamed the `display` command to `roll` to improve clarity and consistency across the CLI.

### Fixed
- Prevented deletion of the currently active account.
- Added password confirmation for account deletion in both CLI and interactive modes to enhance security.


-----------------------------------------

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


-------------------------------------------

## [0.2.0] – 2026-01-20

**Key updates in this release:**

- Introduced colorful console messages using [Rich](https://rich.readthedocs.io/en/stable/) for better UI/UX.
- Added an interactive session panel to make gameplay more engaging.
- Added a progress bar animation for the dice roll to enhance visual feedback.


---------------------------------------------

## [0.1.0] 2026-01-17
- User registration and login
- Secure password hashing (Argon2)
- SQLite score storage persistence
- CLI interface using argparse
- in-memory state for interactive mode


## Authentication & Sessions

- Users can **sign up, log in, and log out**
- A **session token is saved locally** to persist login across CLI runs
- Only **one active session** is stored at a time
- Logging out clears the local session

### Guest Mode
- Users may play without logging in
- Guest progress is **kept in memory only**
- Guest scores are **not saved to the database**
- Only authenticated users appear on the leaderboard



## Game Modes

### Interactive Mode
- Newer versions use **local session persistence** for active gameplay
- Dice rolls and guesses are ephemeral
- Scores are saved to the database at the end of a game (if logged in)

### Non-Interactive Mode
- Uses **local session persistence**
- Supports score saving for:
  - `play`
  - `guess`
- Designed for scripted or one-off CLI usage



## Versioning Policy

This project follows **Semantic Versioning (SemVer)** using the format `vMAJOR.MINOR.PATCH`.

Because this is a **command-line application**, versioning is defined in terms of **user-facing CLI behavior**, not internal implementation details.

### Pre-1.0 Releases (`0.y.z`)
- The project is under active development.
- CLI commands, flags, defaults, and behavior may change between releases.
- All `0.x.y` versions are considered **pre-release**, even without explicit `-alpha` or `-beta` labels.

### MAJOR Version (`1.0.0`, `2.0.0`, …)
A MAJOR version change indicates **breaking changes**, including:
- Removing or renaming commands or subcommands
- Removing or renaming flags or options
- Changing command semantics in a way that breaks existing workflows
- Incompatible changes to persisted data, config formats, or on-disk state

### MINOR Version (`0.6.0` → `0.7.0`)
A MINOR version introduces:
- New commands or subcommands
- New flags or options
- Backward-compatible behavior improvements
- New functionality that does not break existing usage

### PATCH Version (`0.6.1`)
A PATCH version includes:
- Bug fixes
- Performance improvements
- Internal refactoring
- Documentation updates
- Logging, diagnostics, or error-message improvements

PATCH releases do **not** introduce breaking changes to CLI syntax or behavior.

### Releases
- Every meaningful version is tagged (e.g. `v0.6.0`)
- GitHub Releases are published for tagged versions
- All `0.x.y` releases are marked as **Pre-release**
- Stability guarantees begin at `v1.0.0`



## Configuration
The app stores session data in:
~/.local/share/dice_game/sessions



## Project Structure
project-name/ │ ├─ cli/            # Command-line interface module │  └─ init.py │ ├─ commands/       # User-facing CLI commands (signup, login, roll, play, etc.) │ ├─ db/             # Database access and storage logic │ ├─ logging/        # Logging configuration and helpers │ ├─ services/       # Core business logic / game rules │ ├─ session/        # User session management │ ├─ utils/          # Utility functions used across modules │ ├─ tests/          # Unit and integration tests │ ├─ main.py     # Entry point for python -m project_name └─



## Roadmap
- Multiple player sessions



## License
- MIT License



## Author
Dennis Major
Email: dennismajor0@gmail.com
