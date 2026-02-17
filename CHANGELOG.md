## [v0.7.0] - 2026-02-17
### Added
- Informative help messages for all commands, improving user guidance.
- Automatic help display when no arguments are provided.
- Redacting sensitive information in logs and outputs (e.g., usernames).

### Changed
- Refactored argument parsing to better support global flags and subcommands.

### Fixed
- Previously ignored global flags when no command was provided.
- Ensured safe logging practices for sensitive data.

---

## [0.6.0] 2026-01-30

### Added
- Reset password command  
  - Only resets the password of the currently logged-in account
- `whoami` command  
  - Shows authentication status and current user
- `report-bug` command  
  - Creates a ZIP archive of logs with explicit user consent
- `log list` command  
  - Displays all available log files
- `log clear` command  
  - Clears all application logs
- `--debug` flag  
  - Enables debug-level logging

---

### Changed
- Automatic login after successful signup
- Player delete behavior  
  - Users can only delete the account they are currently logged in to
- Reset command renamed and reworked  
  - `reset` → `reset score`
  - Only affects the logged-in user
  - Aborts if score is already `0`
- Interactive mode improvements  
  - Guest mode enabled
  - Uses local disk persistence instead of in-memory state

---

### Notes
- No breaking CLI syntax changes outside renamed reset command
- Focused on security, privacy, and state correctness



## [0.5.0] – 2026-01-22

### Added
- Reset score to zero option with confirmation prompt
- Database-backed session persistence for CLI usage
- Local session token storage (single active user at a time)
- Score persistence for non-interactive mode
- Score saving support for both `play` and `guess` game modes

### Improved
- Clear separation between interactive (in-memory) and non-interactive flows
- Authentication-aware score handling (guest vs logged-in users)



## [0.4.0] – 2026-01-21

### Added
- New `play` command providing a win/lose dice game option.

### Changed
- Renamed the `display` command to `roll` for improved clarity and consistency.

### Fixed
- Blocked deletion of the currently active account.
- Added password verification before account deletion in both CLI and interactive modes to improve security.



## [0.3.0] - 2026-01-20

### Added
- Formatted leaderboard table for clear and structured score display
- Formatted players table for improved user listing readability

### Changed
- Renamed CLI commands for better semantics and consistency:
  - `view users` → `player list`
  - `view scores` → `leaderboard`
  - `delete user` → `player delete`
- Improved overall CLI user experience and command clarity

### Fixed
- Resolved issue where delete success/error message was displayed after three failed delete attempts



## [0.2.0] - 2026-01-20
- Added colorful UI console messages using Rich
- Added a panel for the interactive session
- Added a progress bar for the dice roll



## [0.1.0] – Initial Milestone - 2026-01-17

- Added SQLite database persistence for user data
- Implemented Argon2 password security
- Added login and logout functionality
- Introduced 4 interactive dice game commands
- Implemented interactive session management stored in memory
