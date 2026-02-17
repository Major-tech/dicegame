from importlib.metadata import version, PackageNotFoundError


def get_version() -> str:
    """Returns the current app version"""

    try:
        return version("dicegame")
    except PackageNotFoundError:
        return "0.0.0-dev"
