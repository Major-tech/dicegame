from pathlib import Path


def get_app_data_dir():
    """Returns the directory where the application's data will be saved in"""

    path = Path.home() / '.local/share/dicegame'
    path.mkdir(parents=True, exist_ok=True)

    return path


DB_PATH = get_app_data_dir() / 'dicegame.db'

SESSION_FILE = get_app_data_dir() / 'session'

