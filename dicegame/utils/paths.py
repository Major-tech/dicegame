from pathlib import Path


def get_app_data_dir():
    path = Path.home() / '.local/share/dicegame'
    path.mkdir(parents=True, exist_ok=True)

    return path


LOG_PATH = get_app_data_dir() / 'dicegame.log'

DB_PATH = get_app_data_dir() / 'dicegame.db'
