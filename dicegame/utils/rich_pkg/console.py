from rich.console import Console
from rich.theme import Theme


# Sets color theme to be used on console messages based on the message category
theme = Theme({
    'info': 'cyan',
    'warning': 'bold yellow',
    'error': 'bold red',
    'success': 'bold green'
})

# Returns console object
console = Console(theme=theme)

# Prints files to stderr
err_console = Console(stderr=True)
