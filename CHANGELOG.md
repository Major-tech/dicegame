## [v0.3.0] - 2026-01-20

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


## [v0.2.0] - 2026-01-20
- Added colorful UI console messages using Rich
- Added a panel for the interactive session
- Added a progress bar for the dice roll


## [v0.1.0] – Initial Milestone - 2026-01-17

- Added SQLite database persistence for user data
- Implemented Argon2 password security
- Added login and logout functionality
- Introduced 4 interactive dice game commands
- Implemented interactive session management stored in memory
