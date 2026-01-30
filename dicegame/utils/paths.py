from pathlib import Path


def get_app_data_dir():
    """Returns the directory where the application's data will be saved in"""

    path = Path.home() / '.local/share/dicegame-cli'
    path.mkdir(parents=True, exist_ok=True)

    return path

#def log_dir():
 #   """Returns the log directory"""
  #  path = get_app_data_dir() / 'logs'
   # path.mkdir(parents=True,exist_ok=True)

#    return path


#LOG_DIR = log_dir()

#LOG_PATH = log_dir() / 'dicegame-cli.log'

DB_PATH = get_app_data_dir() / 'dicegame-cli.db'

SESSION_FILE = get_app_data_dir() / 'session'

